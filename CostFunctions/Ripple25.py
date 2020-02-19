"""
Implementation of the Ripple25.py function

# Created by davidis at 2020-01-22
"""

from CostFunctions import CostFunctions
import numpy as np

__all__ = ['Ripple25N2', 'Ripple25N6', 'Ripple25N10', 'Ripple25N20']


class Ripple25(CostFunctions):
    """
    Implementation of the Ripple1.py function from
    M. Jamil and X.-S. S. Yang, “A Literature Survey of Benchmark Functions For Global Optimization Problems,” Int. J. Math. Model. Numer. Optim., vol. 4, no. 2, p. 150, Aug. 2013.
    """
    functionProperties = {
        'minimumValue':  -2.0,
        'optimalArms_SingleDimension': 0.1,
        'searchSpace_SingleDimension': [0, 1],
        'spaceType_SingleDimension': 'uniform',
        'x0_SingleDimension': np.random.uniform(0, 1),
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
        u = -2.0 * np.log(2.0) * ((x - 0.1) / 0.8) ** 2.0
        v = np.sin(5.0 * np.pi * x) ** 6.0
        return np.sum(-np.exp(u) * v)


class Ripple25N2(Ripple25):
    functionProperties = Ripple25.functionProperties

    def __init__(self, functionProperties, sd=1, maxfeval=10):
        super().__init__(functionProperties, N=2, sd=sd, maxfeval=maxfeval)


class Ripple25N6(Ripple25):
    functionProperties = Ripple25.functionProperties

    def __init__(self, functionProperties, sd=1, maxfeval=10):
        super().__init__(functionProperties, N=6, sd=sd, maxfeval=maxfeval)


class Ripple25N10(Ripple25):
    functionProperties = Ripple25.functionProperties

    def __init__(self, functionProperties, sd=1, maxfeval=10):
        super().__init__(functionProperties, N=10, sd=sd, maxfeval=maxfeval)


class Ripple25N20(Ripple25):
    functionProperties = Ripple25.functionProperties

    def __init__(self, functionProperties, sd=1, maxfeval=10):
        super().__init__(functionProperties, N=20, sd=sd, maxfeval=maxfeval)