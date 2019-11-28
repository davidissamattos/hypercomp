"""
Implementation of the BiggsEXP6.py function

# Created by davidis at 2019-11-19
"""

from CostFunctions import CostFunctions
import numpy as np

__all__ = ['BiggsEXP6']


class BiggsEXP6(CostFunctions):
    """
    Implementation of the BiggsEXP5.py function from
    M. Jamil and X.-S. S. Yang, “A Literature Survey of Benchmark Functions For Global Optimization Problems,” Int. J. Math. Model. Numer. Optim., vol. 4, no. 2, p. 150, Aug. 2013.
    """
    functionProperties = {
        'minimumValue': 0,
        'optimalArms': [[1, 10, 1, 5, 4, 3]],
        'searchSpace': [[0, 20], [0, 20],[0, 20],[0, 20],[0, 20],[0, 20]],
        'spaceType': ['uniform', 'uniform','uniform','uniform','uniform','uniform'],
        'x0': [np.random.uniform(0,20),np.random.uniform(0,20),np.random.uniform(0,20),np.random.uniform(0,20),np.random.uniform(0,20),np.random.uniform(0,20)],
        'Continuous': 'Continuous',
        'Differentiability': 'Differentiable',
        'Separability': 'Non-Separable',
        'Scalability': 'Non-Scalable',
        'Modality': 'Multimodal',
        'Ndimensions': 6
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
        x4 = x[3]
        x5 = x[4]
        x6 = x[5]
        value = 0
        for i in range(14):
            ti =0.1*(i+1)
            yi = np.exp(-ti) - 5*np.exp(-10*ti) +3*np.exp(-4*ti)
            value = value + np.power((x3*np.exp(-ti*x1) - x4*np.exp(-ti*x2) +x6*np.exp(-ti*x5) - yi),2)
        return value