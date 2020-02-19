"""
Implementation of the Trefethen.py function

# Created by davidis at 2020-02-19
"""

from CostFunctions import CostFunctions
import numpy as np

__all__ = ['Trefethen']


class Trefethen(CostFunctions):
    """
    Implementation of the Trefethen.py function from 
    M. Jamil and X.-S. S. Yang, “A Literature Survey of Benchmark Functions For Global Optimization Problems,” Int. J. Math. Model. Numer. Optim., vol. 4, no. 2, p. 150, Aug. 2013.
    """
    functionProperties = {
        'minimumValue': -3.30686865,
        'optimalArms': [[-0.024403, 0.210612]],
        'searchSpace': [[-10, 5], [-5, 10]],
        'spaceType': ['uniform', 'uniform'],
        'x0': [np.random.uniform(-10, 5), np.random.uniform(-5, 10)],
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
        """
        value = np.exp(np.sin(50 * x[0])) + np.sin(60 * np.exp(x[1])) + np.sin(70 * np.sin(x[0])) + \
            np.sin(np.sin(80 * x[1])) - np.sin(10 * (x[0] + x[1])) + 1.0 / 4 * (x[0] ** 2 + x[1] ** 2)
        return value