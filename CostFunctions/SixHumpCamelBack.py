from CostFunctions import CostFunctions
import numpy as np

__all__ = ['SixHumpCamelBack']


class SixHumpCamelBack(CostFunctions):
    functionProperties = {
        'minimumValue': -1.0316,
        'optimalArms': [[-0.0898, 0.7126], [0.0898, -0.7126]],
        'searchSpace': [[-5, 5], [-5, 5]],
        'spaceType': ['uniform', 'uniform'],
        'x0': [np.random.uniform(-5, 5), np.random.uniform(-5, 5)],
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
        f1 = (4-2.1*np.power(x1,2) + np.power(x1,4)/3)*np.power(x1,2)
        f2 = x1*x2
        f3 = 4*(np.power(x2,2) -1)*np.power(x2,2)
        value = f1 +f2 +f3
        return value
