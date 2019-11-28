from CostFunctions import CostFunctions
import numpy as np
__all__ = ['Miele']

class Miele(CostFunctions):
    functionProperties = {
        'minimumValue': 0,
        'optimalArms': [[0, 1, 1, 1]],
        'searchSpace': [[-1, 1], [-1, 1], [-1, 1], [-1, 1]],
        'spaceType': ['uniform', 'uniform', 'uniform', 'uniform'],
        'x0': [np.random.uniform(-1,1), np.random.uniform(-1,1), np.random.uniform(-1,1), np.random.uniform(-1,1)],
        'Continuous': 'Continuous',
        'Differentiability': 'Differentiable',
        'Separability': 'Non-Separable',
        'Scalability': 'Non-Scalable',
        'Modality': 'Multimodal',
        'Ndimensions': 4
    }

    def func(self, x):
        x1 = x[0]
        x2 = x[1]
        x3 = x[2]
        x4 = x[3]
        value = -(np.exp(-x1) - x2) ** 4 - 100 * (x2 - x3) ** 6 - (np.tan(x3 - x4)) ** 4 - x1 ** 8
        return value