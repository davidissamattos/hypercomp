"""
Implementation of the Giunta.py function

# Created by davidis at 2019-11-22
"""

from CostFunctions import CostFunctions
import numpy as np

__all__ = ['Giunta']


class Giunta(CostFunctions):
    """
    Implementation of the Giunta.py function from 
    M. Jamil and X.-S. S. Yang, “A Literature Survey of Benchmark Functions For Global Optimization Problems,” Int. J. Math. Model. Numer. Optim., vol. 4, no. 2, p. 150, Aug. 2013.
    https://github.com/andyfaff/ampgo/blob/master/%20ampgo%20--username%20andrea.gavana%40gmail.com/go_benchmark.py
    """
    functionProperties = {
        'minimumValue': 0.06447042053690566,
        'optimalArms': [[0.4673200277395354, 0.4673200169591304]],
        'searchSpace': [[-1, 1], [-1, 1]],
        'spaceType': ['uniform', 'uniform'],
        'x0': [np.random.uniform(-1, 1), np.random.uniform(-1, 1)],
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
        value = 0.6 + \
            np.sin(x1*16/15 - 1) + np.power(np.sin(x1*16/15 - 1) ,2) + (1/50)*np.sin(4*(x1*16/15 -1)) + \
            np.sin(x2 * 16 / 15 - 1) + np.power(np.sin(x2 * 16 / 15 - 1), 2) + (1 / 50) * np.sin(4 * (x2 * 16 / 15 - 1))
        return value