"""
Implementation of the Ackley3 function

# Created by davidis at 2019-11-19
"""

from CostFunctions import CostFunctions
import numpy as np

__all__ = ['Ackley3']


class Ackley3(CostFunctions):
    """
    Implementation of the Ackley3 function]
    M. Jamil and X.-S. S. Yang, “A Literature Survey of Benchmark Functions For Global Optimization Problems,” Int. J. Math. Model. Numer. Optim., vol. 4, no. 2, p. 150, Aug. 2013.
    This function is wrongly specified in the paper in terms of minimun
    """
    functionProperties = {
        'minimumValue': -219.1418,
        'optimalArms': [[0, 0.402465]],
        'searchSpace': [[-32, 20], [-20, 32]],
        'spaceType': ['uniform', 'uniform'],
        'x0': [np.random.uniform(-32, 202),np.random.uniform(-20, 32)],
        'Continuous': 'Continuous',
        'Differentiability': 'Differentiable',
        'Separability': 'Non-Separable',
        'Scalability': 'Non-Scalable',
        'Modality': 'Unimodal',
        'Ndimensions': 2
    }

    def func(self, x):
        """
        x is an array E.g.
        x1 = x[0]
        x2 = x[1]
        If it depends on receiving a dimension you need to re implement the __init__  and call
        the super and re implement the function properties such as searchSpeace, spaceType, x0 etc...
        """
        x1 = x[0]
        x2 = x[1]
        value = -200*np.exp(-0.2*np.sqrt(x1**2 + x2**2)) \
                -5*np.exp(np.cos(3*x1)+np.sin(3*x2))
        return value