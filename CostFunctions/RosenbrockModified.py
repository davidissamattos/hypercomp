from CostFunctions import CostFunctions
import numpy as np

__all__ = ['RosenbrockModified']


class RosenbrockModified(CostFunctions):
    """
    https://github.com/andyfaff/ampgo/blob/master/%20ampgo%20--username%20andrea.gavana%40gmail.com/go_benchmark.py
    """
    functionProperties = {
        'minimumValue': 34.3712,
        'optimalArms': [[-0.9, -0.95]],
        'searchSpace': [[-2, 2], [-2, 2]],
        'spaceType': ['uniform', 'uniform'],
        'x0': [np.random.uniform(-2, 2), np.random.uniform(-2, 2)],
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

        value = 74.0 + 100.0*(x2 - x1**2.0)**2.0 + (1.0 - x1)**2.0 - 400.0*np.exp(-((x1 + 1.0)**2.0 + (x2 + 1.0)**2.0)/0.1)
        return value