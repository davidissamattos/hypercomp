"""
Implementation of the Mishra4 function

# Created by davidis at 2020-01-10
"""

from CostFunctions import CostFunctions
import numpy as np

__all__ = ['Mishra4']


class Mishra4(CostFunctions):
    """
    Implementation of the Mishra4 function from
    M. Jamil and X.-S. S. Yang, “A Literature Survey of Benchmark Functions For Global Optimization Problems,” Int. J. Math. Model. Numer. Optim., vol. 4, no. 2, p. 150, Aug. 2013.
    https://www.al-roomi.org/benchmarks/unconstrained/2-dimensions/138-mishra-s-function-no-3
    """
    functionProperties = {
        'minimumValue': -0.199406970088833,
        'optimalArms': [[-9.941127263635860, -9.999571661999983]],
        'searchSpace': [[-10, 10], [-10, 10]],
        'spaceType': ['uniform', 'uniform'],
        'x0': [np.random.uniform(-10, 10), np.random.uniform(-10, 10)],
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
        value = np.sqrt(
            np.abs(
                np.sin(
                    np.sqrt(
                        np.abs(
                            x1*x1 + x2))))) +\
                0.01*(x1+x2)
        return value