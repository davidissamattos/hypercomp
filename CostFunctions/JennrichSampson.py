"""
Implementation of the JennrichSampson.py function

# Created by davidis at 2020-01-07
"""

from CostFunctions import CostFunctions
import numpy as np

__all__ = ['JennrichSampson']


class JennrichSampson(CostFunctions):
    """
    Implementation of the JennrichSampson.py function from 
    M. Jamil and X.-S. S. Yang, “A Literature Survey of Benchmark Functions For Global Optimization Problems,” Int. J. Math. Model. Numer. Optim., vol. 4, no. 2, p. 150, Aug. 2013.
    """
    functionProperties = {
        'minimumValue': 124.3621824,
        'optimalArms': [[0.257825, 0.257825]],
        'searchSpace': [[-1, 1], [-1, 1]],
        'spaceType': ['uniform', 'uniform'],
        'x0': [np.random.uniform(-1, 1), np.random.uniform(-1, 1)],
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
        rng = np.arange(1.0, 11.0) #from 1 to 10 list
        value = np.sum(np.power(2 + 2*rng -(np.exp(rng*x1)+np.exp(rng*x2)),2))
        return value