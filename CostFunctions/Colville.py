"""
Implementation of the Colville.py function

# Created by davidis at 2019-11-20
"""

from CostFunctions import CostFunctions
import numpy as np

__all__ = ['Colville']


class Colville(CostFunctions):
    """
    Implementation of the Colville.py function from 
    M. Jamil and X.-S. S. Yang, “A Literature Survey of Benchmark Functions For Global Optimization Problems,” Int. J. Math. Model. Numer. Optim., vol. 4, no. 2, p. 150, Aug. 2013.
    """
    functionProperties = {
        'minimumValue': 0,
        'optimalArms': [[1, 1, 1, 1]],
        'searchSpace': [[-10, 10],
                        [-10, 10],
                        [-10, 10],
                        [-10, 10]],
        'spaceType': ['uniform', 'uniform', 'uniform', 'uniform'],
        'x0': [np.random.uniform(-10, 10), np.random.uniform(-10, 10),np.random.uniform(-10, 10),np.random.uniform(-10, 10)],
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
        If it depends on receiving a dimension you need to reimplement the __init__  and call
        the super and reimplement the function properties such as searchSpeace, spaceType, x0 etc...
        """
        x1 = x[0]
        x2 = x[1]
        x3 = x[2]
        x4 = x[3]
        value = 100*np.power(x1 - np.power(x2,2), 2) + np.power(1-x1, 2) + \
            90*np.power(x4-np.power(x3,2),2) + np.power(1-x3, 2) + \
            10.1 * (np.power(x2-1, 2) + np.power(x4-1, 2))  + \
            19.8*(x2-1)*(x4-1)
        return value