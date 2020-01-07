"""
Implementation of the HelicalValley.py function

# Created by davidis at 2019-11-22
"""

from CostFunctions import CostFunctions
import numpy as np

__all__ = ['HelicalValley']


class HelicalValley(CostFunctions):
    """
    Implementation of the HelicalValley.py function from 
    M. Jamil and X.-S. S. Yang, “A Literature Survey of Benchmark Functions For Global Optimization Problems,” Int. J. Math. Model. Numer. Optim., vol. 4, no. 2, p. 150, Aug. 2013.
    https://github.com/andyfaff/ampgo/blob/master/%20ampgo%20--username%20andrea.gavana%40gmail.com/go_benchmark.py
    """
    functionProperties = {
        'minimumValue': 0,
        'optimalArms': [[1.0, 0.0, 0.0]],
        'searchSpace': [[-10, 6], [-10, 5],[-5, 10]],
        'spaceType': ['uniform', 'uniform', 'uniform'],
        'x0': [np.random.uniform(-10, 6), np.random.uniform(-10, 5),np.random.uniform(-5, 10)],
        'Continuous': 'Continuous',
        'Differentiability': 'Differentiable',
        'Separability': 'Non-Separable',
        'Scalability': 'Scalable',
        'Modality': 'Multimodal',
        'Ndimensions': 3
    }

    def func(self, x):
        """
        x is an array E.g.
        x1 = x[0]
        x2 = x[1]
        """
        value = 100*((x[2] - 10*np.arctan2(x[1], x[0])/2/np.pi)**2 + (np.sqrt(x[0]**2 + x[1]**2) - 1)**2) + x[2]**2
        return value