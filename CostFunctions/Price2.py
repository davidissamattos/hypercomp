"""
Implementation of the Price2.py function

# Created by davidis at 2020-01-22
"""

from CostFunctions import CostFunctions
import numpy as np

__all__ = ['Price2']


class Price2(CostFunctions):
    """
    Implementation of the Price2.py function from 
    M. Jamil and X.-S. S. Yang, “A Literature Survey of Benchmark Functions For Global Optimization Problems,” Int. J. Math. Model. Numer. Optim., vol. 4, no. 2, p. 150, Aug. 2013.
    """
    functionProperties = {
        'minimumValue': 0.9,
        'optimalArms': [[0, 0]],
        'searchSpace': [[-5, 10], [-10, 5]],
        'spaceType': ['uniform', 'uniform'],
        'x0': [np.random.uniform(-5, 10), np.random.uniform(-10, 5)],
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
        x1 = x[0]
        x2 = x[1]
        value = 1.0 + np.sin(x1) ** 2+ np.sin(x2)**2 - 0.1 * np.exp(-x1 ** 2.0 - x2 ** 2.0)

        return value