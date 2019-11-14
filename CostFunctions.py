import numpy as np
from scipy import spatial
from abc import ABC, abstractmethod


class CostFunctions(ABC):
    def __init__(self, functionProperties, sd=1, maxfevals=10, maximize=False):
        # Saving parameters
        self._maxfevals = maxfevals
        self.sd = sd
        self.functionProperties = functionProperties
        self.maximize = maximize
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
        Mathematical experssion of the function
        x is a python array/numpy
        return: a value
        """
        pass

    def eval(self, x):
        self.requestedArms.append(x)
        nonoise = self.func(x)
        if self.maximize:
            value = np.random.normal(loc=-nonoise, scale=self.sd, size=1)[0]
        else:
            value = np.random.normal(loc=nonoise, scale=self.sd, size=1)[0]
        self.outputValues.append(value)
        return value

    # At each call we verify if the number of iterations has passed or not
    def __call__(self, x):
        """
        When we call the function/pass this function as a parameter it will call this
        Here we verify that it hasnt gone over the maximum iterations, as some algorithms ignore that
        """
        if self._nfeval > self._maxfevals:
            print('Max iterations were achieved')
            # raise ValueError("Max iterations allowed is over")
        self._nfeval = 1 + self._nfeval
        return self.eval(x)

    # From this point we verify all the metrics that we want to investigate
    def GetRegret(self):
        """
        Here we calculate the absolute value of the regret of the optimization process
        Regret =  Best possible value without noise - output values for the iteration 
        """
        if self.maximize:
            # (max - value) ; max > values always
            return np.ones(np.size(self.outputValues)) * (-1 * self.minimumValue) - self.outputValues
        else:
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
        return reward_diff

    def GetCostFunctionName(self):
        """
        
        """
        return self.__class__.__name__

    def GenerateInfo(self, best_arm, timetocomplete, algorithm_name):
        """
        In this function we create a dictionary logging all the interesting things of the 
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
            'Differentiability':  self.functionProperties['Differentiability'],
            'Separability':  self.functionProperties['Separability'],
            'Scalability':  self.functionProperties['Scalability'],
            'Modality':  self.functionProperties['Modality'],
            'Ndimensions':  self.functionProperties['Ndimensions']
        }
        return info


# defining the benchmark functions
class SixHumpCamelBack(CostFunctions):
    functionProperties = {
        'minimumValue': -1.036,
        'optimalArms': [[-0.0898, 0.7126], [0.0898, -0.7126]],
        'searchSpace': [[-5, 5], [-5, 5]],
        'spaceType': ['uniform', 'uniform'],
        'x0': [0, 0],
        'Continuous': 'Continuous',
        'Differentiability': 'Differentiable',
        'Separability':'Non-Separable',
        'Scalability':'Non-Scalable',
        'Modality': 'Multimodal',
        'Ndimensions': 2
    }

    def func(self, x):
        x0 = x[0]
        x1 = x[1]
        value = -1 * (4.0 - 2.1 * (x0 ** 2) + (x0 ** 4) / 3.0) * x0 ** 2 - x0 * x1 - (4 * (x1 ** 2) - 4) * (x1 ** 2)
        return value


class Easom(CostFunctions):
    functionProperties = {
        'minimumValue': -1,
        'optimalArms': [[np.pi, np.pi]],
        'searchSpace': [[-100, 100], [-100, 100]],
        'spaceType': ['uniform', 'uniform'],
        'x0': [0, 0],
        'Continuous': 'Continuous',
        'Differentiability': 'Differentiable',
        'Separability': 'Separable',
        'Scalability': 'Non-Scalable',
        'Modality': 'Multimodal',
        'Ndimensions': 2
    }

    def func(self, x):
        x1 = x[0]
        x2 = x[1]
        value = np.cos(x1) * np.cos(x2) * np.exp(-(x1 - np.pi) ** 2 - (x2 - np.pi) ** 2)
        return value


class Miele(CostFunctions):
    functionProperties = {
        'minimumValue': 0,
        'optimalArms': [[0, 1, 1, 1]],
        'searchSpace': [[-1, 1], [-1, 1], [-1, 1], [-1, 1]],
        'spaceType': ['uniform', 'uniform', 'uniform', 'uniform'],
        'x0': [0, 0, 0, 0],
        'Continuous': 'Continuous',
        'Differentiability': 'Differentiable',
        'Separability': 'Non-Separable',
        'Scalability': 'Non-Scalable',
        'Modality': 'Multimodal',
        'Ndimensions': 4
    }

    def func(self, x):
        x1 = x[0]
        x2 = x[1]
        x3 = x[2]
        x4 = x[3]
        value = -(np.exp(-x1) - x2) ** 4 - 100 * (x2 - x3) ** 6 - (np.tan(x3 - x4)) ** 4 - x1 ** 8
        return value


class Paviani(CostFunctions):
    functionProperties = {
        'minimumValue': -45.778,
        'optimalArms': [[9.351, 9.351, 9.351, 9.351, 9.351, 9.351, 9.351, 9.351, 9.351, 9.351]],
        'searchSpace': [[2.0001, 10],
                        [2.0001, 10],
                        [2.0001, 10],
                        [2.0001, 10],
                        [2.0001, 10],
                        [2.0001, 10],
                        [2.0001, 10],
                        [2.0001, 10],
                        [2.0001, 10],
                        [2.0001, 10]],
        'spaceType': ['uniform',
                      'uniform',
                      'uniform',
                      'uniform',
                      'uniform',
                      'uniform',
                      'uniform',
                      'uniform',
                      'uniform',
                      'uniform'],
        'x0': [6, 6, 6, 6, 6, 6, 6, 6, 6, 6],
        'Continuous': 'Continuous',
        'Differentiability': 'Differentiable',
        'Separability': 'Non-Separable',
        'Scalability': 'Scalable',
        'Modality': 'Multimodal',
        'Ndimensions': 10
    }

    def func(self, x):
        psum = 0
        product = 1
        for xi in x:
            interm = (np.log(xi - 2)) ** 2 + (np.log(10 - xi)) ** 2
            psum = psum + interm
            product = xi * product
        value = -psum + np.power(product, 0.2)
        return value


class Rosenbrock(CostFunctions):
    functionProperties = {
        'minimumValue': 0,
        'optimalArms_SingleDimension': 0,
        'searchSpace_SingleDimension': [-30, 30],
        'spaceType_SingleDimension': 'uniform',
        'x0_SingleDimension': 0,
        'Continuous': 'Continuous',
        'Differentiability': 'Differentiable',
        'Separability': 'Non-Separable',
        'Scalability': 'Scalable',
        'Modality': 'Unimodal',
    }
    def __init__(self, N, functionProperties, sd=1, maxfevals=10, maximize=False):
        #First we modify the function properties before we initialize the rest
        searchSpace = []
        spaceType = []
        x0 = []
        optimalArm = []
        self.N = N
        for i in range(N):
            searchSpace.append(functionProperties['searchSpace_SingleDimension'])
            spaceType.append(functionProperties['spaceType_SingleDimension'])
            x0.append(functionProperties['x0_SingleDimension'])
            optimalArm.append(functionProperties['optimalArms_SingleDimension'])
        functionProperties['optimalArms'] = [optimalArm]
        functionProperties['x0'] = x0
        functionProperties['spaceType'] = spaceType
        functionProperties['searchSpace'] = searchSpace
        functionProperties['Ndimensions'] = N
        super().__init__(functionProperties, sd=sd, maxfevals=maxfevals, maximize=maximize)

    def func(self, x):
        value = 0
        for i in range(self.N-1):
            value = value + 100*(x[i+1] - x[i]**2)**2 + (x[i]-1)**2
        return value


class RosenbrockModified(CostFunctions):
    functionProperties = {
        'minimumValue': 0,
        'optimalArms': [[-1, -1]],
        'searchSpace': [[-2, 2], [-2, 2]],
        'spaceType': ['uniform', 'uniform'],
        'x0': [0, 0],
        'Continuous': 'Continuous',
        'Differentiability': 'Differentiable',
        'Separability': 'Non-Separable',
        'Scalability': 'Non-Scalable',
        'Modality': 'Multimodal',
        'Ndimensions': 2
    }

    def func(self, x):
        x1 = x[0]
        x2 = x[1]
        expvalue = (-1)*((x1+1)**2 +(x2+1)**2)/0.1
        value = 74 + 100*(x2 -x1**2)**2 + (1-x1)**2 - 400*np.exp(expvalue)
        return value


class BraninRCOS(CostFunctions):
    functionProperties = {
        'minimumValue': 0.3978873,
        'optimalArms': [[-np.pi, 12.275], [np.pi, 2.275], [3*np.pi, 2.425]],
        'searchSpace': [[-5, 10], [-0, 15]],
        'spaceType': ['uniform', 'uniform'],
        'x0': [0, 0],
        'Continuous': 'Continuous',
        'Differentiability': 'Differentiable',
        'Separability': 'Non-Separable',
        'Scalability': 'Non-Scalable',
        'Modality': 'Multimodal',
        'Ndimensions': 2
    }

    def func(self, x):
        x1 = x[0]
        x2 = x[1]
        value = (x2 - (5.1*(x1**2))/(4*(np.pi**2)) + (5*x1/np.pi) - 6)**2 + \
                10*(1 - 1/(8*np.pi))*np.cos(x1) + \
                10
        return value

class BraninRCOS2(CostFunctions):
    functionProperties = {
        'minimumValue': 5.559037,
        'optimalArms': [[-3.2, 12.53]],
        'searchSpace': [[-5, 15], [-5, 15]],
        'spaceType': ['uniform', 'uniform'],
        'x0': [0, 0],
        'Continuous': 'Continuous',
        'Differentiability': 'Differentiable',
        'Separability': 'Non-Separable',
        'Scalability': 'Non-Scalable',
        'Modality': 'Multimodal',
        'Ndimensions': 2
    }

    def func(self, x):
        x1 = x[0]
        x2 = x[1]
        value = (x2 - (5.1*(x1**2))/(4*(np.pi**2)) + (5*x1/np.pi) - 6)**2 + \
                10*(1 - 1/(8*np.pi))*np.cos(x1)*np.cos(x2)*np.log(x1**2 + x2**2 +1) + \
                10
        return value