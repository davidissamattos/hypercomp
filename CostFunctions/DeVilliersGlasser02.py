"""
Implementation of the DeVilliersGlasser02.py function

# Created by davidis at 2019-11-22
"""

from CostFunctions import CostFunctions
import numpy as np

__all__ = ['DeVilliersGlasser02']


class DeVilliersGlasser02(CostFunctions):
    """
    Implementation of the DeVilliersGlasser02.py function from
    M. Jamil and X.-S. S. Yang, “A Literature Survey of Benchmark Functions For Global Optimization Problems,” Int. J. Math. Model. Numer. Optim., vol. 4, no. 2, p. 150, Aug. 2013.
    http://infinity77.net/global_optimization/test_functions_nd_D.html
    """
    functionProperties = {
        'minimumValue': 0,
        'optimalArms': [[53.81, 1.27, 3.012, 2.13, 0.507]],
        'searchSpace': [[-500, 500],
                        [-500, 500],
                        [-500, 500],
                        [-500, 500],
                        [-500, 500]],
        'spaceType': ['uniform', 'uniform','uniform','uniform','uniform'],
        'x0': [np.random.uniform(-500, 500),
               np.random.uniform(-500, 500),
               np.random.uniform(-500, 500),
               np.random.uniform(-500, 500),
               np.random.uniform(-500, 500)],
        'Continuous': 'Continuous',
        'Differentiability': 'Differentiable',
        'Separability': 'Non-Separable',
        'Scalability': 'Non-Scalable',
        'Modality': 'Multimodal',
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
        value = 0
        for i in range(1,16+1):
            ti = 0.1 * (i-1)
            yi = 53.81 * np.power(1.27, ti) * np.tanh(3.012*ti + np.sin(2.13*ti))*np.cos(np.exp(0.507)*ti)
            value = value + np.power(x1*np.power(x2,ti)*np.tanh(x3*ti + np.sin(x4*ti))*np.cos(ti*np.exp(x5)) - yi,  2.0)

        return value