"""
Implementation of the Keane.py function

# Created by davidis at 2020-01-07
"""

from CostFunctions import CostFunctions
import numpy as np

__all__ = ['Keane']


class Keane(CostFunctions):
    """
    Implementation of the Keane.py function from 
    M. Jamil and X.-S. S. Yang, “A Literature Survey of Benchmark Functions For Global Optimization Problems,” Int. J. Math. Model. Numer. Optim., vol. 4, no. 2, p. 150, Aug. 2013.
    https://github.com/andyfaff/ampgo/blob/master/%20ampgo%20--username%20andrea.gavana%40gmail.com/go_benchmark.py
    """
    functionProperties = {
        'minimumValue': 0.673668,
        'optimalArms': [[0, 1.39325],[1.39325,0]],
        'searchSpace': [[0, 10], [0, 10]],
        'spaceType': ['uniform', 'uniform'],
        'x0': [np.random.uniform(0, 10), np.random.uniform(0, 10)],
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
        value = (np.sin(x1 - x2)**2.0*np.sin(x1 + x2)**2.0)/np.sqrt(x1**2.0 + x2**2.0)
        return value