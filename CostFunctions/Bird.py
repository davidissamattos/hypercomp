"""
Implementation of the Bird.py function

# Created by davidis at 2019-11-19
"""

from CostFunctions import CostFunctions
import numpy as np

__all__ = ['Bird']


class Bird(CostFunctions):
    """
    Implementation of the Bird.py function from 
    M. Jamil and X.-S. S. Yang, “A Literature Survey of Benchmark Functions For Global Optimization Problems,” Int. J. Math. Model. Numer. Optim., vol. 4, no. 2, p. 150, Aug. 2013.
    """
    functionProperties = {
        'minimumValue': -106.764537,
        'optimalArms': [[4.70104,3.15294], [-1.58214, -3.13024]],
        'searchSpace': [[-2*np.pi, 2*np.pi], [-2*np.pi, 2*np.pi]],
        'spaceType': ['uniform', 'uniform'],
        'x0': [np.random.uniform(-2*np.pi,2*np.pi),np.random.uniform(-2*np.pi,2*np.pi)],
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
        value = np.sin(x1)*np.exp(np.power(1-np.cos(x2),2)) + np.cos(x2)*np.exp(np.power(1-np.sin(x1),2)) + np.power(x1-x2,2)
        return value