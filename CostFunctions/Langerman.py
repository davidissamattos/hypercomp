"""
Implementation of the Langerman.py function

# Created by davidis at 2020-01-07
"""

from CostFunctions import CostFunctions
import numpy as np

__all__ = ['Langerman']


class Langerman(CostFunctions):
    """
    Implementation of the Langerman.py function from 
    https://github.com/andyfaff/ampgo/blob/master/%20ampgo%20--username%20andrea.gavana%40gmail.com/go_benchmark.py
    """
    functionProperties = {
        'minimumValue': -5.1621259,
        'optimalArms': [[2.00299219, 1.006096]],
        'searchSpace': [[0, 10], [0, 10]],
        'spaceType': ['uniform', 'uniform'],
        'x0': [np.random.uniform(0, 10), np.random.uniform(0, 10)],
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

        a = [3, 5, 2, 1, 7]
        b = [5, 2, 1, 4, 9]
        c = [1, 2, 5, 2, 3]

        value = -np.sum(c*np.exp(-(1/np.pi)*((x[0]-a)**2 + (x[1]-b)**2))*np.cos(np.pi*((x[0]-a)**2 + (x[1]-b)**2)))
        return value