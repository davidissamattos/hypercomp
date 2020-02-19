"""
Implementation of the Schwefel2d6.py function

# Created by davidis at 2020-02-14
"""

from CostFunctions import CostFunctions
import numpy as np

__all__ = ['Schwefel2d6']


class Schwefel2d6(CostFunctions):
    """
    Implementation of the Schwefel2d6.py function from 
    M. Jamil and X.-S. S. Yang, “A Literature Survey of Benchmark Functions For Global Optimization Problems,” Int. J. Math. Model. Numer. Optim., vol. 4, no. 2, p. 150, Aug. 2013.
    """
    functionProperties = {
        'minimumValue': 0,
        'optimalArms': [[1, 3]],
        'searchSpace': [[-10, 5], [-10, 5]],
        'spaceType': ['uniform', 'uniform'],
        'x0': [np.random.uniform(-10, 5), np.random.uniform(-10, 5)],
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
        value = np.max([np.abs(x1 + 2*x2 - 7), np.abs(2*x1 + x2 - 5)])
        return value