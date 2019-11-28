"""
Implementation of the GoldsteinPrice.py function

# Created by davidis at 2019-11-22
"""

from CostFunctions import CostFunctions
import numpy as np

__all__ = ['GoldsteinPrice']


class GoldsteinPrice(CostFunctions):
    """
    Implementation of the GoldsteinPrice.py function from 
    M. Jamil and X.-S. S. Yang, “A Literature Survey of Benchmark Functions For Global Optimization Problems,” Int. J. Math. Model. Numer. Optim., vol. 4, no. 2, p. 150, Aug. 2013.
    """
    functionProperties = {
        'minimumValue': 3,
        'optimalArms': [[0, -1]],
        'searchSpace': [[-2, 2], [-2, 2]],
        'spaceType': ['uniform', 'uniform'],
        'x0': [np.random.uniform(-2, 2), np.random.uniform(-2, 2)],
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
        value = (1+ np.power(x1+ x2 +1,2)*(19 -14*x1 +3* np.power(x1,2) - 14*x2 + 6*x1*x2 +3*np.power(x2,2)))*\
                (30+ np.power(2*x1-3*x2, 2)*(18-32*x1+12*np.power(x1,2)+48*x2 - 36*x1*x2 +27*np.power(x2,2)))
        return value