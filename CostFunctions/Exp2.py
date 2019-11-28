"""
Implementation of the Exp2.py function

# Created by davidis at 2019-11-22
"""

from CostFunctions import CostFunctions
import numpy as np

__all__ = ['Exp2']


class Exp2(CostFunctions):
    """
    Implementation of the Exp2.py function from 
    M. Jamil and X.-S. S. Yang, “A Literature Survey of Benchmark Functions For Global Optimization Problems,” Int. J. Math. Model. Numer. Optim., vol. 4, no. 2, p. 150, Aug. 2013.
    """
    functionProperties = {
        'minimumValue': 0,
        'optimalArms': [[1, 10]],
        'searchSpace': [[0, 20], [0, 20]],
        'spaceType': ['uniform', 'uniform'],
        'x0': [np.random.uniform(0, 20), np.random.uniform(0, 20)],
        'Continuous': '-',
        'Differentiability': '-',
        'Separability': 'Separable',
        'Scalability': '-',
        'Modality': '-',
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
        i = np.arange(0,10)
        f = np.power(np.exp(-i*x1/10) - 5*np.exp(-i*x2/10) - np.exp(-i/10) + 5*np.exp(-i) ,2)
        value = np.sum(f)
        return value