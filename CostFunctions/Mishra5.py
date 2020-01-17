"""
Implementation of the Mishra5.py function

# Created by davidis at 2020-01-10
"""

from CostFunctions import CostFunctions
import numpy as np

__all__ = ['Mishra5']


class Mishra5(CostFunctions):
    """
    Implementation of the Mishra5.py function from 
    M. Jamil and X.-S. S. Yang, “A Literature Survey of Benchmark Functions For Global Optimization Problems,” Int. J. Math. Model. Numer. Optim., vol. 4, no. 2, p. 150, Aug. 2013.
   https://github.com/andyfaff/ampgo/blob/master/%20ampgo%20--username%20andrea.gavana%40gmail.com/go_benchmark.py
    """
    functionProperties = {
        'minimumValue': -0.119829,
        'optimalArms': [[-1.98682, -10.0]],
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
        value = np.power((np.sin((np.cos(x1) + np.cos(x2))**2.0)**2.0) +\
                 (np.cos((np.sin(x1) + np.sin(x2))**2.0)**2.0) + x1, 2.0) +\
                0.01*(x1 + x2)
        return value