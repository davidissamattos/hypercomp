"""
Implementation of the BucheRastrigin function

# Created by davidis at 2020-02-27
"""

from CostFunctions import CostFunctions
import numpy as np
from CostFunctions.BBOBAuxFunctions import *

__all__ = ['BucheRastriginN2', 'BucheRastriginN6', 'BucheRastriginN10', 'BucheRastriginN20']


class BucheRastrigin(CostFunctions):
    """
    Implementation of the BucheRastrigin function from
    M. Jamil and X.-S. S. Yang, “A Literature Survey of Benchmark Functions For Global Optimization Problems,” Int. J. Math. Model. Numer. Optim., vol. 4, no. 2, p. 150, Aug. 2013.
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
        tosz=Tosz(x)
        s = np.zeros(self.N)
        i=1
        j=0
        for xi in x:
            s[j]=np.power(10,0.5*(i-1)/(self.N-1))
            if xi>0 and xi%2==1:
                s[j]= 10*s[j]
            j=j+1
            i=i+1
        z= s*tosz
        value = 10*(self.N - np.sum(np.cos(2*np.pi*z))) + np.sum(z**2) + 100*fpen(x)
        return value


class BucheRastriginN2(BucheRastrigin):
    functionProperties = BucheRastrigin.functionProperties

    def __init__(self, functionProperties, sd=1, maxfeval=10):
        super().__init__(functionProperties, N=2, sd=sd, maxfeval=maxfeval)


class BucheRastriginN6(BucheRastrigin):
    functionProperties = BucheRastrigin.functionProperties

    def __init__(self, functionProperties, sd=1, maxfeval=10):
        super().__init__(functionProperties, N=6, sd=sd, maxfeval=maxfeval)


class BucheRastriginN10(BucheRastrigin):
    functionProperties = BucheRastrigin.functionProperties

    def __init__(self, functionProperties, sd=1, maxfeval=10):
        super().__init__(functionProperties, N=10, sd=sd, maxfeval=maxfeval)


class BucheRastriginN20(BucheRastrigin):
    functionProperties = BucheRastrigin.functionProperties

    def __init__(self, functionProperties, sd=1, maxfeval=10):
        super().__init__(functionProperties, N=20, sd=sd, maxfeval=maxfeval)