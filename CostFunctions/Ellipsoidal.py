"""
Implementation of the Ellipsoidal function

# Created by davidis at 2020-02-26
"""

from CostFunctions import CostFunctions
from CostFunctions.BBOBAuxFunctions import *
import numpy as np

__all__ = ['EllipsoidalN2', 'EllipsoidalN6', 'EllipsoidalN10', 'EllipsoidalN20']


class Ellipsoidal(CostFunctions):
    """
   From BBOB
    """
    functionProperties = {
        'minimumValue': 0,
        'optimalArms_SingleDimension': 0,
        'searchSpace_SingleDimension': [-10, 5],
        'spaceType_SingleDimension': 'uniform',
        'x0_SingleDimension': np.random.uniform(-10, 5),
        'Continuous': 'Continuous',
        'Differentiability': 'Differentiable',
        'Separability': 'Non-Separable',
        'Scalability': 'Scalable',
        'Modality': 'Multimodal',
        'BBOB': 'True'
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
        i = np.arange(1, self.N+1)
        x = np.array(x)
        z = Tosz(x)
        value = np.sum(np.power(10**6,(i-1)/(self.N-1))* z**2)
        return value


class EllipsoidalN2(Ellipsoidal):
    functionProperties = Ellipsoidal.functionProperties

    def __init__(self, functionProperties, sd=1, maxfeval=10):
        super().__init__(functionProperties, N=2, sd=sd, maxfeval=maxfeval)


class EllipsoidalN6(Ellipsoidal):
    functionProperties = Ellipsoidal.functionProperties

    def __init__(self, functionProperties, sd=1, maxfeval=10):
        super().__init__(functionProperties, N=6, sd=sd, maxfeval=maxfeval)


class EllipsoidalN10(Ellipsoidal):
    functionProperties = Ellipsoidal.functionProperties

    def __init__(self, functionProperties, sd=1, maxfeval=10):
        super().__init__(functionProperties, N=10, sd=sd, maxfeval=maxfeval)


class EllipsoidalN20(Ellipsoidal):
    functionProperties = Ellipsoidal.functionProperties

    def __init__(self, functionProperties, sd=1, maxfeval=10):
        super().__init__(functionProperties, N=20, sd=sd, maxfeval=maxfeval)