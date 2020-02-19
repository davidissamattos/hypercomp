"""
Implementation of the Quintic.py function

# Created by davidis at 2020-02-13
"""

from CostFunctions import CostFunctions
import numpy as np
from itertools import combinations_with_replacement

__all__ = ['QuinticN2', 'QuinticN6', 'QuinticN10', 'QuinticN20']


class Quintic(CostFunctions):
    """
    Implementation of the Quintic.py function from
    M. Jamil and X.-S. S. Yang, “A Literature Survey of Benchmark Functions For Global Optimization Problems,” Int. J. Math. Model. Numer. Optim., vol. 4, no. 2, p. 150, Aug. 2013.
    """
    functionProperties = {
        'minimumValue': 0,
        'searchSpace_SingleDimension': [-10, 5],
        'spaceType_SingleDimension': 'uniform',
        'x0_SingleDimension': np.random.uniform(-10, 5),
        'Continuous': 'Continuous',
        'Differentiability': 'Differentiable',
        'Separability': 'Separable',
        'Scalability': 'Non-Scalable',
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
        for comb in combinations_with_replacement([-1,2],self.N):
            optimalArm.append(list(comb))
        functionProperties['optimalArms'] = optimalArm
        functionProperties['x0'] = x0
        functionProperties['spaceType'] = spaceType
        functionProperties['searchSpace'] = searchSpace
        functionProperties['Ndimensions'] = self.N
        super().__init__(functionProperties, sd=sd, maxfeval=maxfeval)

    def func(self, x):
        value = np.sum(np.abs(x**5 - 3*x**4 + 4*x**3 + 2*x**2 - 10*x - 4))
        return value


class QuinticN2(Quintic):
    functionProperties = Quintic.functionProperties

    def __init__(self, functionProperties, sd=1, maxfeval=10):
        super().__init__(functionProperties, N=2, sd=sd, maxfeval=maxfeval)


class QuinticN6(Quintic):
    functionProperties = Quintic.functionProperties

    def __init__(self, functionProperties, sd=1, maxfeval=10):
        super().__init__(functionProperties, N=6, sd=sd, maxfeval=maxfeval)


class QuinticN10(Quintic):
    functionProperties = Quintic.functionProperties

    def __init__(self, functionProperties, sd=1, maxfeval=10):
        super().__init__(functionProperties, N=10, sd=sd, maxfeval=maxfeval)


class QuinticN20(Quintic):
    functionProperties = Quintic.functionProperties

    def __init__(self, functionProperties, sd=1, maxfeval=10):
        super().__init__(functionProperties, N=20, sd=sd, maxfeval=maxfeval)