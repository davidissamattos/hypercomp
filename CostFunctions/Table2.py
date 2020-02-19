"""
Implementation of the Table2.py function

# Created by davidis at 2020-02-19
"""

from CostFunctions import CostFunctions
import numpy as np

__all__ = ['Table2']


class Table2(CostFunctions):
    """
    Implementation of the Table2.py function from 
    M. Jamil and X.-S. S. Yang, “A Literature Survey of Benchmark Functions For Global Optimization Problems,” Int. J. Math. Model. Numer. Optim., vol. 4, no. 2, p. 150, Aug. 2013.
    """
    functionProperties = {
        'minimumValue': -19.20850,
        'optimalArms': [[-8.055023472141116, -9.66459002890654],
                        [8.055023472141116, -9.66459002890654],
                        [-8.055023472141116, 9.66459002890654],
                        [8.055023472141116, 9.66459002890654]],
        'searchSpace': [[-10, 10], [-10, 10]],
        'spaceType': ['uniform', 'uniform'],
        'x0': [np.random.uniform(-10, 10), np.random.uniform(-10, 10)],
        'Continuous': 'Continuous',
        'Differentiability': 'Differentiable',
        'Separability': 'Separable',
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
        value = -np.abs(np.sin(x1)*np.cos(x2)*np.exp(np.abs(1-np.sqrt(x1**2+x2**2)/np.pi)))
        return value