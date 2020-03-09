"""
Implementation of the XinSheYang3 function

# Created by davidis at 2020-02-26
"""

from CostFunctions import CostFunctions
import numpy as np

__all__ = ['XinSheYang3N2', 'XinSheYang3N6', 'XinSheYang3N10', 'XinSheYang3N20']


class XinSheYang3(CostFunctions):
    """
    Implementation of the XinSheYang3 function from
    M. Jamil and X.-S. S. Yang, “A Literature Survey of Benchmark Functions For Global Optimization Problems,” Int. J. Math. Model. Numer. Optim., vol. 4, no. 2, p. 150, Aug. 2013.
    """
    functionProperties = {
        'minimumValue': -1,
        'optimalArms_SingleDimension': 0,
        'searchSpace_SingleDimension': [-5, 20],
        'spaceType_SingleDimension': 'uniform',
        'x0_SingleDimension': np.random.uniform(-5, 20),
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
        beta = 15.0
        m = 5.0
        value = np.exp(-np.sum((x/beta)**(2*m))) - 2.0*np.exp(-np.sum(x**2.0))*np.prod(np.cos(x)**2.0)
        return value

class XinSheYang3N2(XinSheYang3):
    functionProperties = XinSheYang3.functionProperties

    def __init__(self, functionProperties, sd=1, maxfeval=10):
        super().__init__(functionProperties, N=2, sd=sd, maxfeval=maxfeval)


class XinSheYang3N6(XinSheYang3):
    functionProperties = XinSheYang3.functionProperties

    def __init__(self, functionProperties, sd=1, maxfeval=10):
        super().__init__(functionProperties, N=6, sd=sd, maxfeval=maxfeval)


class XinSheYang3N10(XinSheYang3):
    functionProperties = XinSheYang3.functionProperties

    def __init__(self, functionProperties, sd=1, maxfeval=10):
        super().__init__(functionProperties, N=10, sd=sd, maxfeval=maxfeval)


class XinSheYang3N20(XinSheYang3):
    functionProperties = XinSheYang3.functionProperties

    def __init__(self, functionProperties, sd=1, maxfeval=10):
        super().__init__(functionProperties, N=20, sd=sd, maxfeval=maxfeval)