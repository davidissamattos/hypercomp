from CostFunctions import CostFunctions
import numpy as np

__all__ = ['Alpine2']


class Alpine2(CostFunctions):
    functionProperties = {
        'optimalArms_SingleDimension': 7.917,
        'searchSpace_SingleDimension': [0, 10],
        'spaceType_SingleDimension': 'uniform',
        'x0_SingleDimension': np.random.uniform(0,10),
        'Continuous': 'Continuous',
        'Differentiability': 'Differentiable',
        'Separability': 'Non-Separable',
        'Scalability': 'Non-Scalable',
        'Modality': 'Multimodal',
    }

    def __init__(self, functionProperties, N=3, sd=1, maxfeval=10, tol=0.001):
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
        functionProperties['Ndimensions'] = N
        functionProperties['minimumValue'] = -np.power(2.808, int(N))
        tol = 0.1*N
        super().__init__(functionProperties, sd=sd, maxfeval=maxfeval, tol=tol)

    def func(self, x):
        value = 1
        for i in range(self.N):
            value = value * (np.sqrt(x[i]) * np.sin(x[i]))
        return -value
