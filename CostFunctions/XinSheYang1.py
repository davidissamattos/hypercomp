"""
Implementation of the XinSheYang1 function

# Created by davidis at 2020-02-24
"""

from CostFunctions import CostFunctions
import numpy as np

__all__ = ['XinSheYang1N2', 'XinSheYang1N6', 'XinSheYang1N10', 'XinSheYang1N20']


class XinSheYang1(CostFunctions):
    """
    Implementation of the XinSheYang1 function from
    M. Jamil and X.-S. S. Yang, “A Literature Survey of Benchmark Functions For Global Optimization Problems,” Int. J. Math. Model. Numer. Optim., vol. 4, no. 2, p. 150, Aug. 2013.
    """
    functionProperties = {
        'minimumValue': 0,
        'optimalArms_SingleDimension': 0,
        'searchSpace_SingleDimension': [-10, 15],
        'spaceType_SingleDimension': 'uniform',
        'x0_SingleDimension': np.random.uniform(-10, 5),
        'Continuous': 'Continuous',
        'Differentiability': 'NonDifferentiable',
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
        epsilon = np.random.uniform(0.0, 1.0, size=self.N)

        rng = np.arange(1.0, self.N + 1.0)
        value = np.sum(epsilon * (np.abs(x) ** rng))
        return value

class XinSheYang1N2(XinSheYang1):
    functionProperties = XinSheYang1.functionProperties

    def __init__(self, functionProperties, sd=1, maxfeval=10):
        super().__init__(functionProperties, N=2, sd=sd, maxfeval=maxfeval)


class XinSheYang1N6(XinSheYang1):
    functionProperties = XinSheYang1.functionProperties

    def __init__(self, functionProperties, sd=1, maxfeval=10):
        super().__init__(functionProperties, N=6, sd=sd, maxfeval=maxfeval)


class XinSheYang1N10(XinSheYang1):
    functionProperties = XinSheYang1.functionProperties

    def __init__(self, functionProperties, sd=1, maxfeval=10):
        super().__init__(functionProperties, N=10, sd=sd, maxfeval=maxfeval)


class XinSheYang1N20(XinSheYang1):
    functionProperties = XinSheYang1.functionProperties

    def __init__(self, functionProperties, sd=1, maxfeval=10):
        super().__init__(functionProperties, N=20, sd=sd, maxfeval=maxfeval)