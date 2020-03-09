"""
Implementation of the WayburnSeader2.py function

# Created by davidis at 2020-02-19
"""

from CostFunctions import CostFunctions
import numpy as np

__all__ = ['WayburnSeader2']


class WayburnSeader2(CostFunctions):
    """
    Implementation of the WayburnSeader2.py function from 
    M. Jamil and X.-S. S. Yang, “A Literature Survey of Benchmark Functions For Global Optimization Problems,” Int. J. Math. Model. Numer. Optim., vol. 4, no. 2, p. 150, Aug. 2013.
    """
    functionProperties = {
        'minimumValue': 0,
        'optimalArms': [[0.2, 1], [0.425,1]],
        'searchSpace': [[-5, 3], [-5, 3]],
        'spaceType': ['uniform', 'uniform'],
        'x0': [np.random.uniform(-5, 3), np.random.uniform(-5, 3)],
        'Continuous': 'Continuous',
        'Differentiability': 'Differentiable',
        'Separability': 'Non-Separable',
        'Scalability': 'Scalable',
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
        value = (1.613 - 4.0*(x1 - 0.3125)**2.0 - 4.0*(x2 - 1.625)**2.0)**2.0 + (x2 - 1.0)**2.0
        return value