"""
Implementation of the Cola.py function

# Created by davidis at 2019-11-22
"""

from CostFunctions import CostFunctions
import numpy as np

__all__ = ['Cola']


class Cola(CostFunctions):
    """
    Implementation of the Cola.py function from 
    M. Jamil and X.-S. S. Yang, “A Literature Survey of Benchmark Functions For Global Optimization Problems,” Int. J. Math. Model. Numer. Optim., vol. 4, no. 2, p. 150, Aug. 2013.
    https://github.com/andyfaff/ampgo/blob/master/%20ampgo%20--username%20andrea.gavana%40gmail.com/go_benchmark.py
    """
    functionProperties = {
        'minimumValue':11.7464,
        'optimalArms': [[0.651906, 1.30194, 0.099242, -0.883791, -0.8796,
                               0.204651, -3.28414, 0.851188, -3.46245, 2.53245, -0.895246,
                               1.40992, -3.07367, 1.96257, -2.97872, -0.807849, -1.68978]],
        'searchSpace': [[0, 4],
                        [-4, 4],
                        [-4, 4],
                        [-4, 4],
                        [-4, 4],
                        [-4, 4],
                        [-4, 4],
                        [-4, 4],
                        [-4, 4],
                        [-4, 4],
                        [-4, 4],
                        [-4, 4],
                        [-4, 4],
                        [-4, 4],
                        [-4, 4],
                        [-4, 4],
                        [-4, 4],
                        ],
        'spaceType': ['uniform', 'uniform','uniform','uniform','uniform','uniform','uniform','uniform','uniform','uniform','uniform','uniform','uniform','uniform','uniform','uniform','uniform'],
        'x0': [np.random.uniform(0, 4), np.random.uniform(-4, 4),
               np.random.uniform(-4, 4),np.random.uniform(-4, 4),
               np.random.uniform(-4, 4),np.random.uniform(-4, 4),
               np.random.uniform(-4, 4),np.random.uniform(-4, 4),
               np.random.uniform(-4, 4),np.random.uniform(-4, 4),
               np.random.uniform(-4, 4),np.random.uniform(-4, 4),
               np.random.uniform(-4, 4),np.random.uniform(-4, 4),
               np.random.uniform(-4, 4),np.random.uniform(-4, 4),
               np.random.uniform(-4, 4)],
        'Continuous': 'Continuous',
        'Differentiability': 'Differentiable',
        'Separability': 'Non-Separable',
        'Scalability': 'Non-Scalable',
        'Modality': 'Multimodal',
        'Ndimensions': 17
    }

    def func(self, x):
        """
        x is an array E.g.
        x1 = x[0]
        x2 = x[1]
        """
        d = np.array([[0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [1.27, 0, 0, 0, 0, 0, 0, 0, 0],
                     [1.69, 1.43, 0, 0, 0, 0, 0, 0, 0],
                     [2.04, 2.35, 2.43, 0, 0, 0, 0, 0, 0],
                     [3.09, 3.18, 3.26, 2.85, 0, 0, 0, 0, 0],
                     [3.20, 3.22, 3.27, 2.88, 1.55, 0, 0, 0, 0],
                     [2.86, 2.56, 2.58, 2.59, 3.12, 3.06, 0, 0, 0],
                     [3.17, 3.18, 3.18, 3.12, 1.31, 1.64, 3.00, 0, 0],
                     [3.21, 3.18, 3.18, 3.17, 1.70, 1.36, 2.95, 1.32, 0],
                     [2.38, 2.31, 2.42, 1.94, 2.85, 2.81, 2.56, 2.91, 2.97]])

        x1 = np.array([0.0, x[0]] + list(x[1::2]))
        x2 = np.array([0.0, 0.0] + list(x[2::2]))
        y = 0.0

        for i in range(1, len(x1)):
            y += sum((np.sqrt((x1[i] - x1[0:i]) ** 2.0 + (x2[i] - x2[0:i]) ** 2.0) - d[i, 0:i]) ** 2.0)
        return y