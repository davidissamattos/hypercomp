from Algorithms import Algorithm
#CMA-ES
import numpy as np
import cma
from utils import *
import logging
logger = logging.getLogger('Algorithms')

__all__ = ['CMAES']

class CMAES(Algorithm):
    """
    From the cma package
    """
    def __init__(self, objective, maxfeval, sigma=0.5):
        self.algorithm_name = 'CMAES'
        super().__init__(self.algorithm_name, objective, maxfeval)
        self.sigma =sigma

    def assemblespace(self):
        """
        This algorithm just need the initial value and the options
        """
        try:
            self.options = {
                'maxfeval': self.maxfeval,
                'verb_disp': 0
            }
            self.x0 = self.objective.functionProperties['x0']
        except:
            logger.error('Error assembling the space for ' + str(self.algorithm_name) + ' with cost function: ' + str(
                self.objective.GetCostFunctionName()))
            pass

    def optimize(self):
        try:
            xopt, es = cma.fmin2(objective_function=self.objective,
                                 x0=self.x0,
                                 sigma0=self.sigma,
                                 options=self.options)
            best_arm = convertToArray(xopt)
            success = True
        except:
            logger.warning('Optimization for ' + str(self.algorithm_name) + ' failed with cost function: ' + str(
                self.objective.GetCostFunctionName()))
            best_arm = NAN
            success = False
        return best_arm, success
