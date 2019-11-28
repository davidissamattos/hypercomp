from CostFunctions import CostFunctions
import numpy as np

__all__ = ['RosenbrockN2','RosenbrockN6','RosenbrockN10','RosenbrockN20']


class Rosenbrock(CostFunctions):
    functionProperties = {
        'minimumValue': 0,
        'optimalArms_SingleDimension': 1,
        'searchSpace_SingleDimension': [-30, 30],
        'spaceType_SingleDimension': 'uniform',
        'x0_SingleDimension': np.random.uniform(-30, 30),
        'Continuous': 'Continuous',
        'Differentiability': 'Differentiable',
        'Separability': 'Non-Separable',
        'Scalability': 'Scalable',
        'Modality': 'Unimodal',
    }

    def __init__(self, functionProperties, N = 3, sd=1, maxfeval=10):
        # First we modify the function properties before we initialize the rest
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
        super().__init__(functionProperties, sd=sd, maxfeval=maxfeval)

    def func(self, x):
        value = 0
        for i in range(1,self.N): #one less
            xi = x[i-1]
            xiPlus1 = x[i]
            value = value + 100 * np.power((xiPlus1 - np.power(xi,2)), 2) + np.power((xi - 1),2)
        return value

class RosenbrockN2(Rosenbrock):
    functionProperties = Rosenbrock.functionProperties

    def __init__(self, functionProperties, sd=1, maxfeval=10):
        super().__init__(functionProperties, N=2, sd=sd, maxfeval=maxfeval)


class RosenbrockN6(Rosenbrock):
    functionProperties = Rosenbrock.functionProperties

    def __init__(self, functionProperties, sd=1, maxfeval=10):
        super().__init__(functionProperties, N=6, sd=sd, maxfeval=maxfeval)

class RosenbrockN10(Rosenbrock):
    functionProperties = Rosenbrock.functionProperties

    def __init__(self, functionProperties, sd=1, maxfeval=10):
        super().__init__(functionProperties, N=10, sd=sd, maxfeval=maxfeval)


class RosenbrockN20(Rosenbrock):
    functionProperties = Rosenbrock.functionProperties

    def __init__(self, functionProperties, sd=1, maxfeval=10):
        super().__init__(functionProperties, N=20, sd=sd, maxfeval=maxfeval)