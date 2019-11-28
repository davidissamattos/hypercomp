"""
Implementation of the GulfResearch.py function

# Created by davidis at 2019-11-22
"""

from CostFunctions import CostFunctions
import numpy as np

__all__ = ['GulfResearch']


class GulfResearch(CostFunctions):
    """
    Implementation of the GulfResearch.py function from 
    M. Jamil and X.-S. S. Yang, “A Literature Survey of Benchmark Functions For Global Optimization Problems,” Int. J. Math. Model. Numer. Optim., vol. 4, no. 2, p. 150, Aug. 2013.
    """
    functionProperties = {
        'minimumValue': 0,
        'optimalArms': [[50, 25, 1.5]],
        'searchSpace': [[0.1, 100], [0, 25.6], [0, 5]],
        'spaceType': ['uniform', 'uniform','uniform'],
        'x0': [np.random.uniform(0.1, 100), np.random.uniform(0, 25.6), np.random.uniform(0, 5)],
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
        """
        x1 = x[0]
        x2 = x[1]
        x3 = x[2]
        i = np.arange(1,100)
        ui = 25 + np.power(-50*np.log(0.01*i) , 1/1.5)
        v = np.power(np.exp(-np.power(ui-x2,x3)/x1) - 0.01*i,2)
        value = np.sum(v)
        return value