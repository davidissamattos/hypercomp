"""
Implementation of the PenHolder.py function

# Created by davidis at 2020-01-22
"""

from CostFunctions import CostFunctions
import numpy as np

__all__ = ['PenHolder']


class PenHolder(CostFunctions):
    """
    Implementation of the PenHolder.py function from 
    M. Jamil and X.-S. S. Yang, “A Literature Survey of Benchmark Functions For Global Optimization Problems,” Int. J. Math. Model. Numer. Optim., vol. 4, no. 2, p. 150, Aug. 2013.
    """
    functionProperties = {
        'minimumValue': -0.9635348327265058,
        'optimalArms': [[-9.646167708023526, 9.646167671043401],
                        [9.646167708023526, 9.646167671043401],
                        [-9.646167708023526, -9.646167671043401],
                        [9.646167708023526, -9.646167671043401]],
        'searchSpace': [[-11, 11], [-11, 11]],
        'spaceType': ['uniform', 'uniform'],
        'x0': [np.random.uniform(-11, 11), np.random.uniform(-11, 11)],
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
        a = np.abs(1. - (np.sqrt(x[0] ** 2 + x[1] ** 2) / np.pi))
        b = np.cos(x[0]) * np.cos(x[1]) * np.exp(a)
        return -np.exp(-np.abs(b) ** -1)