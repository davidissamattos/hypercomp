"""
Implementation of the DeVilliersGlasser01.py function

# Created by davidis at 2019-11-22
"""

from CostFunctions import CostFunctions
import numpy as np

__all__ = ['DeVilliersGlasser01']


class DeVilliersGlasser01(CostFunctions):
    """
    Implementation of the DeVilliersGlasser01.py function from 
    M. Jamil and X.-S. S. Yang, “A Literature Survey of Benchmark Functions For Global Optimization Problems,” Int. J. Math. Model. Numer. Optim., vol. 4, no. 2, p. 150, Aug. 2013.
    http://infinity77.net/global_optimization/test_functions_nd_D.html
    """
    functionProperties = {
        'minimumValue': 0,
        'optimalArms': [[60.137, 1.371, 3.112, 1.761]],
        'searchSpace': [[-500, 500],
                        [-500, 500],
                        [-500, 500],
                        [-500, 500]],
        'spaceType': ['uniform', 'uniform','uniform','uniform'],
        'x0': [np.random.uniform(-500, 500),
               np.random.uniform(-500, 500),
               np.random.uniform(-500, 500),
               np.random.uniform(-500, 500)],
        'Continuous': 'Continuous',
        'Differentiability': 'Differentiable',
        'Separability': 'Non-Separable',
        'Scalability': 'Non-Scalable',
        'Modality': 'Multimodal',
        'Ndimensions': 4
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
        value = 0
        for i in range(1,24+1):
            ti = 0.1 * (i-1)
            yi = 60.137 * np.power(1.371, ti) * np.sin(3.112*ti + 1.761)
            value = value + np.power(x1*np.power(x2,ti)*np.sin(x3*ti + x4) - yi,  2.0)
        return value