"""
Implementation of the Shekel5.py function

# Created by davidis at 2020-02-14
"""

from CostFunctions import CostFunctions
import numpy as np

__all__ = ['Shekel5']


class Shekel5(CostFunctions):
    """
    Implementation of the Shekel5.py function from 
    M. Jamil and X.-S. S. Yang, “A Literature Survey of Benchmark Functions For Global Optimization Problems,” Int. J. Math. Model. Numer. Optim., vol. 4, no. 2, p. 150, Aug. 2013.
    """
    functionProperties = {
        'minimumValue': -10.1527,
        'optimalArms': [[4,
                         4,
                         4,
                         4]],
        'searchSpace': [[0, 10],
                        [0, 10],
                        [0, 10],
                        [0, 10]],
        'spaceType': ['uniform', 'uniform','uniform','uniform'],
        'x0': [np.random.uniform(0, 10),
               np.random.uniform(0, 10),
               np.random.uniform(0, 10),
               np.random.uniform(0, 10)],
        'Continuous': 'Continuous',
        'Differentiability': 'Differentiable',
        'Separability': 'Non-Separable',
        'Scalability': 'Scalable',
        'Modality': 'Multimodal',
        'Ndimensions': 4
    }

    def func(self, x):
        """
        x is an array E.g.
        x1 = x[0]
        x2 = x[1]
        """
        A = np.asarray([[4.0, 4.0, 4.0, 4.0],
                     [1.0, 1.0, 1.0, 1.0],
                     [8.0, 8.0, 8.0, 8.0],
                     [6.0, 6.0, 6.0, 6.0],
                     [3.0, 7.0, 3.0, 7.0]])

        C = np.asarray([0.1, 0.2, 0.2, 0.4, 0.6])

        sum1 = 0
        for a, c in zip(A, C):
            sum1 = sum1 + - np.sum((1.0 / (np.dot(x - a, x - a) + c)) )
        return sum1