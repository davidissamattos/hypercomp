"""
Implementation of the TesttubeHolder.py function

# Created by davidis at 2020-02-19
"""

from CostFunctions import CostFunctions
import numpy as np

__all__ = ['TesttubeHolder']


class TesttubeHolder(CostFunctions):
    """
    Implementation of the TesttubeHolder.py function from 
    M. Jamil and X.-S. S. Yang, “A Literature Survey of Benchmark Functions For Global Optimization Problems,” Int. J. Math. Model. Numer. Optim., vol. 4, no. 2, p. 150, Aug. 2013.
    """
    functionProperties = {
        'minimumValue': -10.872300,
        'optimalArms': [[np.pi/2, 0],
                        [-np.pi/2, 0]],
        'searchSpace': [[-10, 10], [-5, 10]],
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
        value = -4*np.abs(np.sin(x1)*np.cos(x2)*np.exp(np.abs(np.cos((x1**2 + x2**2)/200))))
        return value