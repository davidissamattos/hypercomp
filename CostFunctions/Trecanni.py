"""
Implementation of the Trecanni.py function

# Created by davidis at 2020-02-19
"""

from CostFunctions import CostFunctions
import numpy as np

__all__ = ['Trecanni']


class Trecanni(CostFunctions):
    """
    Implementation of the Trecanni.py function from 
    M. Jamil and X.-S. S. Yang, “A Literature Survey of Benchmark Functions For Global Optimization Problems,” Int. J. Math. Model. Numer. Optim., vol. 4, no. 2, p. 150, Aug. 2013.
    """
    functionProperties = {
        'minimumValue': 0,
        'optimalArms': [[0, 0],[-2, 0]],
        'searchSpace': [[-5, 10], [-5, 10]],
        'spaceType': ['uniform', 'uniform'],
        'x0': [np.random.uniform(-5, 10), np.random.uniform(-5, 10)],
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
        value = x1**4 - 4*x1**3 + 4*x1 +x2**2
        return value