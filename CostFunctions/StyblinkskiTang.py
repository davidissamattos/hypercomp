"""
Implementation of the StyblinkskiTang.py function

# Created by davidis at 2020-02-19
"""

from CostFunctions import CostFunctions
import numpy as np

__all__ = ['StyblinkskiTang']


class StyblinkskiTang(CostFunctions):
    """
    Implementation of the StyblinkskiTang.py function from 
    M. Jamil and X.-S. S. Yang, “A Literature Survey of Benchmark Functions For Global Optimization Problems,” Int. J. Math. Model. Numer. Optim., vol. 4, no. 2, p. 150, Aug. 2013.
    """
    functionProperties = {
        'minimumValue': -78.332,
        'optimalArms': [[-2.903534, -2.903534]],
        'searchSpace': [[-5, 5], [-5, 5]],
        'spaceType': ['uniform', 'uniform'],
        'x0': [np.random.uniform(-5, 5), np.random.uniform(-5, 5)],
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
        value = 0.5*np.sum(x**4 -16*x**2 +5*x)
        return value