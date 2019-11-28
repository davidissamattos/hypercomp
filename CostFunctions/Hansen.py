"""
Implementation of the Hansen.py function

# Created by davidis at 2019-11-22
"""

from CostFunctions import CostFunctions
import numpy as np

__all__ = ['Hansen']


class Hansen(CostFunctions):
    """
    Implementation of the Hansen.py function from 
    M. Jamil and X.-S. S. Yang, “A Literature Survey of Benchmark Functions For Global Optimization Problems,” Int. J. Math. Model. Numer. Optim., vol. 4, no. 2, p. 150, Aug. 2013.
    """
    functionProperties = {
        'minimumValue':  -176.5417931283926,
        'optimalArms': [[-7.58989583,  -7.70831466],
                        [-7.58989583, 4.858057],
                        [-1.306708, 4.858057],
                        [4.976478, -1.425128],
                        [-7.58989583, -1.425128],
                        [-1.306708, -7.70831466],
                        [4.976478, 4.858057],
                        [4.976478, -7.70831466]],
        'searchSpace': [[-10, 10], [-10, 10]],
        'spaceType': ['uniform', 'uniform'],
        'x0': [np.random.uniform(-10, 10), np.random.uniform(-10, 10)],
        'Continuous': 'Continuous',
        'Differentiability': 'Differentiable',
        'Separability': 'Separable',
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
        i = np.arange(0,5)
        f1 = (i+1)*np.cos(i*x1 + i +1)
        f2 = (i+1)*np.cos((i+2)*x2 +i+1)
        value = np.sum(f1)*np.sum(f2)
        return value