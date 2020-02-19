"""
Implementation of the PowellSingular.py function

# Created by davidis at 2020-01-22
"""

from CostFunctions import CostFunctions
import numpy as np

__all__ = ['PowellSingular']


class PowellSingular(CostFunctions):
    """
    Implementation of the PowellSingular.py function from 
    M. Jamil and X.-S. S. Yang, “A Literature Survey of Benchmark Functions For Global Optimization Problems,” Int. J. Math. Model. Numer. Optim., vol. 4, no. 2, p. 150, Aug. 2013.
    """
    functionProperties = {
        'minimumValue': 0,
        'optimalArms': [[0, 0,0,0]],
        'searchSpace': [[-4, 5], [-4, 5],[-4, 5],[-4, 5]],
        'spaceType': ['uniform', 'uniform','uniform','uniform'],
        'x0': [np.random.uniform(-4, 5),
               np.random.uniform(-4, 5),
               np.random.uniform(-4, 5),
               np.random.uniform(-4, 5)],
        'Continuous': 'Continuous',
        'Differentiability': 'Differentiable',
        'Separability': 'Non-Separable',
        'Scalability': 'Non-Scalable',
        'Modality': 'Unimodal',
        'Ndimensions': 4
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
        x4 = x[3]
        value = (x1 + 10*x2)**2 + 5*(x3-x4)**2 + (x2-2*x3)**4 + 10*(x1-x4)**4
        return value