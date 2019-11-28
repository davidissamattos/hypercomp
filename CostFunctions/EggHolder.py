"""
Implementation of the EggHolder.py function

# Created by davidis at 2019-11-22
"""

from CostFunctions import CostFunctions
import numpy as np

__all__ = ['EggHolder']


class EggHolder(CostFunctions):
    """
    Implementation of the EggHolder.py function from 
    M. Jamil and X.-S. S. Yang, “A Literature Survey of Benchmark Functions For Global Optimization Problems,” Int. J. Math. Model. Numer. Optim., vol. 4, no. 2, p. 150, Aug. 2013.
    https://al-roomi.org/benchmarks/unconstrained/n-dimensions/187-egg-holder-function
    """
    functionProperties = {
        'minimumValue': -959.640662720850742,
        'optimalArms': [[512, 404.231805123817]],
        'searchSpace': [[-512, 512], [-512, 512]],
        'spaceType': ['uniform', 'uniform'],
        'x0': [np.random.uniform(-512, 512), np.random.uniform(-512, 512)],
        'Continuous': 'Continuous',
        'Differentiability': 'Differentiable',
        'Separability': 'Non-Separable',
        'Scalability': 'Scalable',
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
        value = -(x2 + 47)*np.sin(np.sqrt(np.abs(x2 + x1/2 +47))) - x1*np.sin(np.sqrt(np.abs(x1 - (x2+47))))
        return value