"""
Implementation of the Leon.py function

# Created by davidis at 2020-01-07
"""

from CostFunctions import CostFunctions
import numpy as np

__all__ = ['Leon']


class Leon(CostFunctions):
    """
    Implementation of the Leon.py function from 
    M. Jamil and X.-S. S. Yang, “A Literature Survey of Benchmark Functions For Global Optimization Problems,” Int. J. Math. Model. Numer. Optim., vol. 4, no. 2, p. 150, Aug. 2013.
    """
    functionProperties = {
        'minimumValue': 0,
        'optimalArms': [[1, 1]],
        'searchSpace': [[-1.2, 1.2], [-1.2, 1.2]],
        'spaceType': ['uniform', 'uniform'],
        'x0': [np.random.uniform(-1.2, 1.2), np.random.uniform(-1.2, 1.2)],
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
        x1 = x[0]
        x2 = x[1]
        value = 100*(x2 - x1*x1)**2.0 + (1 - x1)**2.0
        return value