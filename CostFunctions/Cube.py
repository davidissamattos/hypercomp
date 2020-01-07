"""
Implementation of the Cube.py function

# Created by davidis at 2019-11-22
"""

from CostFunctions import CostFunctions
import numpy as np

__all__ = ['Cube']


class Cube(CostFunctions):
    """
    Implementation of the Cube.py function from 
    M. Jamil and X.-S. S. Yang, “A Literature Survey of Benchmark Functions For Global Optimization Problems,” Int. J. Math. Model. Numer. Optim., vol. 4, no. 2, p. 150, Aug. 2013.
    https://www.al-roomi.org/benchmarks/unconstrained/2-dimensions/119-cube-function
    """
    functionProperties = {
        'minimumValue': 0,
        'optimalArms': [[1, 1]],
        'searchSpace': [[-10, 4], [-4, 10]],
        'spaceType': ['uniform', 'uniform'],
        'x0': [np.random.uniform(-10, 4), np.random.uniform(-4, 10)],
        'Continuous': 'Continuous',
        'Differentiability': 'Differentiable',
        'Separability': 'Non-Separable',
        'Scalability': 'Non-Scalable',
        'Modality': 'Unimodal',
        'Ndimensions': 2
    }

    def func(self, x):
        x1 = x[0]
        x2 = x[1]
        value = 100*np.power(x2- np.power(x1,3) ,2) +np.power(1-x1,2)
        return value