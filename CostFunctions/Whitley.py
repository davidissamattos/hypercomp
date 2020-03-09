"""
Implementation of the Whitley function

# Created by davidis at 2020-02-24
"""

from CostFunctions import CostFunctions
import numpy as np

__all__ = ['WhitleyN2', 'WhitleyN6', 'WhitleyN10', 'WhitleyN20']


class Whitley(CostFunctions):
    """
    Implementation of the Whitley function from
    M. Jamil and X.-S. S. Yang, “A Literature Survey of Benchmark Functions For Global Optimization Problems,” Int. J. Math. Model. Numer. Optim., vol. 4, no. 2, p. 150, Aug. 2013.
    """
    functionProperties = {
        'minimumValue': 0,
        'optimalArms_SingleDimension': 1,
        'searchSpace_SingleDimension': [-10, 3],
        'spaceType_SingleDimension': 'uniform',
        'x0_SingleDimension': np.random.uniform(-10, 3),
        'Continuous': 'Continuous',
        'Differentiability': 'Differentiable',
        'Separability': 'Non-Separable',
        'Scalability': 'Scalable',
        'Modality': 'Multimodal',
    }

    def __init__(self, functionProperties, N=10, sd=1, maxfeval=10):
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
        functionProperties['Ndimensions'] = self.N
        super().__init__(functionProperties, sd=sd, maxfeval=maxfeval)

    def func(self, x):
        value = 0.0
        for i in range(self.N):
            for j in range(self.N):
                temp = 100.0 * ((x[i] ** 2.0) - x[j]) + (1.0 - x[j]) ** 2.0
                value += (float(temp ** 2.0) / 4000.0) - np.cos(temp) + 1.0
        return value



class WhitleyN2(Whitley):
    functionProperties = Whitley.functionProperties

    def __init__(self, functionProperties, sd=1, maxfeval=10):
        super().__init__(functionProperties, N=2, sd=sd, maxfeval=maxfeval)


class WhitleyN6(Whitley):
    functionProperties = Whitley.functionProperties

    def __init__(self, functionProperties, sd=1, maxfeval=10):
        super().__init__(functionProperties, N=6, sd=sd, maxfeval=maxfeval)


class WhitleyN10(Whitley):
    functionProperties = Whitley.functionProperties

    def __init__(self, functionProperties, sd=1, maxfeval=10):
        super().__init__(functionProperties, N=10, sd=sd, maxfeval=maxfeval)


class WhitleyN20(Whitley):
    functionProperties = Whitley.functionProperties

    def __init__(self, functionProperties, sd=1, maxfeval=10):
        super().__init__(functionProperties, N=20, sd=sd, maxfeval=maxfeval)