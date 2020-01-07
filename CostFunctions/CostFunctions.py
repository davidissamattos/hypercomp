import numpy as np
from scipy import spatial
from abc import ABC, abstractmethod
from utils import *
import logging
logger = logging.getLogger(__name__)
__all__ = ['CostFunctions']


class CostFunctions(ABC):
    def __init__(self, functionProperties, sd=1, maxfeval=10, tol=0.001):
        # Saving parameters
        self._maxfevals = maxfeval
        self.sd = sd
        self.functionProperties = functionProperties
        self.functionProperties['tol'] = tol
        # function properties is a dictionary with several values.
        # Below we have some of the most used in other parts of this class
        self.optimalArms = self.functionProperties['optimalArms']
        self.minimumValue = self.functionProperties['minimumValue']

        # Initializing variables
        self._nfeval = 0
        # Here we log all the parameters that were passed to this function
        self.requestedArms = []
        # Here we log all the output values with noise that the function gives
        self.outputValues = []

    # Needs to be implemented the function without noise
    @abstractmethod
    def func(self, x):
        """
        Mathematical expression of the function
        x is a python array/numpy
        return: a value
        """
        pass

    def eval(self, x):
        try:
            self.requestedArms.append(x)
            nonoise = self.func(x)
            value = np.random.normal(loc=nonoise, scale=self.sd, size=1)[0]
            self.outputValues.append(value)
            return value
        except:
            raise ValueError

    # At each call we verify if the number of iterations has passed or not
    def __call__(self, x):
        """
        x can be both a list or tuple
        When we call the function/pass this function as a parameter it will call this
        Here we verify that it hasnt gone over the maximum iterations, as some algorithms ignore that
        """
        try:
            xx = convertToArray(x)
            # Verify maximum number of evaluations
            if self._nfeval > self._maxfevals:
                logger.debug('Max iterations were achieved')
                # raise ValueError("Max iterations allowed is over")
            self._nfeval = 1 + self._nfeval
            return self.eval(xx)
        except:
            raise ValueError

    # From this point we verify all the metrics that we want to investigate
    def GetRegret(self):
        """
        Here we calculate the absolute value of the regret of the optimization process
        Regret =  Best possible value without noise - output values for the iteration 
        """
        # value - min ;value > min always
        return self.outputValues - np.ones(np.size(self.outputValues)) * self.minimumValue

    def GetCumulativeRegretVector(self):
        """
        This is the cumulative regret vector
        """
        regret = self.GetRegret()
        return np.cumsum(regret)

    def GetCumulativeRegretFinal(self):
        """
        This is the cumulative regret at the end of the optimization
        """
        try:
            regret = self.GetRegret()
            cumregret = np.sum(regret)
        except:
            logger.warning('Error calculating cummulative regret: ' + str(self.GetCostFunctionName()))
            cumregret = NAN
            pass
        return cumregret

    def GetEuclideanDistance(self, best_arm):
        """
        In this function we compute the euclidean distances between the best_arm found in the algorithm and 
        the known optimal arms. We return the shortest distance between then
        """
        try:
            dist = []
            for arm in self.optimalArms:
                d = spatial.distance.euclidean(arm, best_arm)
                dist.append(d)
                logger.debug('Best arm: ' + str(best_arm) + ' Optimal arm: ' + str(arm) + ' Distance: ' + str(d))
            smallestdist = np.min(dist)
        except:
            logger.warning('Error calculating euclidean distance for: ' + str(self.GetCostFunctionName()))
            smallestdist = NAN
        return smallestdist

    def GetTrueRewardDifference(self, best_arm):
        """
        
        """
        try:
            reward_diff = np.abs(self.minimumValue - self.func(best_arm))
            logger.debug('Real min: ' + str(self.minimumValue) + ' obtainded value: ' + str(self.func(best_arm)))
            if type(reward_diff) is np.ndarray:
                reward_diff=np.float64(reward_diff)
        except:
            logger.warning('Error calculating reward for: ' + str(self.GetCostFunctionName()))
            reward_diff = NAN

        return reward_diff

    def GetCostFunctionName(self):
        """
        
        """
        return str(self.__class__.__name__)

    def GenerateInfo(self, best_arm, timetocomplete, algorithm_name, success=True):
        """
        In this function we create a dictionary logging all the interesting things we want from this experimental run
        """
        algorithm_name = str(algorithm_name)
        try:
            info = {
                'BestArm': best_arm,
                'NumberFunctionEval': self._nfeval,
                'Algorithm': algorithm_name,
                'CostFunction': self.GetCostFunctionName(),
                'EuclideanDistance': self.GetEuclideanDistance(best_arm),
                'TrueRewardDifference': self.GetTrueRewardDifference(best_arm),
                'CumulativeRegret': self.GetCumulativeRegretFinal(),
                'TimeToComplete': timetocomplete,
                'Continuous': self.functionProperties['Continuous'],
                'Differentiability': self.functionProperties['Differentiability'],
                'Separability': self.functionProperties['Separability'],
                'Scalability': self.functionProperties['Scalability'],
                'Modality': self.functionProperties['Modality'],
                'Ndimensions': self.functionProperties['Ndimensions'],
                'OptimizationSuccessful': success
            }
            logger.info('Results for ' + str(algorithm_name) + ' with cost function ' + str(
                self.GetCostFunctionName()) + ' were succesfully created')
        except Exception as e:
            logger.error(e)
            logger.error('Failed to generate results for ' + str(algorithm_name) + ' with cost function ' + str(
                self.GetCostFunctionName()))
            raise RuntimeError
        return info










