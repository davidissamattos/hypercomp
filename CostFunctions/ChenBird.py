"""
Implementation of the ChenBird.py function

# Created by davidis at 2019-11-20
"""

from CostFunctions import CostFunctions
import numpy as np

__all__ = ['ChenBird']


class ChenBird(CostFunctions):
    """
    Implementation of the ChenBird.py function from 
    https://al-roomi.org/benchmarks/unconstrained/2-dimensions/111-chen-s-bird-function
    """
    functionProperties = {
        'minimumValue': -2000.003999984000,
        'optimalArms': [[0.5, 0.5]],
        'searchSpace': [[-500, 300], [-300, 500]],
        'spaceType': ['uniform', 'uniform'],
        'x0': [np.random.uniform(-500, 300), np.random.uniform(-300, 500)],
        'Continuous': 'Continuous',
        'Differentiability': 'Differentiable',
        'Separability': 'Non-Separable',
        'Scalability': 'Non-Scalable',
        'Modality': 'Multimodal',
        'Ndimensions': 2
    }

    def func(self, x):
        """
        x is an array E.g.
        x1 = x[0]
        x2 = x[1]
        If it depends on receiving a dimension you need to reimplement the __init__  and call
        the super and reimplement the function properties such as searchSpeace, spaceType, x0 etc...
        """
        x1 = x[0]
        x2 = x[1]
        b = 0.001
        b2 = np.power(b,2)
        f1 = b2 + np.power(np.power(x1,2) + np.power(x2,2) -1, 2)
        f2 = b2 + np.power(np.power(x1, 2) + np.power(x2, 2) - 1/2, 2)
        f3 = b2 + np.power(x1 - x2, 2)
        value = -b/f1 - b/f2 -b/f3
        return value