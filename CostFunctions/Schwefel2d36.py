"""
Implementation of the Schwefel2d36.py function

# Created by davidis at 2020-02-14
"""

from CostFunctions import CostFunctions
import numpy as np

__all__ = ['Schwefel2d36']


class Schwefel2d36(CostFunctions):
    """
    Implementation of the Schwefel2d36.py function from 
    M. Jamil and X.-S. S. Yang, “A Literature Survey of Benchmark Functions For Global Optimization Problems,” Int. J. Math. Model. Numer. Optim., vol. 4, no. 2, p. 150, Aug. 2013.
    """
    functionProperties = {
        'minimumValue': -3456,
        'optimalArms': [[12, 12]],
        'searchSpace': [[0, 500], [0, 500]],
        'spaceType': ['uniform', 'uniform'],
        'x0': [np.random.uniform(0, 500), np.random.uniform(0, 500)],
        'Continuous': 'Continuous',
        'Differentiability': 'Differentiable',
        'Separability': 'Separable',
        'Scalability': 'Scalable',
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
        value = -x1*x2*(72.0 - 2.0*x1 - 2.0*x2)
        return value