import numpy as np
from scipy import spatial
from abc import ABC, abstractmethod
from utils import *
import copy
from ConfigSpace.configuration_space import Configuration

__all__ = ['CostFunctions']


class CostFunctions(ABC):
    def __init__(self, functionProperties, sd=1, maxfeval=10, tol=0.001):
        # print('Cost function instantiated')
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
        self.requestedArms.append(x)
        nonoise = self.func(x)
        value = np.random.normal(loc=nonoise, scale=self.sd, size=1)[0]
        self.outputValues.append(value)
        # print('x: ', x, ' value ', value)
        return value

    # At each call we verify if the number of iterations has passed or not
    def __call__(self, x):
        """
        x can be both a list or tuple
        When we call the function/pass this function as a parameter it will call this
        Here we verify that it hasnt gone over the maximum iterations, as some algorithms ignore that
        """
        xx = convertToArray(x)

        # Verify maximum number of evaluations
        if self._nfeval > self._maxfevals:
            print('Max iterations were achieved')
            # raise ValueError("Max iterations allowed is over")
        self._nfeval = 1 + self._nfeval
        # print('nfeval: ', self._nfeval)
        return self.eval(xx)

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
        regret = self.GetRegret()
        return np.sum(regret)

    def GetEuclideanDistance(self, best_arm):
        """
        In this function we compute the euclidean distances between the best_arm found in the algorithm and 
        the known optimal arms. We return the shortest distance between then
        """
        dist = []
        for arm in self.optimalArms:
            d = spatial.distance.euclidean(arm, best_arm)
            dist.append(d)
            # print('Best arm: ', best_arm, ' Optimal arm: ', arm, ' Distance: ', d)
        smallestdist = np.min(dist)
        return smallestdist

    def GetTrueRewardDifference(self, best_arm):
        """
        
        """
        reward_diff = abs(self.minimumValue - self.func(best_arm))
        # print('real min: ',self.minimumValue, ' obtainded value: ', self.func(best_arm))
        return reward_diff

    def GetCostFunctionName(self):
        """
        
        """
        return self.__class__.__name__

    def GenerateInfo(self, best_arm, timetocomplete, algorithm_name):
        """
        In this function we create a dictionary logging all the interesting things we want from this experimental run
        """
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
            'Ndimensions': self.functionProperties['Ndimensions']
        }
        return info










