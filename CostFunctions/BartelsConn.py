"""
Implementation of the BartelsConn.py function

# Created by davidis at 2019-11-19
"""

from CostFunctions import CostFunctions
import numpy as np

__all__ = ['BartelsConn']


class BartelsConn(CostFunctions):
    """
    Implementation of the BartelsConn.py function from 
    M. Jamil and X.-S. S. Yang, “A Literature Survey of Benchmark Functions For Global Optimization Problems,” Int. J. Math. Model. Numer. Optim., vol. 4, no. 2, p. 150, Aug. 2013.
    """
    functionProperties = {
        'minimumValue': 1,
        'optimalArms': [[0, 0]],
        'searchSpace': [[-500, 300], [-300, 500]],
        'spaceType': ['uniform', 'uniform'],
        'x0': [np.random.uniform(-500,300),np.random.uniform(-300,500)],
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
        value = np.abs(x1**2 + x2**2 + x1*x2) + np.abs(np.sin(x1)) + np.abs(np.cos(x2))
        return value