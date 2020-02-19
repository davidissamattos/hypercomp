"""
Implementation of the Ursem3.py function

# Created by davidis at 2020-02-19
"""

from CostFunctions import CostFunctions
import numpy as np

__all__ = ['Ursem3']


class Ursem3(CostFunctions):
    """
    Implementation of the Ursem3.py function from 
    M. Jamil and X.-S. S. Yang, “A Literature Survey of Benchmark Functions For Global Optimization Problems,” Int. J. Math. Model. Numer. Optim., vol. 4, no. 2, p. 150, Aug. 2013.
    """
    functionProperties = {
        'minimumValue': -3,
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
        value = -np.sin(2.2*np.pi*x1 + 0.5*np.pi)*((2.0 - np.abs(x1))/2.0)*((3.0 - np.abs(x1))/2.0) - np.sin(2.2*np.pi*x2 + 0.5*np.pi)*((2.0 - np.abs(x2))/2.0)*((3.0 - np.abs(x2))/2.0)
        return value