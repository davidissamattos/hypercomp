"""
Implementation of the Zettl.py function

# Created by davidis at 2020-02-26
"""

from CostFunctions import CostFunctions
import numpy as np

__all__ = ['Zettl']


class Zettl(CostFunctions):
    """
    Implementation of the Zettl.py function from 
    M. Jamil and X.-S. S. Yang, “A Literature Survey of Benchmark Functions For Global Optimization Problems,” Int. J. Math. Model. Numer. Optim., vol. 4, no. 2, p. 150, Aug. 2013.
    """
    functionProperties = {
        'minimumValue': -0.003791237220468656,
        'optimalArms': [[-0.02989597760285287, 0]],
        'searchSpace': [[-5, 10], [-5, 10]],
        'spaceType': ['uniform', 'uniform'],
        'x0': [np.random.uniform(-5, 10), np.random.uniform(-5, 10)],
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
        value = (x1**2 + x2**2 - 2*x1)**2 + x1/4
        return value