"""
Implementation of the simpleQuadratic.py function

# Created by davidis at 2019-11-25
"""

from CostFunctions import CostFunctions
import numpy as np

__all__ = ['simpleQuadratic']


class simpleQuadratic(CostFunctions):
    """
    Implementation of the simpleQuadratic.py function from 
    M. Jamil and X.-S. S. Yang, “A Literature Survey of Benchmark Functions For Global Optimization Problems,” Int. J. Math. Model. Numer. Optim., vol. 4, no. 2, p. 150, Aug. 2013.
    """
    functionProperties = {
        'minimumValue': -0.25,
        'optimalArms': [[-2.5]],
        'searchSpace': [[-5, 5]],
        'spaceType': ['uniform'],
        'x0': [np.random.uniform(-5, 5)],
        'Continuous': 'Continuous',
        'Differentiability': 'Differentiable',
        'Separability': 'Separable',
        'Scalability': 'Scalable',
        'Modality': 'Unimodal',
        'Ndimensions': 1
    }

    def func(self, x):
        """
        x is an array E.g.
        x1 = x[0]
        x2 = x[1]
        """
        x1 = x[0]
        value = np.power(x1,2) + 5*x1 +6
        # print('x: ', x1, ' f(x): ', value)
        return value