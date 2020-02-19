"""
Implementation of the Price4.py function

# Created by davidis at 2020-01-22
"""

from CostFunctions import CostFunctions
import numpy as np

__all__ = ['Price4']


class Price4(CostFunctions):
    """
    Implementation of the Price4.py function from 
    M. Jamil and X.-S. S. Yang, “A Literature Survey of Benchmark Functions For Global Optimization Problems,” Int. J. Math. Model. Numer. Optim., vol. 4, no. 2, p. 150, Aug. 2013.
    """
    functionProperties = {
        'minimumValue': 0,
        'optimalArms': [[0, 0],
                        [2,4],
                        [1.464,-2.506]],
        'searchSpace': [[-500, 100], [-100, 500]],
        'spaceType': ['uniform', 'uniform'],
        'x0': [np.random.uniform(-500, 100), np.random.uniform(-100, 500)],
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
        value = ((2.0 * x[1] * x[0] ** 3.0 - x[1] ** 3.0) ** 2.0
                + (6.0 * x[0] - x[1] ** 2.0 + x[1]) ** 2.0)
        return value