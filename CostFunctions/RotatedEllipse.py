"""
Implementation of the RotatedEllipse.py function

# Created by davidis at 2020-01-22
"""

from CostFunctions import CostFunctions
import numpy as np

__all__ = ['RotatedEllipse']


class RotatedEllipse(CostFunctions):
    """
    Implementation of the RotatedEllipse.py function from 
    M. Jamil and X.-S. S. Yang, “A Literature Survey of Benchmark Functions For Global Optimization Problems,” Int. J. Math. Model. Numer. Optim., vol. 4, no. 2, p. 150, Aug. 2013.
    """
    functionProperties = {
        'minimumValue': 0,
        'optimalArms': [[0, 0]],
        'searchSpace': [[-15, 50], [-50, 15]],
        'spaceType': ['uniform', 'uniform'],
        'x0': [np.random.uniform(-15, 50), np.random.uniform(-50, 15)],
        'Continuous': 'Continuous',
        'Differentiability': 'Differentiable',
        'Separability': 'Non-Separable',
        'Scalability': 'Non-Scalable',
        'Modality': 'Unimodal',
        'Ndimensions': 2
    }

    def func(self, x):
        """
        x is an array E.g.
        x1 = x[0]
        x2 = x[1]
        """
        value = (7.0 * x[0] ** 2.0 - 6.0 * np.sqrt(3) * x[0] * x[1]
         + 13 * x[1] ** 2.0)
        return value