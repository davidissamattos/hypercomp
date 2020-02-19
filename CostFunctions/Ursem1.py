"""
Implementation of the Ursem1.py function

# Created by davidis at 2020-02-19
"""

from CostFunctions import CostFunctions
import numpy as np

__all__ = ['Ursem1']


class Ursem1(CostFunctions):
    """
    Implementation of the Ursem1.py function from 
    M. Jamil and X.-S. S. Yang, “A Literature Survey of Benchmark Functions For Global Optimization Problems,” Int. J. Math. Model. Numer. Optim., vol. 4, no. 2, p. 150, Aug. 2013.
    """
    functionProperties = {
        'minimumValue': -4.8168,
        'optimalArms': [[1.69714, 0.0]],
        'searchSpace': [[-2.5, 3], [-2.5, 1.5]],
        'spaceType': ['uniform', 'uniform'],
        'x0': [np.random.uniform(-2.5, 3), np.random.uniform(-2.5, 1.5)],
        'Continuous': 'Continuous',
        'Differentiability': 'Differentiable',
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
        x1 = x[0]
        x2 = x[1]
        value = -np.sin(2*x1 - 0.5*np.pi) - 3.0*np.cos(x2) - 0.5*x1
        return value