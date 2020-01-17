from Algorithms import Algorithm
#Hyperopt TPE and rand
from Algorithms.AlgorithmsFromSource.MinmLGHOO import MinmLGHOO
from utils import *
import logging
logger = logging.getLogger('Algorithms')

__all__ = ['mLGHOO', 'HOO']

class BaseFormLGHOO(Algorithm):
    """
    Implement the algorithms of the hyperopt package

    Parameters from the super class to keep track

    """

    def __init__(self, algorithm_name, objective, maxfeval, height=20, v1=10.0, rho=0.5, minimum_grow=1):
        super().__init__(algorithm_name, objective, maxfeval)
        self.algorithm_name = algorithm_name
        self.height = height
        self.v1 = v1
        self.rho = rho
        self.minimum_grow=minimum_grow


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
                spc = {}
                if obj_space_type[i] == 'uniform':
                    spc['name'] = 'x' + str(i)
                    spc['height_limit'] = self.height
                    spc['arm_min'] = dim_i[0]
                    spc['arm_max'] = dim_i[1]
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
            mlghoo = MinmLGHOO(arms_def=self.space,
                               v1=self.v1,
                               rho=self.rho,
                               minimum_grow=self.minimum_grow,
                               p_vector=None)

            for i in range(self.maxfeval):
                arm = mlghoo.select_arm()
                reward = self.objective(arm)
                mlghoo.update(chosen_arm=arm, reward=reward)

            best = mlghoo.get_best_arm_value()
            best_arm = convertToArray(best)
            success = True
        except:
            logger.warning('Optimization for ' + str(self.algorithm_name) + ' failed with cost function: ' + str(
                self.objective.GetCostFunctionName()))
            best_arm = NAN
            success = False

        return best_arm, success

class mLGHOO(BaseFormLGHOO):
    def __init__(self, objective, maxfeval):
        super().__init__(objective=objective,
                         maxfeval=maxfeval,
                         algorithm_name='mLGHOO',height=15,minimum_grow=4)

class HOO(BaseFormLGHOO):
    def __init__(self, objective, maxfeval):
        super().__init__(objective=objective,
                         maxfeval=maxfeval,
                         algorithm_name='HOO',height=100,minimum_grow=1)