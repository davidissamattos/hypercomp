import numpy as np
import pandas as pd
import logging
from timeit import default_timer as timer
logger = logging.getLogger(__name__)
import os, re, shutil, importlib

#GoogleCloud bucket
from google.cloud import storage
# say where your private key to google cloud exists
from Algorithms import all_algorithms


class Comparator():
    """
    This is the class that implements all the simulations
    The class initializes receiving a CostFunction class as parameter and other simulation parameters such as number of iterations, noise and simulation
    
    To extend we implement a new function that loops thorugh the number of iterations and give the output result
    This result must be saved and appended in the results vector
    """
    def __init__(self, objFuncClass,
                 results_folder,
                 filename,
                 sd,
                 maxfeval,
                 maxfevalBydimensions=False, #IF this is TRUE we multiply maxfeval by the dimensions to obtain the new number of maximum function evaluations
                 nsim=1,
                 useGCP=False,
                 GCPbucketName=None):
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

        if self.useGCP:
            if GCPbucketName==None:
                raise Exception('You need to set a GCP bucket name')
            else:
                self.GCPbucketName = GCPbucketName
                self.GCPbucketFolderName = results_folder
                self.storage_client = storage.Client()
                self.bucket = self.storage_client.get_bucket(GCPbucketName)
        pass


    def run(self):
        """
        Run all algorithms for nsim times then rank and save them
        :return:
        """
        for i in range(self.nsim):
            #dinamically importing the algorithm classes from Algorithms
            for algname in all_algorithms:
                module = importlib.import_module('Algorithms')
                cl = getattr(module, algname)  # cl is a class of the CostFunctions imported dynamically
                result = self.run_algorithm(cl)
                result['simNumber'] = i
                self.results.append(result)
        #After all iterations we rank them by simulation number
        df = pd.DataFrame(self.results)
        # Rank by true distance
        df['RankTrueRewardDifference'] = df.groupby('simNumber')['TrueRewardDifference'].rank(method='average', ascending=True)
        # Rank the regret
        df['RankCumulativeRegret'] = df.groupby('simNumber')['CumulativeRegret'].rank(method='average', ascending=True)
        # rank the euclidean distance
        df['RankEuclideanDistance'] = df.groupby('simNumber')['EuclideanDistance'].rank(method='average', ascending=True)

        #saving results depending if it is google cloud or not
        self.saveResults(df)
        self.cleanUp()



    def run_algorithm(self, algoClass):
        """
        Run a single instance of an algorithm
        :return:
        """
        if self.maxfevalBydimensions:
            maxfeval = int(self.objFuncClass.functionProperties['Ndimensions']*self.maxfeval)
            objective = self.objFuncClass(functionProperties=self.objFuncClass.functionProperties,
                                          sd=self.maxfeval,
                                          maxfeval=maxfeval)
        else:
            objective = self.objFuncClass(functionProperties=self.objFuncClass.functionProperties,
                                      sd=self.maxfeval,
                                      maxfeval=self.maxfeval)
        algo = algoClass(objective=objective,
                         maxfeval=self.maxfeval)
        result = algo.run()
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

    def saveResults(self, df):
        """
        Saving the df results as a csv file
        Also creates the ranks by the different variables
        """
        if self.useGCP:
            # First lets create a temporary folder to save
            cwpath = os.getcwd()
            path = os.path.join(cwpath, 'temp')
            if not os.path.isdir(path):
                os.mkdir(path)
            savepath = os.path.join(path, self.filename)
            df.to_csv(savepath)

            # now we upload to the GCP
            blob = self.bucket.blob(self.GCPbucketFolderName + self.filename)
            blob.upload_from_filename(savepath)

            # The folder is always deleted in the cleanup
        else:
            savepath = os.path.join(self.resultsFolder, self.filename)
            df.to_csv(savepath)
        return