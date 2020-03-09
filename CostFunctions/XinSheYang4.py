"""
Implementation of the XinSheYang4 function

# Created by davidis at 2020-02-26
"""

from CostFunctions import CostFunctions
import numpy as np

__all__ = ['XinSheYang4N2', 'XinSheYang4N6', 'XinSheYang4N10', 'XinSheYang4N20']


class XinSheYang4(CostFunctions):
    """
    Implementation of the XinSheYang4 function from
    M. Jamil and X.-S. S. Yang, “A Literature Survey of Benchmark Functions For Global Optimization Problems,” Int. J. Math. Model. Numer. Optim., vol. 4, no. 2, p. 150, Aug. 2013.
    """
    functionProperties = {
        'minimumValue': -1,
        'optimalArms_SingleDimension': 0,
        'searchSpace_SingleDimension': [-10, 5],
        'spaceType_SingleDimension': 'uniform',
        'x0_SingleDimension': np.random.uniform(-10, 5),
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
        value = (np.sum(np.sin(x)**2.0) - np.exp(-np.sum(x**2.0)))*np.exp(-np.sum(np.sin(np.sqrt(np.abs(x)))**2.0))
        return value


class XinSheYang4N2(XinSheYang4):
    functionProperties = XinSheYang4.functionProperties

    def __init__(self, functionProperties, sd=1, maxfeval=10):
        super().__init__(functionProperties, N=2, sd=sd, maxfeval=maxfeval)


class XinSheYang4N6(XinSheYang4):
    functionProperties = XinSheYang4.functionProperties

    def __init__(self, functionProperties, sd=1, maxfeval=10):
        super().__init__(functionProperties, N=6, sd=sd, maxfeval=maxfeval)


class XinSheYang4N10(XinSheYang4):
    functionProperties = XinSheYang4.functionProperties

    def __init__(self, functionProperties, sd=1, maxfeval=10):
        super().__init__(functionProperties, N=10, sd=sd, maxfeval=maxfeval)


class XinSheYang4N20(XinSheYang4):
    functionProperties = XinSheYang4.functionProperties

    def __init__(self, functionProperties, sd=1, maxfeval=10):
        super().__init__(functionProperties, N=20, sd=sd, maxfeval=maxfeval)