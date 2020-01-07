"""
Implementation of the Corana.py function

# Created by davidis at 2019-11-22
"""

from CostFunctions import CostFunctions
import numpy as np

__all__ = ['Corana']


class Corana(CostFunctions):
    """
    Implementation of the Corana.py function from 
    M. Jamil and X.-S. S. Yang, “A Literature Survey of Benchmark Functions For Global Optimization Problems,” Int. J. Math. Model. Numer. Optim., vol. 4, no. 2, p. 150, Aug. 2013.
    https://www.al-roomi.org/benchmarks/unconstrained/4-dimensions/90-corana-s-function
    """
    functionProperties = {
        'minimumValue': 0,
        'optimalArms': [[0, 0, 0, 0]],
        'searchSpace': [[-500, 300], [-300, 500],[-500, 300],[-300, 500]],
        'spaceType': ['uniform', 'uniform','uniform','uniform'],
        'x0': [np.random.uniform(-500, 300), np.random.uniform(-300, 500),
               np.random.uniform(-500, 300),np.random.uniform(-300, 500)],
        'Continuous': 'Discontinuous',
        'Differentiability': 'Non-Differentiable',
        'Separability': 'Separable',
        'Scalability': 'Scalable',
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
        x = np.array(x)
        z =0.2* np.floor(np.abs(x/0.2)+ 0.49999)*np.sign(x)
        v = np.abs(x-z)
        d = np.array([1, 1000, 10, 100])
        A = 0.05

        value = 0
        for i in range(4):
            f1 = 0.15*np.power(z[i]-0.05*np.sign(z[i]), 2)*d[i]
            f2 = d[i]*np.power(x[i],2)
            if np.abs(v[i]) < A:
                value = value + f1
            else:
                value = value + f2

        return value