"""
Implementation of the Brad function

# Created by davidis at 2019-11-19
"""

from CostFunctions import CostFunctions
import numpy as np

__all__ = ['Brad']


class Brad(CostFunctions):
    """
    Implementation of the Brad function from
    M. Jamil and X.-S. S. Yang, “A Literature Survey of Benchmark Functions For Global Optimization Problems,” Int. J. Math. Model. Numer. Optim., vol. 4, no. 2, p. 150, Aug. 2013.
    """
    functionProperties = {
        'minimumValue': 0.00821487,
        'optimalArms': [[0.0824, 1.133, 2.3437]],
        'searchSpace': [[-0.25, 0.25], [0.01, 2.5], [0.01, 2.5]],
        'spaceType': ['uniform', 'uniform', 'uniform'],
        'x0': [0, 0, 0],
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
        y = [0.14, 0.18, 0.22, 0.25, 0.29, 0.32, 0.35, 0.39, 0.37, 0.58, 0.73, 0.96, 1.34, 2.10, 4.39]
        for i in range(1,15+1):
            ui = i
            vi = 16 - i
            wi = min(ui,vi)
            yi = y[i-1]#because of the loop starts at 1
            numerator = x1*x2*vi +x1*x3*wi + ui
            denominator = vi * x2 + wi * x3
            value = value + yi - np.power(numerator/denominator, 1)
        return value