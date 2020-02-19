"""
Implementation of the VenterSobiezcczanskiSobieski.py function

# Created by davidis at 2020-02-19
"""

from CostFunctions import CostFunctions
import numpy as np

__all__ = ['VenterSobiezcczanskiSobieski']


class VenterSobiezcczanskiSobieski(CostFunctions):
    """
    Implementation of the VenterSobiezcczanskiSobieski.py function from 
    M. Jamil and X.-S. S. Yang, “A Literature Survey of Benchmark Functions For Global Optimization Problems,” Int. J. Math. Model. Numer. Optim., vol. 4, no. 2, p. 150, Aug. 2013.
    """
    functionProperties = {
        'minimumValue': -400,
        'optimalArms': [[0, 0]],
        'searchSpace': [[-50, 10], [-10, 50]],
        'spaceType': ['uniform', 'uniform'],
        'x0': [np.random.uniform(-50, 10), np.random.uniform(-10, 50)],
        'Continuous': 'Continuous',
        'Differentiability': 'Differentiable',
        'Separability': 'Separable',
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
        value = x1**2.0 - 100.0*np.cos(x1)**2.0 - \
                100.0*np.cos(x1**2.0/30.0) + x2**2.0 - \
                100.0*np.cos(x2)**2.0 - 100.0*np.cos(x2**2.0/30.0)

        return value