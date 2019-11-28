"""
Implementation of the Hartman3.py function

# Created by davidis at 2019-11-22
"""

from CostFunctions import CostFunctions
import numpy as np

__all__ = ['Hartman3']


class Hartman3(CostFunctions):
    """
    Implementation of the Hartman3.py function from 
    M. Jamil and X.-S. S. Yang, “A Literature Survey of Benchmark Functions For Global Optimization Problems,” Int. J. Math. Model. Numer. Optim., vol. 4, no. 2, p. 150, Aug. 2013.
    https://github.com/andyfaff/ampgo/blob/master/%20ampgo%20--username%20andrea.gavana%40gmail.com/go_benchmark.py
    """
    functionProperties = {
        'minimumValue': -3.86278214782076,
        'optimalArms': [[0.1, 0.55592003, 0.85218259]],
        'searchSpace': [[0, 1], [0, 1],[0, 1]],
        'spaceType': ['uniform', 'uniform', 'uniform'],
        'x0': [np.random.uniform(0, 1), np.random.uniform(0, 1),np.random.uniform(0, 1)],
        'Continuous': 'Continuous',
        'Differentiability': 'Differentiable',
        'Separability': 'Non-Separable',
        'Scalability': 'Non-Scalable',
        'Modality': 'Multimodal',
        'Ndimensions': 3
    }

    def func(self, x):
        """
        x is an array E.g.
        x1 = x[0]
        x2 = x[1]
        """
        a = np.array([[3.0, 0.1, 3.0, 0.1],
                     [10.0, 10.0, 10.0, 10.0],
                     [30.0, 35.0, 30.0, 35.0]])
        p = np.array([[0.36890, 0.46990, 0.10910, 0.03815],
                     [0.11700, 0.43870, 0.87320, 0.57430],
                     [0.26730, 0.74700, 0.55470, 0.88280]])
        c = np.array([1.0, 1.2, 3.0, 3.2])
        d = np.zeros_like(c)

        for i in range(4):
            d[i] = sum(a[:, i] * (x - p[:, i]) ** 2)

        return -sum(c * np.exp(-d))