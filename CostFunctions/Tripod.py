"""
Implementation of the Tripod.py function

# Created by davidis at 2020-02-19
"""

from CostFunctions import CostFunctions
import numpy as np

__all__ = ['Tripod']


class Tripod(CostFunctions):
    """
    Implementation of the Tripod.py function from 
    M. Jamil and X.-S. S. Yang, “A Literature Survey of Benchmark Functions For Global Optimization Problems,” Int. J. Math. Model. Numer. Optim., vol. 4, no. 2, p. 150, Aug. 2013.
    """
    functionProperties = {
        'minimumValue': 0,
        'optimalArms': [[0, -50]],
        'searchSpace': [[-80, 100], [-100, 80]],
        'spaceType': ['uniform', 'uniform'],
        'x0': [np.random.uniform(-80, 100), np.random.uniform(-100, 80)],
        'Continuous': 'Discontinuous',
        'Differentiability': 'Non-Differentiable',
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
        p1 = np.float(x1 >= 0)
        p2 = np.float(x2 >= 0)
        value = p2*(1.0 + p1) + np.abs(x1 + 50.0*p2*(1.0-2.0*p1)) +\
                np.abs(x2 + 50.0*(1.0-2.0*p2))
        return value