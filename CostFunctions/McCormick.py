"""
Implementation of the McCormick.py function

# Created by davidis at 2020-01-09
"""

from CostFunctions import CostFunctions
import numpy as np

__all__ = ['McCormick']


class McCormick(CostFunctions):
    """
    Implementation of the McCormick.py function from 
    M. Jamil and X.-S. S. Yang, “A Literature Survey of Benchmark Functions For Global Optimization Problems,” Int. J. Math. Model. Numer. Optim., vol. 4, no. 2, p. 150, Aug. 2013.
    """
    functionProperties = {
        'minimumValue': -1.9133,
        'optimalArms': [[-0.547, -1.547]],
        'searchSpace': [[-1.5, 4], [-3, 2]],
        'spaceType': ['uniform', 'uniform'],
        'x0': [np.random.uniform(-1.5, 4), np.random.uniform(-3, 2)],
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
        value = np.sin(x1 + x2) + np.power(x1-x2,2) -x1*3/2 +5*x2/2 +1
        return value