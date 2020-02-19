from Algorithms import Algorithm
#Hyperopt TPE and rand
from hyperopt import fmin, tpe, hp, rand, atpe
from utils import *
import logging
logger = logging.getLogger('Algorithms')

__all__ = ['RandomSearch','ATPE','TPE']

class Hyperopt(Algorithm):
    """
    Implement the algorithms of the hyperopt package

    Parameters from the super class to keep track

    """

    def __init__(self, algorithm_name, objective, maxfeval):
        super().__init__(algorithm_name, objective, maxfeval)
        self.algorithm_name = algorithm_name
        if algorithm_name not in ['RandomSearch', 'TPE', 'ATPE']:
            logger.error('HyperOpt does not have algorithm :' + str(algorithm_name))
            raise Exception


    def assemblespace(self):
        """
        We need to create a variable self.space to store the space to be used by the algorithm
        Changes between algorithms

        """
        try:
            obj_space = self.objective.functionProperties['searchSpace']
            obj_space_type = self.objective.functionProperties['spaceType']

            # assembling the space
            i = 0
            self.space = []
            for dim_i in obj_space:
                spc = None
                varname = 'x' + str(i)
                if obj_space_type[i] == 'uniform':
                    spc = hp.uniform(varname, dim_i[0], dim_i[1])
                # TODO: categorical
                if obj_space_type[i] == 'categorical':
                    logger.error('Functionality not implemented yet')
                    raise TypeError('This algorithm doesnt accept categorical variables yet')
                self.space.append(spc)
                i = i + 1
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
            algo = None
            if self.algorithm_name == 'RandomSearch':
                algo = rand.suggest
            elif self.algorithm_name == 'TPE':
                algo = tpe.suggest
            elif self.algorithm_name == 'ATPE':
                algo = atpe.suggest
            best = fmin(fn=self.objective,
                        space= self.space,
                        algo=algo,
                        max_evals=self.maxfeval,
                        show_progressbar=False,
                        verbose=0)

            best_arm = convertToArray(best)
            success = True
        except:
            logger.warning('Optimization for ' + str(self.algorithm_name) + ' failed with cost function: ' + str(
                self.objective.GetCostFunctionName()))
            best_arm = NAN
            success = False

        return best_arm, success, self.objective

class RandomSearch(Hyperopt):
    def __init__(self, objective, maxfeval):
        super().__init__(objective=objective,
                         maxfeval=maxfeval,
                         algorithm_name='RandomSearch')

class TPE(Hyperopt):
    def __init__(self, objective, maxfeval):
        super().__init__(objective=objective,
                         maxfeval=maxfeval,
                         algorithm_name='TPE')

class ATPE(Hyperopt):
    def __init__(self, objective, maxfeval):
        super().__init__(objective=objective,
                         maxfeval=maxfeval,
                         algorithm_name='ATPE')