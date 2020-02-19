"""
Implementation of the UrsemWaves.py function

# Created by davidis at 2020-02-19
"""

from CostFunctions import CostFunctions
import numpy as np

__all__ = ['UrsemWaves']


class UrsemWaves(CostFunctions):
    """
    Implementation of the UrsemWaves.py function from 
    M. Jamil and X.-S. S. Yang, “A Literature Survey of Benchmark Functions For Global Optimization Problems,” Int. J. Math. Model. Numer. Optim., vol. 4, no. 2, p. 150, Aug. 2013.
    """
    functionProperties = {
        'minimumValue': -8.5536,
        'optimalArms': [[1.2, 1.2]],
        'searchSpace': [[-0.9, 1.2], [-1.2, 1.2]],
        'spaceType': ['uniform', 'uniform'],
        'x0': [np.random.uniform(-0.9, 1.2), np.random.uniform(-1.2, 1.2)],
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
        value =- 0.9*x1**2.0 + (x2**2.0 - 4.5*x2**2.0)*x1*x2 + \
               4.7*np.cos(3*x1 - x2**2.0*(2.0 + x1))*np.sin(2.5*np.pi*x1)

        return value