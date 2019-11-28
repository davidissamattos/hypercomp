"""
Implementation of the BiggsEXP3.py function

# Created by davidis at 2019-11-19
"""

from CostFunctions import CostFunctions
import numpy as np

__all__ = ['BiggsEXP3']


class BiggsEXP3(CostFunctions):
    """
    Implementation of the BiggsEXP3.py function from
    M. Jamil and X.-S. S. Yang, “A Literature Survey of Benchmark Functions For Global Optimization Problems,” Int. J. Math. Model. Numer. Optim., vol. 4, no. 2, p. 150, Aug. 2013.
      Note: function is wrong in the paper yi= exp(-ti) -5exp(-10ti)
    """
    functionProperties = {
        'minimumValue': 0,
        'optimalArms': [[1, 10, 5]],
        'searchSpace': [[0, 20], [0, 20], [0, 20]],
        'spaceType': ['uniform', 'uniform','uniform'],
        'x0': [np.random.uniform(0,20),np.random.uniform(0,20),np.random.uniform(0,20)],
        'Continuous': 'Continuous',
        'Differentiability': 'Differentiable',
        'Separability': 'Non-Separable',
        'Scalability': 'Non-Scalable',
        'Modality': 'Multimodal',
        'Ndimensions': 3
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
        x3 = x[2]
        value = 0
        for i in range(11):
            ti =0.1*(i+1)
            yi = np.exp(-ti) - 5*np.exp(-10*ti)
            value = value + np.power((np.exp(-ti*x1) - x3*np.exp(-ti*x2) - yi),2)
        return value