"""
Implementation of the Mishra8.py function

# Created by davidis at 2020-01-13
"""

from CostFunctions import CostFunctions
import numpy as np

__all__ = ['Mishra8']


class Mishra8(CostFunctions):
    """
    Implementation of the Mishra8.py function from 
    M. Jamil and X.-S. S. Yang, “A Literature Survey of Benchmark Functions For Global Optimization Problems,” Int. J. Math. Model. Numer. Optim., vol. 4, no. 2, p. 150, Aug. 2013.
    https://github.com/andyfaff/ampgo/blob/master/%20ampgo%20--username%20andrea.gavana%40gmail.com/go_benchmark.py
    """
    functionProperties = {
        'minimumValue': 0,
        'optimalArms': [[2, -3]],
        'searchSpace': [[-10, 10], [-10, 10]],
        'spaceType': ['uniform', 'uniform'],
        'x0': [np.random.uniform(-10, 10), np.random.uniform(-10, 10)],
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
        F1 = np.abs(x1 ** 10 - 20 * x1 ** 9 + 180 * x1 ** 8 - 960 * x1 ** 7 + 3360 * x1 ** 6 - 8064 * x1 ** 5 + 13340 * x1 ** 4 - 15360 * x1 ** 3 + 11520 * x1 ** 2 - 5120 * x1 + 2624)
        F2 = np.abs(x2 ** 4 + 12 * x2 ** 3 + 54 * x2 ** 2 + 108 * x2 + 81.0)
        value = 0.001 * (F1 + F2) ** 2
        return value