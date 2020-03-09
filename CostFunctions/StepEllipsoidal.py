"""
Implementation of the StepEllipsoidal function

# Created by davidis at 2020-02-26
"""

from CostFunctions import CostFunctions
from CostFunctions.BBOBAuxFunctions import *
import numpy as np

__all__ = ['StepEllipsoidalN2', 'StepEllipsoidalN6', 'StepEllipsoidalN10', 'StepEllipsoidalN20']


class StepEllipsoidal(CostFunctions):
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
        x = np.array(x)
        Q, R = QR(self.N)
        Gamma = DiagAlpha(10,self.N)
        zhat =Gamma.dot(R.dot(x))
        ztil = np.zeros(self.N)
        j=0
        for _ in zhat:
            if np.abs(zhat[j]) > 0.5:
                ztil[j] = np.floor(0.5+zhat[j])
            else:
                ztil[j] = np.floor(0.5+10*zhat[j])/10
            j=j+1
        z = Q.dot(ztil)
        i = np.arange(1,self.N+1)
        value = 0.1*np.maximum(np.abs(zhat[0])/(10**4), np.sum(np.power(10, 2*(i-1)/(self.N-1))* z**2)) + fpen(x)
        return value


class StepEllipsoidalN2(StepEllipsoidal):
    functionProperties = StepEllipsoidal.functionProperties

    def __init__(self, functionProperties, sd=1, maxfeval=10):
        super().__init__(functionProperties, N=2, sd=sd, maxfeval=maxfeval)


class StepEllipsoidalN6(StepEllipsoidal):
    functionProperties = StepEllipsoidal.functionProperties

    def __init__(self, functionProperties, sd=1, maxfeval=10):
        super().__init__(functionProperties, N=6, sd=sd, maxfeval=maxfeval)


class StepEllipsoidalN10(StepEllipsoidal):
    functionProperties = StepEllipsoidal.functionProperties

    def __init__(self, functionProperties, sd=1, maxfeval=10):
        super().__init__(functionProperties, N=10, sd=sd, maxfeval=maxfeval)


class StepEllipsoidalN20(StepEllipsoidal):
    functionProperties = StepEllipsoidal.functionProperties

    def __init__(self, functionProperties, sd=1, maxfeval=10):
        super().__init__(functionProperties, N=20, sd=sd, maxfeval=maxfeval)