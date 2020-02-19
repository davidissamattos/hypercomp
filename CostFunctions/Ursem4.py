"""
Implementation of the Ursem4.py function

# Created by davidis at 2020-02-19
"""

from CostFunctions import CostFunctions
import numpy as np

__all__ = ['Ursem4']


class Ursem4(CostFunctions):
    """
    Implementation of the Ursem4.py function from 
    M. Jamil and X.-S. S. Yang, “A Literature Survey of Benchmark Functions For Global Optimization Problems,” Int. J. Math. Model. Numer. Optim., vol. 4, no. 2, p. 150, Aug. 2013.
    """
    functionProperties = {
        'minimumValue': -1.5,
        'optimalArms': [[0, 0]],
        'searchSpace': [[-1, 3], [-3, 1]],
        'spaceType': ['uniform', 'uniform'],
        'x0': [np.random.uniform(-1, 3), np.random.uniform(-3, 1)],
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
        value = -3*np.sin(0.5*np.pi*x1 + 0.5*np.pi)*(2.0 - np.sqrt(x1**2.0 + x2**2.0))/4.0
        return value