"""
Implementation of the Dolan.py function

# Created by davidis at 2019-11-22
"""

from CostFunctions import CostFunctions
import numpy as np

__all__ = ['Dolan']


class Dolan(CostFunctions):
    """
    Implementation of the Dolan.py function from 
    M. Jamil and X.-S. S. Yang, “A Literature Survey of Benchmark Functions For Global Optimization Problems,” Int. J. Math. Model. Numer. Optim., vol. 4, no. 2, p. 150, Aug. 2013.
        http://infinity77.net/global_optimization/test_functions_nd_D.html
    obal optimum: f(x_i) = 10^{-5} for \mathbf{x} = [8.39045925, 4.81424707, 7.34574133, 68.88246895, 3.85470806]
    """
    functionProperties = {
        'minimumValue': 1e-5,
        'optimalArms': [[8.39045925, 4.81424707, 7.34574133, 68.88246895, 3.85470806]],
        'searchSpace': [[-100, 100],
                        [-100, 100],
                        [-100, 100],
                        [-100, 100],
                        [-100, 100]],
        'spaceType': ['uniform', 'uniform','uniform','uniform','uniform'],
        'x0': [np.random.uniform(-100, 100),
               np.random.uniform(-100, 100),
               np.random.uniform(-100, 100),
               np.random.uniform(-100, 100),
               np.random.uniform(-100, 100)],
        'Continuous': 'Continuous',
        'Differentiability': 'Differentiable',
        'Separability': 'Non-Separable',
        'Scalability': 'Scalable',
        'Modality': 'Unimodal',
        'Ndimensions': 5
    }

    def func(self, x):
        """
        x is an array E.g.
        x1 = x[0]
        x2 = x[1]
        """
        x1 = x[0]
        x2 = x[1]
        x3 = x[2]
        x4 = x[3]
        x5 = x[4]
        value = np.abs((x1 + 1.7*x2)*np.sin(x1) - 1.5*x3 - 0.1*x4*np.cos(x4 + x5 - x1) + 0.2*np.power(x5,2.0) - x2 - 1.0)
        return value