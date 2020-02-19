"""
REMOVED: INFINITY NUMBER OF SOLUTIONS
Implementation of the Step2 function

# Created by davidis at 2020-02-17
"""

from CostFunctions import CostFunctions
import numpy as np

__all__ = ['Step2N2', 'Step2N6', 'Step2N10', 'Step2N20']


class Step2(CostFunctions):
    """
    Implementation of the Step2 function from
    M. Jamil and X.-S. S. Yang, “A Literature Survey of Benchmark Functions For Global Optimization Problems,” Int. J. Math. Model. Numer. Optim., vol. 4, no. 2, p. 150, Aug. 2013.
    """
    functionProperties = {
        'minimumValue': 0.5,
        'optimalArms_SingleDimension': 0.5,
        'searchSpace_SingleDimension': [-100, 30],
        'spaceType_SingleDimension': 'uniform',
        'x0_SingleDimension': np.random.uniform(-100, 30),
        'Continuous': 'Discontinuous',
        'Differentiability': 'Non-Differentiable',
        'Separability': 'Separable',
        'Scalability': 'Scalable',
        'Modality': 'Unimodal',
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
        functionProperties['minimumValue'] = self.N*0.5

        super().__init__(functionProperties, sd=sd, maxfeval=maxfeval)

    def func(self, x):
        value = np.sum((np.abs(np.floor(x) + 0.5))**2.0)
        return value


class Step2N2(Step2):
    functionProperties = Step2.functionProperties

    def __init__(self, functionProperties, sd=1, maxfeval=10):
        super().__init__(functionProperties, N=2, sd=sd, maxfeval=maxfeval)


class Step2N6(Step2):
    functionProperties = Step2.functionProperties

    def __init__(self, functionProperties, sd=1, maxfeval=10):
        super().__init__(functionProperties, N=6, sd=sd, maxfeval=maxfeval)


class Step2N10(Step2):
    functionProperties = Step2.functionProperties

    def __init__(self, functionProperties, sd=1, maxfeval=10):
        super().__init__(functionProperties, N=10, sd=sd, maxfeval=maxfeval)


class Step2N20(Step2):
    functionProperties = Step2.functionProperties

    def __init__(self, functionProperties, sd=1, maxfeval=10):
        super().__init__(functionProperties, N=20, sd=sd, maxfeval=maxfeval)