from CostFunctions import CostFunctions
import numpy as np

__all__ = ['BraninRCOS']


class BraninRCOS(CostFunctions):
    functionProperties = {
        'minimumValue': 0.3978873,
        'optimalArms': [[-np.pi, 12.275], [np.pi, 2.275], [3 * np.pi, 2.475]],
        'searchSpace': [[-5, 10], [0, 15]],
        'spaceType': ['uniform', 'uniform'],
        'x0': [np.random.uniform(-5,10), np.random.uniform(0,15)],
        'Continuous': 'Continuous',
        'Differentiability': 'Differentiable',
        'Separability': 'Non-Separable',
        'Scalability': 'Non-Scalable',
        'Modality': 'Multimodal',
        'Ndimensions': 2
    }

    def func(self, x):
        x1 = x[0]
        x2 = x[1]
        value = np.power(x2 - (5.1 * np.power(x1,2)) / (4 * (np.power(np.pi, 2))) + (5 * x1)/(np.pi) - 6,2) + \
                10 * (1 - 1 / (8 * np.pi)) * np.cos(x1) + \
                10
        return value
