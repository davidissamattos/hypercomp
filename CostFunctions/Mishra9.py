"""
Implementation of the Mishra9.py function

# Created by davidis at 2020-01-22
"""

from CostFunctions import CostFunctions
import numpy as np

__all__ = ['Mishra9']


class Mishra9(CostFunctions):
    """
    Implementation of the Mishra9.py function from 
    M. Jamil and X.-S. S. Yang, “A Literature Survey of Benchmark Functions For Global Optimization Problems,” Int. J. Math. Model. Numer. Optim., vol. 4, no. 2, p. 150, Aug. 2013.
    """
    functionProperties = {
        'minimumValue': 0,
        'optimalArms': [[1.0, 2.0, 3.0]],
        'searchSpace': [[-5, 10], [-10, 5],[-10,10]],
        'spaceType': ['uniform', 'uniform','uniform'],
        'x0': [np.random.uniform(-5, 10), np.random.uniform(-10, 5),np.random.uniform(-10, 10)],
        'Continuous': 'Continuous',
        'Differentiability': 'Differentiable',
        'Separability': 'Non-Separable',
        'Scalability': 'Non-Scalable',
        'Modality': 'Multimodal',
        'Ndimensions': 3
    }

    def func(self, x):
        """
        x is an array E.g.
        x1 = x[0]
        x2 = x[1]
        """
        x1 = x[0]
        x2 = x[1]
        x3 = x[2]
        F1 = 2 * x1 ** 3 + 5 * x1 * x2 + 4 * x3 - 2 * x1 ** 2 * x3 - 18.0
        F2 = x1 + x2 ** 3 + x1 * x2 ** 2 + x1 * x3 ** 2 - 22.0
        F3 = 8 * x1 ** 2 + 2 * x2 * x3 + 2 * x2 ** 2 + 3 * x2 ** 3 - 52.0
        value = (F1 * F3 * F2 ** 2 + F1 * F2 * F3 ** 2 + F2 ** 2 + (x1 + x2 - x3) ** 2) ** 2
        return value