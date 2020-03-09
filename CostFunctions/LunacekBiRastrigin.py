"""
Implementation of the LunacekBiRastrigin function

# Created by davidis at 2020-02-26
"""

from CostFunctions import CostFunctions
from CostFunctions.BBOBAuxFunctions import *
import numpy as np

__all__ = ['LunacekBiRastriginN2', 'LunacekBiRastriginN6', 'LunacekBiRastriginN10', 'LunacekBiRastriginN20']


class LunacekBiRastrigin(CostFunctions):
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
        self.mu0 = 2.5
        self.Q, self.R = QR(self.N)
        self.xopt = Iplusminus(self.N)*self.mu0/2
        functionProperties['optimalArms'] = [self.xopt]
        super().__init__(functionProperties, sd=sd, maxfeval=maxfeval)

    def func(self, x):
        x=np.array(x)
        xhat = np.multiply(2*np.sign(self.xopt), x)
        z = self.Q.dot(DiagAlpha(100,self.N).dot(self.R.dot(xhat-self.mu0)))
        d=1
        s=1 - 1/(2*np.sqrt(self.N + 20)-8.2)
        mu1 = -np.sqrt((self.mu0**2 -d)/s)
        value = np.minimum(np.sum((xhat-self.mu0)**2), d*self.N + s*np.sum((xhat-mu1)**2)) + \
                10*(self.N -np.sum(np.cos(2*np.pi*z))) + 10**4 * fpen(x)
        return value


class LunacekBiRastriginN2(LunacekBiRastrigin):
    functionPropertes = LunacekBiRastrigin.functionProperties

    def __init__(self, functionProperties, sd=1, maxfeval=10):
        super().__init__(functionProperties, N=2, sd=sd, maxfeval=maxfeval)


class LunacekBiRastriginN6(LunacekBiRastrigin):
    functionProperties = LunacekBiRastrigin.functionProperties

    def __init__(self, functionProperties, sd=1, maxfeval=10):
        super().__init__(functionProperties, N=6, sd=sd, maxfeval=maxfeval)


class LunacekBiRastriginN10(LunacekBiRastrigin):
    functionProperties = LunacekBiRastrigin.functionProperties

    def __init__(self, functionProperties, sd=1, maxfeval=10):
        super().__init__(functionProperties, N=10, sd=sd, maxfeval=maxfeval)


class LunacekBiRastriginN20(LunacekBiRastrigin):
    functionProperties = LunacekBiRastrigin.functionProperties

    def __init__(self, functionProperties, sd=1, maxfeval=10):
        super().__init__(functionProperties, N=20, sd=sd, maxfeval=maxfeval)