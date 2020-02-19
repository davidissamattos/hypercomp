"""
Implementation of the Table3.py function

# Created by davidis at 2020-02-19
"""

from CostFunctions import CostFunctions
import numpy as np

__all__ = ['Table3']


class Table3(CostFunctions):
    """
    Implementation of the Table3.py function from 
    M. Jamil and X.-S. S. Yang, “A Literature Survey of Benchmark Functions For Global Optimization Problems,” Int. J. Math. Model. Numer. Optim., vol. 4, no. 2, p. 150, Aug. 2013.
    """
    functionProperties = {
        'minimumValue': -24.1568155,
        'optimalArms': [[-9.646157266348881, -9.646134286497169],
                        [9.646157266348881, -9.646134286497169],
                        [-9.646157266348881, 9.646134286497169],
                        [9.646157266348881, 9.646134286497169]],
        'searchSpace': [[-10, 10], [-10, 10]],
        'spaceType': ['uniform', 'uniform'],
        'x0': [np.random.uniform(-10, 10), np.random.uniform(-10, 10)],
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
        value = -((np.cos(x1)*np.cos(x2)*np.exp(np.abs(1-np.sqrt(x1**2+x2**2)/(np.pi)))))**2 /30
        return value