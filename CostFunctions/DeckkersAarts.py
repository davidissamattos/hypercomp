"""
Implementation of the DeckkersAarts.py function

# Created by davidis at 2019-11-22
"""

from CostFunctions import CostFunctions
import numpy as np

__all__ = ['DeckkersAarts']


class DeckkersAarts(CostFunctions):
    """
    Implementation of the DeckkersAarts.py function from 
    M. Jamil and X.-S. S. Yang, “A Literature Survey of Benchmark Functions For Global Optimization Problems,” Int. J. Math. Model. Numer. Optim., vol. 4, no. 2, p. 150, Aug. 2013.
    Although all references indicate the same thing
    Implementation says otherwise
    """
    functionProperties = {
        'minimumValue': -24771.093749999996,
        'optimalArms': [[0, 15],[0, -15]],
        'searchSpace': [[-20, 20], [-20, 20]],
        'spaceType': ['uniform', 'uniform'],
        'x0': [np.random.uniform(-20, 20), np.random.uniform(-20, 20)],
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
        x1 = x[0]
        x2 = x[1]
        # value = 1e5*x1**2.0 + x2**2.0 - (x1**2.0 + x2**2.0)**2.0 + 1e-5*(x1**2.0 + x2**2.0)**4.0
        value = 1e5*np.power(x1,2.0) \
                + np.power(x2,2.0) \
                -np.power(np.power(x1,2.0)+np.power(x2,2.0),2.0) \
                + 1e-5*np.power(np.power(x1,2.0)+np.power(x2,2.0) ,4.0)
        return value