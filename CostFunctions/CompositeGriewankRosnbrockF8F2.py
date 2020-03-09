"""
Implementation of the CompositeGriewankRosnbrockF8F2 function

# Created by davidis at 2020-02-26
"""

from CostFunctions import CostFunctions
from CostFunctions.BBOBAuxFunctions import *
import numpy as np

__all__ = ['CompositeGriewankRosnbrockF8F2N2', 'CompositeGriewankRosnbrockF8F2N6', 'CompositeGriewankRosnbrockF8F2N10', 'CompositeGriewankRosnbrockF8F2N20']


class CompositeGriewankRosnbrockF8F2(CostFunctions):
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
        functionProperties['x0'] = x0
        functionProperties['spaceType'] = spaceType
        functionProperties['searchSpace'] = searchSpace
        functionProperties['Ndimensions'] = self.N
        self.Q, self.R = QR(self.N)
        xopt = np.linalg.inv(self.R).dot((onesVec(self.N) - 0.5) / np.maximum(1, np.sqrt(self.N) / 8))
        functionProperties['optimalArms'] = [xopt]
        super().__init__(functionProperties, sd=sd, maxfeval=maxfeval)

    def func(self, x):
        x=np.array(x)
        z = np.maximum(1,np.sqrt(self.N)/8)*self.R.dot(x) +0.5
        z1N = z[:-1]
        z2N = z[1:]
        s = 100*(z1N**2 - z2N)**2 + (z1N-1)**2
        value =(10/(self.N-1) )* np.sum(s/4000 - np.cos(s)) + 10
        return value


class CompositeGriewankRosnbrockF8F2N2(CompositeGriewankRosnbrockF8F2):
    functionPropertes = CompositeGriewankRosnbrockF8F2.functionProperties

    def __init__(self, functionProperties, sd=1, maxfeval=10):
        super().__init__(functionProperties, N=2, sd=sd, maxfeval=maxfeval)


class CompositeGriewankRosnbrockF8F2N6(CompositeGriewankRosnbrockF8F2):
    functionProperties = CompositeGriewankRosnbrockF8F2.functionProperties

    def __init__(self, functionProperties, sd=1, maxfeval=10):
        super().__init__(functionProperties, N=6, sd=sd, maxfeval=maxfeval)


class CompositeGriewankRosnbrockF8F2N10(CompositeGriewankRosnbrockF8F2):
    functionProperties = CompositeGriewankRosnbrockF8F2.functionProperties

    def __init__(self, functionProperties, sd=1, maxfeval=10):
        super().__init__(functionProperties, N=10, sd=sd, maxfeval=maxfeval)


class CompositeGriewankRosnbrockF8F2N20(CompositeGriewankRosnbrockF8F2):
    functionProperties = CompositeGriewankRosnbrockF8F2.functionProperties

    def __init__(self, functionProperties, sd=1, maxfeval=10):
        super().__init__(functionProperties, N=20, sd=sd, maxfeval=maxfeval)