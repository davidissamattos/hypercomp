"""
Implementation of the Schwefel2d26 function

# Created by davidis at 2020-02-14
"""

from CostFunctions import CostFunctions
import numpy as np
from itertools import combinations_with_replacement

__all__ = ['Schwefel2d26N2', 'Schwefel2d26N6', 'Schwefel2d26N10', 'Schwefel2d26N20']


class Schwefel2d26(CostFunctions):
    """
    Implementation of the Schwefel2d26 function from
    M. Jamil and X.-S. S. Yang, “A Literature Survey of Benchmark Functions For Global Optimization Problems,” Int. J. Math. Model. Numer. Optim., vol. 4, no. 2, p. 150, Aug. 2013.
    https://www.sfu.ca/~ssurjano/schwef.html

    """
    functionProperties = {
        'minimumValue': 0,
        'optimalArms_SingleDimension': 420.968746,
        'searchSpace_SingleDimension': [-500, 500],
        'spaceType_SingleDimension': 'uniform',
        'x0_SingleDimension': np.random.uniform(-500, 500),
        'Continuous': 'Continuous',
        'Differentiability': 'Differentiable',
        'Separability': 'Separable',
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
        value = (418.982887*self.N) - np.sum(x*np.sin(np.sqrt(np.abs(x))))
        return value


class Schwefel2d26N2(Schwefel2d26):
    functionProperties = Schwefel2d26.functionProperties

    def __init__(self, functionProperties, sd=1, maxfeval=10):
        super().__init__(functionProperties, N=2, sd=sd, maxfeval=maxfeval)


class Schwefel2d26N6(Schwefel2d26):
    functionProperties = Schwefel2d26.functionProperties

    def __init__(self, functionProperties, sd=1, maxfeval=10):
        super().__init__(functionProperties, N=6, sd=sd, maxfeval=maxfeval)


class Schwefel2d26N10(Schwefel2d26):
    functionProperties = Schwefel2d26.functionProperties

    def __init__(self, functionProperties, sd=1, maxfeval=10):
        super().__init__(functionProperties, N=10, sd=sd, maxfeval=maxfeval)


class Schwefel2d26N20(Schwefel2d26):
    functionProperties = Schwefel2d26.functionProperties

    def __init__(self, functionProperties, sd=1, maxfeval=10):
        super().__init__(functionProperties, N=20, sd=sd, maxfeval=maxfeval)