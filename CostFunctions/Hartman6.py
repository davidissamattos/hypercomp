"""
Implementation of the Hartman6.py function

# Created by davidis at 2019-11-22
"""

from CostFunctions import CostFunctions
import numpy as np

__all__ = ['Hartman6']


class Hartman6(CostFunctions):
    """
    Implementation of the Hartman6.py function from 
    M. Jamil and X.-S. S. Yang, “A Literature Survey of Benchmark Functions For Global Optimization Problems,” Int. J. Math. Model. Numer. Optim., vol. 4, no. 2, p. 150, Aug. 2013.
    https://github.com/andyfaff/ampgo/blob/master/%20ampgo%20--username%20andrea.gavana%40gmail.com/go_benchmark.py
    """
    functionProperties = {
        'minimumValue': -3.32236801141551,
        'optimalArms': [[0.20168952, 0.15001069, 0.47687398, 0.27533243, 0.31165162, 0.65730054]],
        'searchSpace': [[0, 1],
                        [0, 1],
                        [0, 1],
                        [0, 1],
                        [0, 1],
                        [0, 1]],
        'spaceType': ['uniform', 'uniform','uniform','uniform','uniform','uniform'],
        'x0': [np.random.uniform(0, 1),
               np.random.uniform(0, 1),
               np.random.uniform(0, 1),
               np.random.uniform(0, 1),
               np.random.uniform(0, 1),
               np.random.uniform(0, 1)],
        'Continuous': 'Continuous',
        'Differentiability': 'Differentiable',
        'Separability': 'Non-Separable',
        'Scalability': 'Non-Scalable',
        'Modality': 'Multimodal',
        'Ndimensions': 6
    }

    def func(self, x):
        """
        x is an array E.g.
        x1 = x[0]
        x2 = x[1]
        """
        a = np.array([[10.00, 0.05, 3.00, 17.00],
                     [3.00, 10.00, 3.50, 8.00],
                     [17.00, 17.00, 1.70, 0.05],
                     [3.50, 0.10, 10.00, 10.00],
                     [1.70, 8.00, 17.00, 0.10],
                     [8.00, 14.00, 8.00, 14.00]])

        p = np.array([[0.1312, 0.2329, 0.2348, 0.4047],
                     [0.1696, 0.4135, 0.1451, 0.8828],
                     [0.5569, 0.8307, 0.3522, 0.8732],
                     [0.0124, 0.3736, 0.2883, 0.5743],
                     [0.8283, 0.1004, 0.3047, 0.1091],
                     [0.5886, 0.9991, 0.6650, 0.0381]])

        c = np.array([1.0, 1.2, 3.0, 3.2])
        d = np.zeros_like(c)

        for i in range(4):
            d[i] = np.sum(a[:, i] * (x - p[:, i]) ** 2)

        return -np.sum(c * np.exp(-d))
