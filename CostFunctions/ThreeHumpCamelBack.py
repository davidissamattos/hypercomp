"""
Implementation of the ThreeHumpCamelBack.py function

# Created by davidis at 2019-11-20
"""

from CostFunctions import CostFunctions
import numpy as np

__all__ = ['ThreeHumpCamelBack']


class ThreeHumpCamelBack(CostFunctions):
    """
    Implementation of the ThreeHumpCamelBack.py function from 
    M. Jamil and X.-S. S. Yang, “A Literature Survey of Benchmark Functions For Global Optimization Problems,” Int. J. Math. Model. Numer. Optim., vol. 4, no. 2, p. 150, Aug. 2013.
    """
    functionProperties = {
        'minimumValue': 0,
        'optimalArms': [[0, 0]],
        'searchSpace': [[-5, 2], [-2, 5]],
        'spaceType': ['uniform', 'uniform'],
        'x0': [np.random.uniform(-5,2), np.random.uniform(-2,5)],
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
        value = x1 * x2
        return value