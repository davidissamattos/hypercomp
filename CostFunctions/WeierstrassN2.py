"""
Implementation of the WeierstrassN2.py function

# Created by davidis at 2020-02-24
"""

from CostFunctions import CostFunctions
import numpy as np

__all__ = ['WeierstrassN2']


class WeierstrassN2(CostFunctions):
    """
    Implementation of the WeierstrassN2.py function from 
    M. Jamil and X.-S. S. Yang, “A Literature Survey of Benchmark Functions For Global Optimization Problems,” Int. J. Math. Model. Numer. Optim., vol. 4, no. 2, p. 150, Aug. 2013.
    """
    functionProperties = {
        'minimumValue': 4.0,
        'optimalArms': [[0, 0]],
        'searchSpace': [[-0.3, 0.5], [-0.3, 0.5]],
        'spaceType': ['uniform', 'uniform'],
        'x0': [np.random.uniform(-0.3, 0.5), np.random.uniform(-0.3, 0.5)],
        'Continuous': 'Continuous',
        'Differentiability': 'Differentiable',
        'Separability': 'Separable',
        'Scalability': 'Scalable',
        'Modality': 'Multimodal',
        'Ndimensions': 2,
        'BBOB': 'True'
    }

    def func(self, x):
        """
        x is an array E.g.
        x1 = x[0]
        x2 = x[1]
        """
        kmax = 20
        a, b = 0.5, 3.0
        y = np.zeros((2,))

        ak = a ** (np.arange(0, kmax + 1))
        bk = b ** (np.arange(0, kmax + 1))
        for i in range(2):
            y[i] = np.sum(ak * np.cos(2 * np.pi * bk * (x[i] + 0.5))) -2 * np.sum(ak * np.cos(np.pi * bk))

        return np.sum(y)