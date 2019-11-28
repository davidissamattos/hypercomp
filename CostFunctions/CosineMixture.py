"""
Implementation of the CosineMixture.py function

# Created by davidis at 2019-11-22
"""

from CostFunctions import CostFunctions
import numpy as np

__all__ = ['CosineMixtureN2', 'CosineMixtureN6', 'CosineMixtureN10', 'CosineMixtureN20']


class CosineMixture(CostFunctions):
    """
    Implementation of the CosineMixture.py function from
    M. Jamil and X.-S. S. Yang, “A Literature Survey of Benchmark Functions For Global Optimization Problems,” Int. J. Math. Model. Numer. Optim., vol. 4, no. 2, p. 150, Aug. 2013.
    https://al-roomi.org/benchmarks/unconstrained/n-dimensions/166-cosine-mixture-function
    """
    functionProperties = {
        'minimumValue': 0.1,
        'optimalArms_SingleDimension': 0,
        'searchSpace_SingleDimension': [-1, 1],
        'spaceType_SingleDimension': 'uniform',
        'x0_SingleDimension': np.random.uniform(-1, 1),
        'Continuous': 'Discontinuous',
        'Differentiability': 'Non-Differentiable',
        'Separability': 'Separable',
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
        functionProperties['minimumValue']= -0.1*self.N,
        functionProperties['optimalArms'] = [optimalArm]
        functionProperties['x0'] = x0
        functionProperties['spaceType'] = spaceType
        functionProperties['searchSpace'] = searchSpace
        functionProperties['Ndimensions'] = self.N
        super().__init__(functionProperties, sd=sd, maxfeval=maxfeval)

    def func(self, x):
        x = np.array(x)
        f1 = 0
        f2 = 0
        for i in range(self.N):
            f1 = f1 + np.cos(5*np.pi*x[i])
            f2 = f2 + np.power(x[i],2)
        value = f2 - 0.1*f1
        return value


class CosineMixtureN2(CosineMixture):
    functionProperties = CosineMixture.functionProperties

    def __init__(self, functionProperties, sd=1, maxfeval=10):
        super().__init__(functionProperties, N=2, sd=sd, maxfeval=maxfeval)


class CosineMixtureN6(CosineMixture):
    functionProperties = CosineMixture.functionProperties

    def __init__(self, functionProperties, sd=1, maxfeval=10):
        super().__init__(functionProperties, N=6, sd=sd, maxfeval=maxfeval)


class CosineMixtureN10(CosineMixture):
    functionProperties = CosineMixture.functionProperties

    def __init__(self, functionProperties, sd=1, maxfeval=10):
        super().__init__(functionProperties, N=10, sd=sd, maxfeval=maxfeval)


class CosineMixtureN20(CosineMixture):
    functionProperties = CosineMixture.functionProperties

    def __init__(self, functionProperties, sd=1, maxfeval=10):
        super().__init__(functionProperties, N=20, sd=sd, maxfeval=maxfeval)