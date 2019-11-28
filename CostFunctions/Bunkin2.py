"""
Implementation of the Bunkin2.py function

# Created by davidis at 2019-11-20
"""

from CostFunctions import CostFunctions
import numpy as np

__all__ = ['Bunkin2']


class Bunkin2(CostFunctions):
    """
    Implementation of the Bunkin2.py function from 
    M. Jamil and X.-S. S. Yang, “A Literature Survey of Benchmark Functions For Global Optimization Problems,” Int. J. Math. Model. Numer. Optim., vol. 4, no. 2, p. 150, Aug. 2013.
    """
    functionProperties = {
        'minimumValue': 0,
        'optimalArms': [[-10, 0]],
        'searchSpace': [[-15, -5], [-3, 3]],
        'spaceType': ['uniform', 'uniform'],
        'x0': [np.random.uniform(-15, -5), np.random.uniform(-3, 3)],
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
        value = 100*(x2-0.01*np.power(x1,2)+1) + 0.01*np.power(x1+10,2)
        return value