"""
Implementation of the LinearSlope function

# Created by davidis at 2020-02-27
"""

from CostFunctions import CostFunctions
import numpy as np
from CostFunctions.BBOBAuxFunctions import *

__all__ = ['LinearSlopeN2', 'LinearSlopeN6', 'LinearSlopeN10', 'LinearSlopeN20']


class LinearSlope(CostFunctions):
    """
    Implementation of the LinearSlope function from
    M. Jamil and X.-S. S. Yang, “A Literature Survey of Benchmark Functions For Global Optimization Problems,” Int. J. Math. Model. Numer. Optim., vol. 4, no. 2, p. 150, Aug. 2013.
    """
    functionProperties = {
        'minimumValue': 0.0,
        'optimalArms_SingleDimension': 5,
        'searchSpace_SingleDimension': [-5, 5],
        'spaceType_SingleDimension': 'uniform',
        'x0_SingleDimension': np.random.uniform(-5, 5),
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
        x=np.array(x)
        xopt =  self.functionProperties['optimalArms'][0]
        z = np.zeros(self.N)
        s = np.zeros(self.N)
        i=1
        j=0
        for xi in x:
            if xi*xopt[j]<25:
                z[j]= xi
            else:
                z[j]=xopt[j]
            s[j]=np.sign(xopt[j])*np.power(10, (i-1)/(self.N-1))
        value = np.sum(5*np.abs(s) - s*z)
        return value


class LinearSlopeN2(LinearSlope):
    functionProperties = LinearSlope.functionProperties

    def __init__(self, functionProperties, sd=1, maxfeval=10):
        super().__init__(functionProperties, N=2, sd=sd, maxfeval=maxfeval)


class LinearSlopeN6(LinearSlope):
    functionProperties = LinearSlope.functionProperties

    def __init__(self, functionProperties, sd=1, maxfeval=10):
        super().__init__(functionProperties, N=6, sd=sd, maxfeval=maxfeval)


class LinearSlopeN10(LinearSlope):
    functionProperties = LinearSlope.functionProperties

    def __init__(self, functionProperties, sd=1, maxfeval=10):
        super().__init__(functionProperties, N=10, sd=sd, maxfeval=maxfeval)


class LinearSlopeN20(LinearSlope):
    functionProperties = LinearSlope.functionProperties

    def __init__(self, functionProperties, sd=1, maxfeval=10):
        super().__init__(functionProperties, N=20, sd=sd, maxfeval=maxfeval)