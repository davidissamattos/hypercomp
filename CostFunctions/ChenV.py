"""
Implementation of the ChenV.py function

# Created by davidis at 2019-11-20
"""

from CostFunctions import CostFunctions
import numpy as np

__all__ = ['ChenV']


class ChenV(CostFunctions):
    """
    Implementation of the ChenV.py function from 
    https://al-roomi.org/benchmarks/unconstrained/2-dimensions/110-chen-s-v-function
    """
    functionProperties = {
        'minimumValue': -2000,
        'optimalArms': [[7/18, 13/18]],
        'searchSpace': [[-300, 500], [-500, 300]],
        'spaceType': ['uniform', 'uniform'],
        'x0': [np.random.uniform(-300, 500), np.random.uniform(-500,300)],
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
        b = 0.001
        b2 = np.power(b,2)
        f1 = b2 + np.power(x1-0.4*x2-0.1, 2)
        f2 = b2 + np.power(2*x1+x2-1.5, 2)
        value = -b/f1 - b/f2
        return value