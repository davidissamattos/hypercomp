"""
Implementation of the Hosaki.py function

# Created by davidis at 2020-01-07
"""

from CostFunctions import CostFunctions
import numpy as np

__all__ = ['Hosaki']


class Hosaki(CostFunctions):
    """
    Implementation of the Hosaki.py function from 
    M. Jamil and X.-S. S. Yang, “A Literature Survey of Benchmark Functions For Global Optimization Problems,” Int. J. Math. Model. Numer. Optim., vol. 4, no. 2, p. 150, Aug. 2013.
    """
    functionProperties = {
        'minimumValue': -2.3458,
        'optimalArms': [[4, 2]],
        'searchSpace': [[0, 5], [0, 6]],
        'spaceType': ['uniform', 'uniform'],
        'x0': [np.random.uniform(0, 5), np.random.uniform(0, 6)],
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
        value = (1- 8*x1+ 7*x1*x1 -7*x1*x1*x1/3 + np.power(x1,4)/4)*x2*x2*np.exp(-x2)
        return value