"""
Implementation of the Chichinadze.py function

# Created by davidis at 2019-11-20
"""

from CostFunctions import CostFunctions
import numpy as np

__all__ = ['Chichinadze']


class Chichinadze(CostFunctions):
    """
    Implementation of the Chichinadze.py function from 
    M. Jamil and X.-S. S. Yang, “A Literature Survey of Benchmark Functions For Global Optimization Problems,” Int. J. Math. Model. Numer. Optim., vol. 4, no. 2, p. 150, Aug. 2013.
    https://al-roomi.org/benchmarks/unconstrained/2-dimensions/42-chichinadze-s-function
    """
    functionProperties = {
        'minimumValue': -42.94438701899098,
        'optimalArms': [[6.189866586965680, 0.5]],
        'searchSpace': [[-30, 30], [-30, 30]],
        'spaceType': ['uniform', 'uniform'],
        'x0': [np.random.uniform(-30, 30), np.random.uniform(-30, 30)],
        'Continuous': 'Continuous',
        'Differentiability': 'Differentiable',
        'Separability': 'Separable',
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
        value = np.power(x1,2) - 12*x1 + 11 \
                + 10*np.cos(np.pi*x1/2) + 8* np.sin(5*np.pi*x1/2) \
                - np.sqrt(1/5)*np.exp(-0.5*np.power(x2-0.5,2))
        return value