from CostFunctions import CostFunctions
import numpy as np
from CostFunctions.BBOBAuxFunctions import *

__all__ = ['RosenbrockRotatedN2','RosenbrockRotatedN6','RosenbrockRotatedN10','RosenbrockRotatedN20']


class RosenbrockRotated(CostFunctions):
    functionProperties = {
        'minimumValue': 0, #due to the transformation
        'optimalArms_SingleDimension': 1,
        'searchSpace_SingleDimension': [-30, 10],
        'spaceType_SingleDimension': 'uniform',
        'x0_SingleDimension': np.random.uniform(-30, 10),
        'Continuous': 'Continuous',
        'Differentiability': 'Differentiable',
        'Separability': 'Non-Separable',
        'Scalability': 'Scalable',
        'Modality': 'Unimodal',
        'BBOB': 'True'
    }

    def __init__(self, functionProperties, N = 3, sd=1, maxfeval=10):
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

        functionProperties['x0'] = x0
        functionProperties['spaceType'] = spaceType
        functionProperties['searchSpace'] = searchSpace
        functionProperties['Ndimensions'] = N
        self.Q, self.R = QR(self.N)
        xopt = np.linalg.inv(self.R).dot((onesVec(self.N) - onesVec(self.N)/2)/np.maximum(1, np.sqrt(self.N)/8))
        functionProperties['optimalArms'] = [xopt]
        super().__init__(functionProperties, sd=sd, maxfeval=maxfeval)

    def func(self, x):
        value = 0
        z = np.maximum(1, np.sqrt(self.N)/8)*self.R.dot(x) + onesVec(self.N)/2
        for i in range(1, self.N):  # one less
            zi = z[i - 1]
            ziPlus1 = z[i]
            value = value + 100 * np.power((ziPlus1 - np.power(zi, 2)), 2) + np.power((zi - 1), 2)
        return value

class RosenbrockRotatedN2(RosenbrockRotated):
    functionProperties = RosenbrockRotated.functionProperties

    def __init__(self, functionProperties, sd=1, maxfeval=10):
        super().__init__(functionProperties, N=2, sd=sd, maxfeval=maxfeval)


class RosenbrockRotatedN6(RosenbrockRotated):
    functionProperties = RosenbrockRotated.functionProperties

    def __init__(self, functionProperties, sd=1, maxfeval=10):
        super().__init__(functionProperties, N=6, sd=sd, maxfeval=maxfeval)

class RosenbrockRotatedN10(RosenbrockRotated):
    functionProperties = RosenbrockRotated.functionProperties

    def __init__(self, functionProperties, sd=1, maxfeval=10):
        super().__init__(functionProperties, N=10, sd=sd, maxfeval=maxfeval)


class RosenbrockRotatedN20(RosenbrockRotated):
    functionProperties = RosenbrockRotated.functionProperties

    def __init__(self, functionProperties, sd=1, maxfeval=10):
        super().__init__(functionProperties, N=20, sd=sd, maxfeval=maxfeval)