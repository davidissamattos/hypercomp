from Algorithms import Algorithm
import numpy as np
import hpbandster.core.nameserver as hpns
import hpbandster.core.result as hpres
from hpbandster.optimizers import BOHB as BOHB
from hpbandster.optimizers import HyperBand as HyperBand
import ConfigSpace as CS
from hpbandster.core.worker import Worker
from utils import *
import logging
logger = logging.getLogger('Algorithms')

__all__ = ['hpbandsterHyperBand','hpbandsterBOHB']

class HpbandsterAlgorithms(Algorithm):
    """
    Implement the algorithms of the hyperopt package

    Parameters from the super class to keep track

    """

    def __init__(self, algorithm_name, objective, maxfeval):
        super().__init__(algorithm_name, objective, maxfeval)
        self.algorithm_name = algorithm_name
        if algorithm_name not in ['BOHB', 'HyperBand']:
            raise Exception('hpbandster does not have algorithm :' + str(algorithm_name))


    def assemblespace(self):
        """
        We need to create a variable self.space to store the space to be used by the algorithm
        Changes between algorithms

        """
        try:
            obj_space = self.objective.functionProperties['searchSpace']
            obj_space_type = self.objective.functionProperties['spaceType']
            objective = self.objective
            # Then we define a worker
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
                            config_space.add_hyperparameter(
                                CS.UniformFloatHyperparameter(varname, lower=dim_i[0], upper=dim_i[1]))
                        # TODO: categorical
                        if obj_space_type[i] == 'categorical':
                            logger.error('This algorithm doesnt accept categorical variables. Functionality not implemented yet')
                            raise Exception
                        space.append(spc)
                        i = i + 1
                    return (config_space)

            # Then we initialize the server and the worker
            self.NS = hpns.NameServer(run_id='example1', host='127.0.0.1', port=None)
            self.NS.start()
            self.worker = MyWorker(nameserver='127.0.0.1', run_id='example1')
            self.worker.run(background=True)
            # We run the algorithm
        except:
            logger.error('Error assembling the space for ' + str(self.algorithm_name) + ' with cost function: ' + str(
                self.objective.GetCostFunctionName()))
            pass

    def optimize(self):
        """
        The main optimization procedure
        Should return the best arm as and array/ list
        :return:

        THe instance to be optimized is the self.objective value
        """
        try:
            if self.algorithm_name == 'BOHB':
                algo = BOHB(configspace=self.worker.get_configspace(),
                            run_id='example1', nameserver='127.0.0.1',
                            min_budget=1, max_budget=1
                            # budget is the number of epochs that will run so it is 1 for min and max
                            )
            else:
                algo = HyperBand(configspace=self.worker.get_configspace(),
                                      run_id='example1', nameserver='127.0.0.1',
                                      min_budget=1, max_budget=1
                                      # budget is the number of epochs that will run so it is 1 for min and max
                                      )

            res = algo.run(n_iterations=self.maxfeval)
            #We shutdown the server
            algo.shutdown(shutdown_workers=True)
            self.NS.shutdown()
            id2config = res.get_id2config_mapping()
            incumbent = res.get_incumbent_id()
            best = id2config[incumbent]['config']
            best_arm = convertToArray(best)
            success = True
        except:
            logger.warning('Optimization for ' + str(self.algorithm_name) + ' failed with cost function: ' + str(
                self.objective.GetCostFunctionName()))
            best_arm = NAN
            success = False
        return best_arm, success


class hpbandsterHyperBand(HpbandsterAlgorithms):
    def __init__(self, objective, maxfeval):
        super().__init__(objective=objective,
                         maxfeval=maxfeval,
                         algorithm_name='HyperBand')

class hpbandsterBOHB(HpbandsterAlgorithms):
    def __init__(self, objective, maxfeval):
        super().__init__(objective=objective,
                         maxfeval=maxfeval,
                         algorithm_name='BOHB')