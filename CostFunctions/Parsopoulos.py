"""
Implementation of the Parsopoulos.py function

# Created by davidis at 2020-01-22
"""

from CostFunctions import CostFunctions
import numpy as np

__all__ = ['Parsopoulos']


class Parsopoulos(CostFunctions):
    """
    Implementation of the Parsopoulos.py function from 
    M. Jamil and X.-S. S. Yang, “A Literature Survey of Benchmark Functions For Global Optimization Problems,” Int. J. Math. Model. Numer. Optim., vol. 4, no. 2, p. 150, Aug. 2013.
    """
    functionProperties = {
        'minimumValue': 0,
        'optimalArms': [[1*np.pi/2, 0* np.pi],
                        [-1*np.pi/2,0* np.pi],
                        [1*np.pi/2, 1*np.pi],
                        [-1*np.pi/2, 1*np.pi],
                        [1*np.pi/2, -1*np.pi],
                        [-1*np.pi/2, -1*np.pi],
                        [3 * np.pi / 2, 0 * np.pi],
                        [-3 * np.pi / 2, 0 * np.pi],
                        [3 * np.pi / 2, 1 * np.pi],
                        [-3 * np.pi / 2, 1 * np.pi],
                        [3 * np.pi / 2, -1 * np.pi],
                        [-3 * np.pi / 2, -1 * np.pi]],
        'searchSpace': [[-5, 5], [-5, 5]],
        'spaceType': ['uniform', 'uniform'],
        'x0': [np.random.uniform(-5, 5), np.random.uniform(-5, 5)],
        'Continuous': 'Continuous',
        'Differentiability': 'Differentiable',
        'Separability': 'Separable',
        'Scalability': 'Scalable',
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
        value = np.cos(x1)**2.0 + np.sin(x2)**2.0
        return value