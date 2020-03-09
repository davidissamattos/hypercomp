"""
Implementation of the AttractiveSector function

# Created by davidis at 2020-02-26
"""

from CostFunctions import CostFunctions
from CostFunctions.BBOBAuxFunctions import *
import numpy as np

__all__ = ['AttractiveSectorN2', 'AttractiveSectorN6', 'AttractiveSectorN10', 'AttractiveSectorN20']


class AttractiveSector(CostFunctions):
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
        z =Q.dot(Gamma.dot(R.dot(x)))
        j = 0
        s=np.zeros(self.N)

        for xi in x:
            if z[j] * x[j] < 0:
                s[j] = 100
            else:
                s[j] = 1
            j=j+1
        value = (Tosz(np.sum((s*z)**2)))**0.9
        return value


class AttractiveSectorN2(AttractiveSector):
    functionProperties = AttractiveSector.functionProperties

    def __init__(self, functionProperties, sd=1, maxfeval=10):
        super().__init__(functionProperties, N=2, sd=sd, maxfeval=maxfeval)


class AttractiveSectorN6(AttractiveSector):
    functionProperties = AttractiveSector.functionProperties

    def __init__(self, functionProperties, sd=1, maxfeval=10):
        super().__init__(functionProperties, N=6, sd=sd, maxfeval=maxfeval)


class AttractiveSectorN10(AttractiveSector):
    functionProperties = AttractiveSector.functionProperties

    def __init__(self, functionProperties, sd=1, maxfeval=10):
        super().__init__(functionProperties, N=10, sd=sd, maxfeval=maxfeval)


class AttractiveSectorN20(AttractiveSector):
    functionProperties = AttractiveSector.functionProperties

    def __init__(self, functionProperties, sd=1, maxfeval=10):
        super().__init__(functionProperties, N=20, sd=sd, maxfeval=maxfeval)