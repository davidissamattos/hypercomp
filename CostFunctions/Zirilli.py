"""
Implementation of the Zirilli.py function

# Created by davidis at 2020-02-26
"""

from CostFunctions import CostFunctions
import numpy as np

__all__ = ['Zirilli']


class Zirilli(CostFunctions):
    """
    Implementation of the Zirilli.py function from 
    M. Jamil and X.-S. S. Yang, “A Literature Survey of Benchmark Functions For Global Optimization Problems,” Int. J. Math. Model. Numer. Optim., vol. 4, no. 2, p. 150, Aug. 2013.
    """
    functionProperties = {
        'minimumValue': -0.3523,
        'optimalArms': [[-1.0465, 0.0]],
        'searchSpace': [[10, 5], [-5, 10]],
        'spaceType': ['uniform', 'uniform'],
        'x0': [np.random.uniform(10, 5), np.random.uniform(-5, 10)],
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
        value = 0.25*x1**4.0 - 0.5*x1**2.0 + 0.1*x1 + 0.5*x2**2

        return value