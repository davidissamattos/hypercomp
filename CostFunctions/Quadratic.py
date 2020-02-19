"""
Implementation of the Quadratic.py function

# Created by davidis at 2020-02-13
"""

from CostFunctions import CostFunctions
import numpy as np

__all__ = ['Quadratic']


class Quadratic(CostFunctions):
    """
    Implementation of the Quadratic.py function from 
    M. Jamil and X.-S. S. Yang, “A Literature Survey of Benchmark Functions For Global Optimization Problems,” Int. J. Math. Model. Numer. Optim., vol. 4, no. 2, p. 150, Aug. 2013.
    """
    functionProperties = {
        'minimumValue': -3873.72418,
        'optimalArms': [[0.19388, 0.48513]],
        'searchSpace': [[-10, 5], [-5, 10]],
        'spaceType': ['uniform', 'uniform'],
        'x0': [np.random.uniform(-10, 5), np.random.uniform(-5, 10)],
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
        value = -3803.84 - 138.08*x1 - 232.92*x2 + 128.08*x1**2.0 + 203.64*x2**2.0 + 182.25*x1*x2
        return value