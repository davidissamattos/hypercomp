"""
Implementation of the Price3.py function

# Created by davidis at 2020-01-22
"""

from CostFunctions import CostFunctions
import numpy as np

__all__ = ['Price3']


class Price3(CostFunctions):
    """
    Implementation of the Price3.py function from 
    M. Jamil and X.-S. S. Yang, “A Literature Survey of Benchmark Functions For Global Optimization Problems,” Int. J. Math. Model. Numer. Optim., vol. 4, no. 2, p. 150, Aug. 2013.
    https://al-roomi.org/benchmarks/unconstrained/2-dimensions/160-price-s-function-no-3-modified-rosenbrock-s-or-price-rosenbrock-s-function
    """
    functionProperties = {
        'minimumValue': 0,
        'optimalArms': [[1, 1], [0.341307503353524,0.116490811845416]],
        'searchSpace': [[-10, 5], [-5, 10]],
        'spaceType': ['uniform', 'uniform'],
        'x0': [np.random.uniform(-10, 5), np.random.uniform(-10, 5)],
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
        value = (100 * (x[1] - x[0] ** 2) ** 2
                + (6.4 * (x[1] - 0.5) ** 2 - x[0] - 0.6) ** 2)
        return value