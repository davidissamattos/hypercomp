"""
Implementation of the WayburnSeader3.py function

# Created by davidis at 2020-02-19
"""

from CostFunctions import CostFunctions
import numpy as np

__all__ = ['WayburnSeader3']


class WayburnSeader3(CostFunctions):
    """
    Implementation of the WayburnSeader3.py function from 
    M. Jamil and X.-S. S. Yang, “A Literature Survey of Benchmark Functions For Global Optimization Problems,” Int. J. Math. Model. Numer. Optim., vol. 4, no. 2, p. 150, Aug. 2013.

    Corrected from https://al-roomi.org/benchmarks/unconstrained/2-dimensions/279-wayburn-seader-s-function-no-03
    """
    functionProperties = {
        'minimumValue': 19.105879794567979,
        'optimalArms': [[5.146896745324582, 6.839589743000071] ],
        'searchSpace': [[-10, 10], [-10, 10]],
        'spaceType': ['uniform', 'uniform'],
        'x0': [np.random.uniform(-10, 10), np.random.uniform(-10, 10)],
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
        value = (2/3)*x1**3 -8*x1**2 +33*x1 -x1*x2 +5 +\
                ((x1-4)**2 + (x2-5)**2 - 4)**2
        return value