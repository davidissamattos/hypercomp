"""
Implementation of the Bohachevsky2.py function

# Created by davidis at 2019-11-20
"""

from CostFunctions import CostFunctions
import numpy as np

__all__ = ['Bohachevsky2']


class Bohachevsky2(CostFunctions):
    """
    Implementation of the Bohachevsky2.py function from
    M. Jamil and X.-S. S. Yang, “A Literature Survey of Benchmark Functions For Global Optimization Problems,” Int. J. Math. Model. Numer. Optim., vol. 4, no. 2, p. 150, Aug. 2013.
    https://www.mathlayer.com/support/benchmark-problems-bohachevsky2.html
    """
    functionProperties = {
        'minimumValue': 0,
        'optimalArms': [[0, 0]],
        'searchSpace': [[-100, 30], [-30, 100]],
        'spaceType': ['uniform', 'uniform'],
        'x0': [np.random.uniform(-100, 30), np.random.uniform(-30, 100)],
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
        value = np.power(x1,2) + 2*np.power(x2,2) - 0.3*np.cos(3*np.pi*x1)*np.cos(4*np.pi*x2) +0.3
        return value