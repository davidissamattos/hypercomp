"""
Implementation of the Bohachevsky1.py function

# Created by davidis at 2019-11-20
"""

from CostFunctions import CostFunctions
import numpy as np

__all__ = ['Bohachevsky1']


class Bohachevsky1(CostFunctions):
    """
    Implementation of the Bohachevsky1.py function from 
    M. Jamil and X.-S. S. Yang, “A Literature Survey of Benchmark Functions For Global Optimization Problems,” Int. J. Math. Model. Numer. Optim., vol. 4, no. 2, p. 150, Aug. 2013.
    """
    functionProperties = {
        'minimumValue': 0,
        'optimalArms': [[0, 0]],
        'searchSpace': [[-30, 100], [-100, 30]],
        'spaceType': ['uniform', 'uniform'],
        'x0': [np.random.uniform(-30, 100), np.random.uniform(-100, 30)],
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
        If it depends on receiving a dimension you need to reimplement the __init__  and call
        the super and reimplement the function properties such as searchSpeace, spaceType, x0 etc...
        """
        x1 = x[0]
        x2 = x[1]
        value = np.power(x1,2) + 2*np.power(x2,2) -0.3*np.cos(3*np.pi*x1)- 0.4*np.cos(4*np.pi*x2) +0.7
        return value