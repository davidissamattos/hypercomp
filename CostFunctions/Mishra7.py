"""
Implementation of the Mishra7.py function

# Created by davidis at 2020-01-13
"""

from CostFunctions import CostFunctions
import numpy as np

__all__ = ['Mishra7N2', 'Mishra7N6', 'Mishra7N10', 'Mishra7N20']


class Mishra7(CostFunctions):
    """
    Implementation of the Mishra7.py function from
    M. Jamil and X.-S. S. Yang, “A Literature Survey of Benchmark Functions For Global Optimization Problems,” Int. J. Math. Model. Numer. Optim., vol. 4, no. 2, p. 150, Aug. 2013.
    https://github.com/andyfaff/ampgo/blob/master/%20ampgo%20--username%20andrea.gavana%40gmail.com/go_benchmark.py
    """
    functionProperties = {
        'minimumValue': 0,
        #'optimalArms_SingleDimension': 0, #for this case
        'searchSpace_SingleDimension': [-100, 100],
        'spaceType_SingleDimension': 'uniform',
        'x0_SingleDimension': np.random.uniform(-100, 100),
        'Continuous': 'Continuous',
        'Differentiability': 'Differentiable',
        'Separability': 'Non-Separable',
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
            optimalArm.append(i+1)#Maximum is a vector like [1 2 3 4 ... D]
        functionProperties['optimalArms'] = [optimalArm]
        functionProperties['x0'] = x0
        functionProperties['spaceType'] = spaceType
        functionProperties['searchSpace'] = searchSpace
        functionProperties['Ndimensions'] = self.N
        super().__init__(functionProperties, sd=sd, maxfeval=maxfeval)

    def func(self, x):
        value = np.power(np.prod(x) - np.math.factorial(int(self.N)),2)
        return value


class Mishra7N2(Mishra7):
    functionProperties = Mishra7.functionProperties

    def __init__(self, functionProperties, sd=1, maxfeval=10):
        super().__init__(functionProperties, N=2, sd=sd, maxfeval=maxfeval)


class Mishra7N6(Mishra7):
    functionProperties = Mishra7.functionProperties

    def __init__(self, functionProperties, sd=1, maxfeval=10):
        super().__init__(functionProperties, N=6, sd=sd, maxfeval=maxfeval)


class Mishra7N10(Mishra7):
    functionProperties = Mishra7.functionProperties

    def __init__(self, functionProperties, sd=1, maxfeval=10):
        super().__init__(functionProperties, N=10, sd=sd, maxfeval=maxfeval)


class Mishra7N20(Mishra7):
    functionProperties = Mishra7.functionProperties

    def __init__(self, functionProperties, sd=1, maxfeval=10):
        super().__init__(functionProperties, N=20, sd=sd, maxfeval=maxfeval)