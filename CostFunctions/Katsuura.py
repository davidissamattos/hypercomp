"""
Implementation of the Katsuura function

# Created by davidis at 2020-02-26
"""

from CostFunctions import CostFunctions
from CostFunctions.BBOBAuxFunctions import *
import numpy as np

__all__ = ['KatsuuraN2', 'KatsuuraN6', 'KatsuuraN10', 'KatsuuraN20']


class Katsuura(CostFunctions):
    """
    BBOB
    """
    functionProperties = {
        'minimumValue': 1,
        'optimalArms_SingleDimension': 0,
        'searchSpace_SingleDimension': [-5, 10],
        'spaceType_SingleDimension': 'uniform',
        'x0_SingleDimension': np.random.uniform(-5, 10),
        'Continuous': 'Continuous',
        'Differentiability': 'Differentiable',
        'Separability': 'Non-Separable',
        'Scalability': 'Scalable',
        'Modality': 'Multimodal',
        'BBOB': 'True',
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
        self.Q, self.R = QR(self.N)
        super().__init__(functionProperties, sd=sd, maxfeval=maxfeval)

    def func(self, x):
        x=np.array(x)
        z = self.Q.dot(DiagAlpha(100,self.N).dot(self.R.dot(x)))

        j = np.arange(1, 33)
        ii=0
        i = 1
        s=np.zeros(self.N)
        for zi in z:
            s[ii] = np.sum(np.abs(zi* 2**j - np.abs(zi* 2**j))/(2**j))
            ii = ii +1
        i = np.arange(1,self.N+1)
        value = (10/self.N**2)* np.prod((1+i*s)**(10/(self.N**1.2))) - (10/self.N**2) +fpen(x) + 1

        return value


class KatsuuraN2(Katsuura):
    functionPropertes = Katsuura.functionProperties

    def __init__(self, functionProperties, sd=1, maxfeval=10):
        super().__init__(functionProperties, N=2, sd=sd, maxfeval=maxfeval)


class KatsuuraN6(Katsuura):
    functionProperties = Katsuura.functionProperties

    def __init__(self, functionProperties, sd=1, maxfeval=10):
        super().__init__(functionProperties, N=6, sd=sd, maxfeval=maxfeval)


class KatsuuraN10(Katsuura):
    functionProperties = Katsuura.functionProperties

    def __init__(self, functionProperties, sd=1, maxfeval=10):
        super().__init__(functionProperties, N=10, sd=sd, maxfeval=maxfeval)


class KatsuuraN20(Katsuura):
    functionProperties = Katsuura.functionProperties

    def __init__(self, functionProperties, sd=1, maxfeval=10):
        super().__init__(functionProperties, N=20, sd=sd, maxfeval=maxfeval)