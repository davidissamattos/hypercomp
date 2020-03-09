"""
Implementation of the SchaffersF7 function

# Created by davidis at 2020-02-26
"""

from CostFunctions import CostFunctions
from CostFunctions.BBOBAuxFunctions import *
import numpy as np

__all__ = ['SchaffersF7N2', 'SchaffersF7N6', 'SchaffersF7N10', 'SchaffersF7N20']


class SchaffersF7(CostFunctions):
    """
    BBOB
    """
    functionProperties = {
        'minimumValue': 0,
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
        z= DiagAlpha(alpha=10,D=self.N).dot(self.Q.dot(Tasy(x,0.5).dot(self.R.dot(x))))
        z1N = z[0:-1]
        z2N = z[1:]
        s= np.sqrt(z1N**2 + z2N**2)
        value = 1/(self.N-1) * np.sum(np.sqrt(s)+np.sqrt(s)*(np.sin(50*s**0.2))**2) + 10*fpen(x)
        return value


class SchaffersF7N2(SchaffersF7):
    functionPropertes = SchaffersF7.functionProperties

    def __init__(self, functionProperties, sd=1, maxfeval=10):
        super().__init__(functionProperties, N=2, sd=sd, maxfeval=maxfeval)


class SchaffersF7N6(SchaffersF7):
    functionProperties = SchaffersF7.functionProperties

    def __init__(self, functionProperties, sd=1, maxfeval=10):
        super().__init__(functionProperties, N=6, sd=sd, maxfeval=maxfeval)


class SchaffersF7N10(SchaffersF7):
    functionProperties = SchaffersF7.functionProperties

    def __init__(self, functionProperties, sd=1, maxfeval=10):
        super().__init__(functionProperties, N=10, sd=sd, maxfeval=maxfeval)


class SchaffersF7N20(SchaffersF7):
    functionProperties = SchaffersF7.functionProperties

    def __init__(self, functionProperties, sd=1, maxfeval=10):
        super().__init__(functionProperties, N=20, sd=sd, maxfeval=maxfeval)