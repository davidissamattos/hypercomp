import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import logging
from timeit import default_timer as timer
logging.basicConfig(level=logging.CRITICAL)
logger = logging.getLogger(__name__)


from CostFunctions import *
from utils import * 

#Hyperopt TPE and rand
from hyperopt import fmin, tpe, hp, rand
#bayes_opt
from bayes_opt import BayesianOptimization
from bayes_opt import UtilityFunction
#CMA-ES
import cma

#BOHB
import hpbandster.core.nameserver as hpns
import hpbandster.core.result as hpres
from hpbandster.optimizers import BOHB as BOHB
from hpbandster.optimizers import HyperBand as HyperBand
import ConfigSpace as CS
from hpbandster.core.worker import Worker


class Simulator():
    """
    This is the class that implements all the simulations
    The class initializes receiving a CostFunction class as parameter and other simulation parameters such as number of iterations, noise and simulation
    
    To extend we implement a new function that loops thorugh the number of iterations and give the output result
    This result must be saved and appended in the results vector
    """
    def __init__(self, objFuncClass, sd=1, maxfeval= 50, nsim=1):
        self.objFuncClass = objFuncClass
        #standard deviation
        self.sd=sd
        #number of iterations for the algorithm. Number of function evaluations
        self.maxfeval = maxfeval
        #number of simulations 
        self.nsim = nsim
        self.results = []
        pass

    def RunRandomSearch(self):
        """
        Runs the random search algorithm from the hyperopt package
        """
        objective = self.objFuncClass(functionProperties=self.objFuncClass.functionProperties,
                                      sd=self.maxfeval,
                                      maxfevals=self.maxfeval)
        obj_space = self.objFuncClass.functionProperties['searchSpace']
        obj_space_type = self.objFuncClass.functionProperties['spaceType']
     
        #assembling the space
        i=0
        space = []
        for dim_i in obj_space:
            spc = None
            varname = 'x' + str(i)
            if obj_space_type[i] == 'uniform':
                spc = hp.uniform(varname, dim_i[0], dim_i[1])
            #TODO: categorical
            if  obj_space_type[i] == 'categorical':
                raise TypeError('This algorithm doesnt accept categorical variables')
            space.append(spc)
            i=i+1

        #run the random search algorithm
        start = timer()
        best = fmin(fn=objective,
                    space= space,
                    algo=rand.suggest,
                    max_evals=self.maxfeval)
        end = timer()
        timetocomplete = end-start
        
        #saving the results
        best_arm = dictToArray(best)
        result = objective.GenerateInfo(best_arm= best_arm,
                                timetocomplete= timetocomplete,
                                algorithm_name= 'RandomSearch')
        self.results.append(result)
        return

    def RunTPE(self):
        """
        Runs the TPE algorithm from the hyperopt package
        """
        objective = self.objFuncClass(functionProperties=self.objFuncClass.functionProperties,
                                      sd=self.maxfeval,
                                      maxfevals=self.maxfeval)
        obj_space = self.objFuncClass.functionProperties['searchSpace']
        obj_space_type = self.objFuncClass.functionProperties['spaceType']
     
        #assembling the space
        i=0
        space = []
        for dim_i in obj_space:
            spc = None
            varname = 'x' + str(i)
            if obj_space_type[i] == 'uniform':
                spc = hp.uniform(varname, dim_i[0], dim_i[1])
            
            #TODO: categorical
            if  obj_space_type[i] == 'categorical':
                raise TypeError('This algorithm doesnt accept categorical variables')
            space.append(spc)
            i=i+1

        #run the random search algorithm
        start = timer()
        best = fmin(fn=objective,
                    space= space,
                    algo=tpe.suggest,
                    max_evals=self.maxfeval)
        end = timer()
        timetocomplete = end-start
        
        #saving the results
        best_arm = dictToArray(best)
        result= objective.GenerateInfo(best_arm= best_arm,
                                timetocomplete= timetocomplete,
                                algorithm_name= 'TPE')
        self.results.append(result)
        return
    
    def RunBayesianEI(self, xi, kappa):
        """
        Runs Bayesian optimization with Expected improvement algorithm from the hyperopt package
        """
        objective = self.objFuncClass(functionProperties=self.objFuncClass.functionProperties,
                                      sd=self.maxfeval,
                                      maxfevals=self.maxfeval)
        obj_space = self.objFuncClass.functionProperties['searchSpace']
        obj_space_type = self.objFuncClass.functionProperties['spaceType']
     
        #assembling the space
        i=0
        space = {}
        for dim_i in obj_space:
            varname = 'x' + str(i)
            if obj_space_type[i] == 'uniform':
                spc = (dim_i[0], dim_i[1])
            #TODO: categorical
            if  obj_space_type[i] == 'categorical':
                raise TypeError('This algorithm doesnt accept categorical variables')
            space[varname] = spc
            i=i+1

        #run the random search algorithm
        start = timer()
        utility = UtilityFunction(kind='ei', kappa = kappa, xi=xi)
        optimizer = BayesianOptimization(
                f=None,
                pbounds=space,
                random_state=1,
                verbose=0 #silent mode
            )
        for i in range(self.maxfeval):
            #Get the next arm to try
            next_point_to_probe = optimizer.suggest(utility)
            x = dictToArray(next_point_to_probe)
            #evaluate the function
            target = objective(x)
            #Register and update the states
            optimizer.register(params=next_point_to_probe,
                                target = target)
        end = timer()
        timetocomplete =end-start
        
        #saving the results
        best = optimizer.max
        algo= 'BayesEI-xi-'+str(xi)+'-kappa-'+str(kappa)
        best_arm = dictToArray(best['params'])
        result= objective.GenerateInfo(best_arm= best_arm,
                                timetocomplete= timetocomplete,
                                algorithm_name= algo)
        self.results.append(result)
        return

    def RunBayesianUCB(self, xi, kappa):
        """
        Runs Bayesian optimization with UCB algorithm from the hyperopt package
        """
        objective = self.objFuncClass(functionProperties=self.objFuncClass.functionProperties,
                                      sd=self.maxfeval,
                                      maxfevals=self.maxfeval)
        obj_space = self.objFuncClass.functionProperties['searchSpace']
        obj_space_type = self.objFuncClass.functionProperties['spaceType']
     
        #assembling the space
        i=0
        space = {}
        for dim_i in obj_space:
            varname = 'x' + str(i)
            if obj_space_type[i] == 'uniform':
                spc = (dim_i[0], dim_i[1])
            #TODO: categorical
            if  obj_space_type[i] == 'categorical':
                raise TypeError('This algorithm doesnt accept categorical variables')
            space[varname] = spc
            i=i+1

        #run the random search algorithm
        start = timer()
        utility = UtilityFunction(kind='ucb', kappa = kappa, xi=xi)
        optimizer = BayesianOptimization(
                f=None,
                pbounds=space,
                random_state=1,
                verbose=0 #silent mode
            )
        for i in range(self.maxfeval):
            #Get the next arm to try
            next_point_to_probe = optimizer.suggest(utility)
            x = dictToArray(next_point_to_probe)
            #evaluate the function
            target = objective(x)
            #Register and update the states
            optimizer.register(params=next_point_to_probe,
                                target = target)
        end = timer()
        timetocomplete =end-start
        
        #saving the results
        best = optimizer.max
        algo= 'BayesUCB-xi-'+str(xi)+'-kappa-'+str(kappa)
        best_arm = dictToArray(best['params'])
        result= objective.GenerateInfo(best_arm= best_arm,
                                timetocomplete= timetocomplete,
                                algorithm_name= algo)
        self.results.append(result)
        return

    def RunBayesianPOI(self, xi, kappa):
        """
        Runs Bayesian optimization with UCB algorithm from the hyperopt package
        """
        objective = self.objFuncClass(functionProperties=self.objFuncClass.functionProperties,
                                      sd=self.maxfeval,
                                      maxfevals=self.maxfeval)
        obj_space = self.objFuncClass.functionProperties['searchSpace']
        obj_space_type = self.objFuncClass.functionProperties['spaceType']
     
        #assembling the space
        i=0
        space = {}
        for dim_i in obj_space:
            varname = 'x' + str(i)
            if obj_space_type[i] == 'uniform':
                spc = (dim_i[0], dim_i[1])
            #TODO: categorical
            if  obj_space_type[i] == 'categorical':
                raise TypeError('This algorithm doesnt accept categorical variables')
            space[varname] = spc
            i=i+1

        #run the random search algorithm
        start = timer()
        utility = UtilityFunction(kind='poi', kappa = kappa, xi=xi)
        optimizer = BayesianOptimization(
                f=None,
                pbounds=space,
                random_state=1,
                verbose=0 #silent mode
            )
        for i in range(self.maxfeval):
            #Get the next arm to try
            next_point_to_probe = optimizer.suggest(utility)
            x = dictToArray(next_point_to_probe)
            #evaluate the function
            target = objective(x)
            #Register and update the states
            optimizer.register(params=next_point_to_probe,
                                target = target)
        end = timer()
        timetocomplete =end-start
        
        #saving the results
        best = optimizer.max
        algo= 'BayesPOI-xi-'+str(xi)+'-kappa-'+str(kappa)
        best_arm = dictToArray(best['params'])
        result= objective.GenerateInfo(best_arm= best_arm,
                                timetocomplete= timetocomplete,
                                algorithm_name= algo)
        self.results.append(result)
        return

    def RunCMAES(self, sigma=0.5):
        """
        Runs the CMAES algorithm from the cma package
        """
        objective = self.objFuncClass(functionProperties=self.objFuncClass.functionProperties,
                                      sd=self.maxfeval,
                                      maxfevals=self.maxfeval)
        # the algorithm doenst use the space
        # run the random search algorithm
        options = {'maxfevals': self.maxfeval,
                   'verb_disp': 0}
        start = timer()
        xopt, es = cma.fmin2(objective_function=objective,
                             x0=objective.functionProperties['x0'],
                             sigma0=sigma,
                             options=options)

        end = timer()
        timetocomplete = end - start

        # saving the results
        result = objective.GenerateInfo(best_arm=xopt,
                                        timetocomplete=timetocomplete,
                                        algorithm_name='CMA-ES')
        self.results.append(result)
        return


    def RunBOHB(self):
        #first we get the space
        objective = self.objFuncClass(functionProperties=self.objFuncClass.functionProperties,
                                      sd=self.maxfeval,
                                      maxfevals=self.maxfeval)
        obj_space = self.objFuncClass.functionProperties['searchSpace']
        obj_space_type = self.objFuncClass.functionProperties['spaceType']


        #Then we define a worker
        class MyWorker(Worker):
            def __init__(self, *args, **kwargs):
                super().__init__(*args, **kwargs)

            def compute(self, config, budget, **kwargs):
                x = dictToArray(config)
                res = objective(x)
                return ({
                    'loss': float(res),  # this is the a mandatory field to run hyperband
                    'info': res  # can be used for any user-defined information - also mandatory
                })

            @staticmethod
            def get_configspace():
                config_space = CS.ConfigurationSpace()
                # assembling the space
                i = 0
                space = []
                for dim_i in obj_space:
                    spc = None
                    varname = 'x' + str(i)
                    if obj_space_type[i] == 'uniform':
                        config_space.add_hyperparameter(CS.UniformFloatHyperparameter(varname, lower=dim_i[0], upper=dim_i[1]))
                    # TODO: categorical
                    if obj_space_type[i] == 'categorical':
                        raise TypeError('This algorithm doesnt accept categorical variables')
                    space.append(spc)
                    i = i + 1
                return (config_space)

        #Then we initialize the server and the worker
        NS = hpns.NameServer(run_id='example1', host='127.0.0.1', port=None)
        NS.start()
        w = MyWorker(nameserver='127.0.0.1', run_id='example1')
        w.run(background=True)
        #We run the algorithm

        bohb = BOHB(configspace=w.get_configspace(),
                    run_id='example1', nameserver='127.0.0.1',
                    min_budget=1, max_budget=1 #budget is the number of epochs that will run so it is 1 for min and max
                    )
        start = timer()
        res = bohb.run(n_iterations=self.maxfeval)
        end = timer()
        timetocomplete = end - start

        #We shutdown the server
        bohb.shutdown(shutdown_workers=True)
        NS.shutdown()

        #We get the response
        id2config = res.get_id2config_mapping()
        incumbent = res.get_incumbent_id()
        best = id2config[incumbent]['config']

        #We log
        best_arm = dictToArray(best)
        result = objective.GenerateInfo(best_arm=best_arm,
                                        timetocomplete=timetocomplete,
                                        algorithm_name='BOHB')
        self.results.append(result)
        return

    def RunHyperBand(self):
        #first we get the space
        objective = self.objFuncClass(functionProperties=self.objFuncClass.functionProperties,
                                      sd=self.maxfeval,
                                      maxfevals=self.maxfeval)
        obj_space = self.objFuncClass.functionProperties['searchSpace']
        obj_space_type = self.objFuncClass.functionProperties['spaceType']


        #Then we define a worker
        class MyWorker(Worker):
            def __init__(self, *args, **kwargs):
                super().__init__(*args, **kwargs)

            def compute(self, config, budget, **kwargs):
                x = dictToArray(config)
                res = objective(x)
                return ({
                    'loss': float(res),  # this is the a mandatory field to run hyperband
                    'info': res  # can be used for any user-defined information - also mandatory
                })

            @staticmethod
            def get_configspace():
                config_space = CS.ConfigurationSpace()
                # assembling the space
                i = 0
                space = []
                for dim_i in obj_space:
                    spc = None
                    varname = 'x' + str(i)
                    if obj_space_type[i] == 'uniform':
                        config_space.add_hyperparameter(CS.UniformFloatHyperparameter(varname, lower=dim_i[0], upper=dim_i[1]))
                    # TODO: categorical
                    if obj_space_type[i] == 'categorical':
                        raise TypeError('This algorithm doesnt accept categorical variables')
                    space.append(spc)
                    i = i + 1
                return (config_space)

        #Then we initialize the server and the worker
        NS = hpns.NameServer(run_id='example1', host='127.0.0.1', port=None)
        NS.start()
        w = MyWorker(nameserver='127.0.0.1', run_id='example1')
        w.run(background=True)
        #We run the algorithm

        hyperband = HyperBand(configspace=w.get_configspace(),
                    run_id='example1', nameserver='127.0.0.1',
                    min_budget=1, max_budget=1 #budget is the number of epochs that will run so it is 1 for min and max
                    )
        start = timer()
        res = hyperband.run(n_iterations=self.maxfeval)
        end = timer()
        timetocomplete = end - start

        #We shutdown the server
        hyperband.shutdown(shutdown_workers=True)
        NS.shutdown()

        #We get the response
        id2config = res.get_id2config_mapping()
        incumbent = res.get_incumbent_id()
        best = id2config[incumbent]['config']

        #We log
        best_arm = dictToArray(best)
        result = objective.GenerateInfo(best_arm=best_arm,
                                        timetocomplete=timetocomplete,
                                        algorithm_name='HyperBand')
        self.results.append(result)
        return


    def run(self):
        """
        Run all the algorithms for a number of times
        """
        for i in range(self.nsim):
            print('Sim loop number: ', i)
            self.RunRandomSearch()
            # self.RunTPE()
            # self.RunBayesianUCB(xi=0.0,kappa=1.0)#more exploitation
            # self.RunBayesianUCB(xi=0.0,kappa=10.0)#more exploration
            # self.RunBayesianEI(xi=0.10,kappa=1.0)#more exploration
            # self.RunBayesianEI(xi=0.0,kappa=1.0)#more exploitation
            # self.RunBayesianPOI(xi=0.10,kappa=1.0)#more exploration
            # self.RunBayesianPOI(xi=0.0,kappa=1.0)#more exploitation
            self.RunCMAES()
            self.RunBOHB()
            self.RunHyperBand()

        
        return


    def saveResults(self):
        """
        Saving the results as a csv file
        """
        df = pd.DataFrame(self.results)
        print(df)
        return
