from CostFunctions import CostFunctions
import numpy as np
__all__ = ['Easom']

class Easom(CostFunctions):
    functionProperties = {
        'minimumValue': -1,
        'optimalArms': [[np.pi, np.pi]],
        'searchSpace': [[-100, 100], [-100, 100]],
        'spaceType': ['uniform', 'uniform'],
        'x0': [np.random.uniform(-100,100),np.random.uniform(-100,100)],
        'Continuous': 'Continuous',
        'Differentiability': 'Differentiable',
        'Separability': 'Separable',
        'Scalability': 'Non-Scalable',
        'Modality': 'Multimodal',
        'Ndimensions': 2
    }

    def func(self, x):
        # print('x: ',x)
        x1 = x[0]
        x2 = x[1]
        value = -np.cos(x1) * np.cos(x2) * np.exp(-(x1 - np.pi) ** 2 - (x2 - np.pi) ** 2)
        return value
