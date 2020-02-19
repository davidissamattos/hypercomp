"""
Implementation of the Scahffer3.py function

# Created by davidis at 2020-02-13
"""

from CostFunctions import CostFunctions
import numpy as np

__all__ = ['Scahffer3']


class Scahffer3(CostFunctions):
    """
    Implementation of the Scahffer3.py function from
    M. Jamil and X.-S. S. Yang, “A Literature Survey of Benchmark Functions For Global Optimization Problems,” Int. J. Math. Model. Numer. Optim., vol. 4, no. 2, p. 150, Aug. 2013.
    """
    functionProperties = {
        'minimumValue': 0.00156685,
        'optimalArms': [[0, 1.253115]],
        'searchSpace': [[-100, 150], [-50, 100]],
        'spaceType': ['uniform', 'uniform'],
        'x0': [np.random.uniform(-100, 50), np.random.uniform(-50, 100)],
        'Continuous': 'Continuous',
        'Differentiability': 'Differentiable',
        'Separability': 'Non-Separable',
        'Scalability': 'Non-Scalable',
        'Modality': 'Unimodal',
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
        value = 0.5 + (np.sin(np.cos(np.abs(x1**2.0 - x2**2.0)))**2.0 - 0.5)/(1 + 0.001*(x1**2.0 + x2**2.0)**2.0)
        return value