"""
Implementation of the Himmelblau.py function

# Created by davidis at 2020-01-07
"""

from CostFunctions import CostFunctions
import numpy as np

__all__ = ['Himmelblau']


class Himmelblau(CostFunctions):
    """
    Implementation of the Himmelblau.py function from 
    M. Jamil and X.-S. S. Yang, “A Literature Survey of Benchmark Functions For Global Optimization Problems,” Int. J. Math. Model. Numer. Optim., vol. 4, no. 2, p. 150, Aug. 2013.
    """
    functionProperties = {
        'minimumValue': 0,
        'optimalArms': [[3, 2]], #Jamil
        #'optimalArms': [[0, 0]], #ampgo
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
        x1 = x[0]
        x2 = x[1]
        value =  np.power(x1 * x1 + x2 - 11, 2) + np.power(x1 + x2 * x2 - 7, 2)
        return value