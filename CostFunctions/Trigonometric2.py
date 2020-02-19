"""
Implementation of the Trigonometric2 function

# Created by davidis at 2020-02-19
"""

from CostFunctions import CostFunctions
import numpy as np

__all__ = ['Trigonometric2N2', 'Trigonometric2N6', 'Trigonometric2N10', 'Trigonometric2N20']


class Trigonometric2(CostFunctions):
    """
    Implementation of the Trigonometric2 function from
    M. Jamil and X.-S. S. Yang, “A Literature Survey of Benchmark Functions For Global Optimization Problems,” Int. J. Math. Model. Numer. Optim., vol. 4, no. 2, p. 150, Aug. 2013.
    """
    functionProperties = {
        'minimumValue': 1,
        'optimalArms_SingleDimension': 0.9,
        'searchSpace_SingleDimension': [-100, 500],
        'spaceType_SingleDimension': 'uniform',
        'x0_SingleDimension': np.random.uniform(-100, 500),
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
        value = 1.0 + np.sum(8.0*(np.sin(7.0*(x - 0.9)**2.0)**2.0) +
                             6.0*(np.sin(14.0*(x - 0.9)**2.0)**2.0) + (x - 0.9)**2.0)
        return value


class Trigonometric2N2(Trigonometric2):
    functionProperties = Trigonometric2.functionProperties

    def __init__(self, functionProperties, sd=1, maxfeval=10):
        super().__init__(functionProperties, N=2, sd=sd, maxfeval=maxfeval)


class Trigonometric2N6(Trigonometric2):
    functionProperties = Trigonometric2.functionProperties

    def __init__(self, functionProperties, sd=1, maxfeval=10):
        super().__init__(functionProperties, N=6, sd=sd, maxfeval=maxfeval)


class Trigonometric2N10(Trigonometric2):
    functionProperties = Trigonometric2.functionProperties

    def __init__(self, functionProperties, sd=1, maxfeval=10):
        super().__init__(functionProperties, N=10, sd=sd, maxfeval=maxfeval)


class Trigonometric2N20(Trigonometric2):
    functionProperties = Trigonometric2.functionProperties

    def __init__(self, functionProperties, sd=1, maxfeval=10):
        super().__init__(functionProperties, N=20, sd=sd, maxfeval=maxfeval)