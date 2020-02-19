"""
Implementation of the Price1.py function

# Created by davidis at 2020-01-22
"""

from CostFunctions import CostFunctions
import numpy as np

__all__ = ['Price1']


class Price1(CostFunctions):
    """
    Implementation of the Price1.py function from 
    M. Jamil and X.-S. S. Yang, “A Literature Survey of Benchmark Functions For Global Optimization Problems,” Int. J. Math. Model. Numer. Optim., vol. 4, no. 2, p. 150, Aug. 2013.
    """
    functionProperties = {
        'minimumValue': 0,
        'optimalArms': [[5, 5],
                        [-5, 5],
                        [5, -5],
                        [-5, -5]],
        'searchSpace': [[-10, 10], [-10, 10]],
        'spaceType': ['uniform', 'uniform'],
        'x0': [np.random.uniform(-10, 10), np.random.uniform(-10, 10)],
        'Continuous': 'Continuous',
        'Differentiability': 'Non-Differentiable',
        'Separability': 'Separable',
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

        value = (np.abs(x[0]) - 5.0) ** 2.0 + (np.abs(x[1]) - 5.0) ** 2.0
        return value