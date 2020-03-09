import numpy as np
import pandas as pd
import logging
logger = logging.getLogger(__name__)
import os, re, shutil, importlib
from tqdm import tqdm

#GoogleCloud bucket
from google.cloud import storage
# say where your private key to google cloud exists
from Algorithms import all_algorithms, niapy_random_search, no_bayesian

class Comparator():
    """
    This is the class that implements all the simulations
    The class initializes receiving a CostFunction class as parameter and other simulation parameters such as number of iterations, noise and simulation
    
    To extend we implement a new function that loops thorugh the number of iterations and give the output result
    This result must be saved and appended in the results vector
    """
    def __init__(self,
                 objFuncClass,
                 results_folder,
                 filename,
                 sd,
                 maxfeval,
                 maxfevalBydimensions=False, #IF this is TRUE we multiply maxfeval by the dimensions to obtain the new number of maximum function evaluations
                 nsim=1,
                 useGCP=False,
                 GCPbucketName=None,
                 timeout_min=15,
                 nfevalbydimensions=False,
                 algorithmgroup='all'):

        self.objFuncClass = objFuncClass
        #standard deviation
        self.sd=sd
        #number of iterations for the algorithm. Number of function evaluations
        self.maxfeval = maxfeval
        self.maxfevalBydimensions = maxfevalBydimensions
        #number of simulations 
        self.nsim = nsim
        self.results = []
        self.resultsFolder = results_folder
        self.filename = filename
        self.useGCP=useGCP
        self.nfevalbydimensions=nfevalbydimensions
        self.algorithmgroup = algorithmgroup
        if algorithmgroup is None:
            self.algorithmgroup='all'
        if timeout_min > 0:
            self.timeout = int(timeout_min * 60)
        else:
            self.timeout = int(15 * 60)
        logger.info('Using a timeout of '+ str(self.timeout)+ ' seconds per algorithm')

        if self.useGCP:
            if GCPbucketName is None:
                logger.error('You need to set a GCP bucket name')
                raise Exception
            else:
                self.GCPbucketName = GCPbucketName
                self.GCPbucketFolderName = self.resultsFolder
                self.storage_client = storage.Client()
                self.bucket = self.storage_client.get_bucket(GCPbucketName)
        pass


    def run(self):
        """
        Run all algorithms for nsim times then rank and save them
        :return:
        """
        if self.algorithmgroup == 'all':
            alg_to_run = all_algorithms
        elif self.algorithmgroup == 'niapy':
            alg_to_run = niapy_random_search
        elif self.algorithmgroup == 'no_bayesian':
            alg_to_run = no_bayesian
        else:
            raise ValueError('There is no algorithm class called: ' + self.algorithmgroup)
        #tqdm is just to create a progress bar
        for i in tqdm(range(self.nsim), desc='NSim'):
            logger.info('Running all the algorithms for simulation number ' + str(i) + ' and cost function '+ str(self.objFuncClass))
            #dinamically importing the algorithm classes from Algorithms
            results = []
            for algname in alg_to_run:
                module = importlib.import_module('Algorithms')
                cl = getattr(module, algname)  # cl is a class of the Algorithms imported dynamically
                result = self.run_algorithm(cl)
                result['simNumber'] = i
                results.append(result)
            #After all iterations we rank them by simulation number
            # df = pd.DataFrame(self.results)
            df = pd.DataFrame(results)

            #saving results depending if it is google cloud or not
            self.saveResults(df,i)
            self.cleanUp()



    def run_algorithm(self, algoClass):
        """
        Run a single instance of an algorithm
        :return:
        """
        #We are adding here as a class variable simply because it is somehow lost in the middle of the calculations the instantiation and reference

        #we initialize as if nfevalbydimensions was False and then we change
        self._objective = self.objFuncClass(functionProperties=self.objFuncClass.functionProperties,
                                      sd=self.sd,
                                      maxfeval=self.maxfeval)

        # here we take into account the number of dimensions
        # we need to keep the self.maxfeval parameter constant for the other functions
        # but we need to initialize the algorithm with the updated maxfeval from the cost function
        algo_maxfeval=self.maxfeval
        if self.nfevalbydimensions:
            self._objective.ChangeMaxFevalBasedOnDimensions(k=self.maxfeval)
            algo_maxfeval =self._objective.maxfeval

        algo = algoClass(objective=self._objective,
                         maxfeval=algo_maxfeval)


        result = algo.run(timeout=self.timeout)
        return result

    def cleanUp(self):
        """
        Deleting some of the folders created by other algorithms
        :return:
        """

        def purge(dir, pattern):
            for f in os.listdir(dir):
                if re.search(pattern, f):
                    shutil.rmtree(os.path.join(dir, f))

        purge(os.getcwd(), 'smac3-output*')
        purge(os.getcwd(), 'outcmaes*')
        purge(os.getcwd(), 'temp')
        logger.info('All temporary files were deleted')

    def saveResults(self, df,i):
        """
        Saving the df results as a csv file
        Also creates the ranks by the different variables
        df is the data frame
        i is the simulation number since we always save it
        """
        newfilename = self.filename + str(i) + '.csv'
        if self.useGCP:
            # First lets create a temporary folder to save
            cwpath = os.getcwd()
            path = os.path.join(cwpath, 'temp')
            if not os.path.isdir(path):
                os.mkdir(path)
            savepath = os.path.join(path, newfilename)
            df.to_csv(savepath)

            # now we upload to the GCP
            gcpsavepath = os.path.join(self.GCPbucketFolderName,newfilename)
            blob = self.bucket.blob(gcpsavepath)
            blob.upload_from_filename(savepath)

            # The folder is always deleted in the cleanup
        else:
            savepath = os.path.join(self.resultsFolder,newfilename)
            df.to_csv(savepath)
        return