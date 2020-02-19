"""
Implementation of the SchafferF6.py function

# Created by davidis at 2020-02-17
"""

from CostFunctions import CostFunctions
import numpy as np

__all__ = ['SchafferF6']


class SchafferF6(CostFunctions):
    """
    Implementation of the SchafferF6.py function from 
    M. Jamil and X.-S. S. Yang, “A Literature Survey of Benchmark Functions For Global Optimization Problems,” Int. J. Math. Model. Numer. Optim., vol. 4, no. 2, p. 150, Aug. 2013.
    """
    functionProperties = {
        'minimumValue': 0,
        'optimalArms': [[0, 0]],
        'searchSpace': [[-30, 100], [-100, 30]],
        'spaceType': ['uniform', 'uniform'],
        'x0': [np.random.uniform(-30, 100), np.random.uniform(-100, 30)],
        'Continuous': 'Continuous',
        'Differentiability': 'Differentiable',
        'Separability': 'Non-Separable',
        'Scalability': 'Non-Scalable',
        'Modality': 'Multimodal',
        'Ndimensions': 2
    }

    def func(self, xi):
        """
        x is an array E.g.
        x1 = x[0]
        x2 = x[1]
        """
        x = xi[0]

        y = xi[1]
        value = 0.5 + ((np.sin(np.sqrt(x**2 + y**2)))**2 -0.5)/((1+0.001*(x**2+y**2))**2)
        return value