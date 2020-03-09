"""
Implementation of the Wolfe.py function

# Created by davidis at 2020-02-24
"""

from CostFunctions import CostFunctions
import numpy as np

__all__ = ['Wolfe']


class Wolfe(CostFunctions):
    """
    Implementation of the Wolfe.py function from 
    M. Jamil and X.-S. S. Yang, “A Literature Survey of Benchmark Functions For Global Optimization Problems,” Int. J. Math. Model. Numer. Optim., vol. 4, no. 2, p. 150, Aug. 2013.
    """
    functionProperties = {
        'minimumValue': 0,
        'optimalArms': [[0, 0, 0]],
        'searchSpace': [[0, 2], [0, 2], [0, 2]],
        'spaceType': ['uniform', 'uniform', 'uniform'],
        'x0': [np.random.uniform(0, 2), np.random.uniform(0, 2), np.random.uniform(0, 2)],
        'Continuous': 'Continuous',
        'Differentiability': 'Differentiable',
        'Separability': 'Separable',
        'Scalability': 'Scalable',
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
        value = (4.0/3.0)*(x1**2.0 + x2**2.0 - x1*x2)**0.75 + x3
        return value