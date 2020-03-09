"""
Implementation of the WayburnSeader1.py function

# Created by davidis at 2020-02-19
"""

from CostFunctions import CostFunctions
import numpy as np

__all__ = ['WayburnSeader1']


class WayburnSeader1(CostFunctions):
    """
    Implementation of the WayburnSeader1.py function from 
    M. Jamil and X.-S. S. Yang, “A Literature Survey of Benchmark Functions For Global Optimization Problems,” Int. J. Math. Model. Numer. Optim., vol. 4, no. 2, p. 150, Aug. 2013.
    """
    functionProperties = {
        'minimumValue': 0,
        'optimalArms': [[1, 2], [1.596804153876933,0.806391692246134]],
        'searchSpace': [[-5, 5], [-5, 5]],
        'spaceType': ['uniform', 'uniform'],
        'x0': [np.random.uniform(-5, 5), np.random.uniform(-5, 5)],
        'Continuous': 'Continuous',
        'Differentiability': 'Differentiable',
        'Separability': 'Non-Separable',
        'Scalability': 'Scalable',
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
        value = (x1**6.0 + x2**4.0 - 17.0)**2.0 + (2*x1 + x2 - 4.0)**2.0
        return value