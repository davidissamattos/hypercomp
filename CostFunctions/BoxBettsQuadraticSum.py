"""
Implementation of the BoxBettsQuadraticSum.py function

# Created by davidis at 2019-11-20
"""

from CostFunctions import CostFunctions
import numpy as np

__all__ = ['BoxBettsQuadraticSum']


class BoxBettsQuadraticSum(CostFunctions):
    """
    Implementation of the BoxBettsQuadraticSum.py function from 
    M. Jamil and X.-S. S. Yang, “A Literature Survey of Benchmark Functions For Global Optimization Problems,” Int. J. Math. Model. Numer. Optim., vol. 4, no. 2, p. 150, Aug. 2013.
    https://www.al-roomi.org/benchmarks/unconstrained/3-dimensions/87-box-betts-exponential-quadratic-sum-function
    """
    functionProperties = {
        'minimumValue': 0,
        'optimalArms': [[1, 10, 1]],
        'searchSpace': [[0.9, 1.2], [9, 11.2], [0.9, 1.2]],
        'spaceType': ['uniform', 'uniform', 'uniform'],
        'x0': [np.random.uniform(0.9, 1.2), np.random.uniform(9, 11.2), np.random.uniform(0.9, 1.2)],
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

        def g(i, x1, x2, x3):
            f1 = np.exp(-0.1 * i * x1)
            f2 = np.exp(-0.1 * i * x2)
            f3 = (np.exp(-0.1 * i) - np.exp(-i) )* x3
            return f1 - f2 - f3

        value = 0
        for i in range(1,10+1):
            value = np.power(g(i ,x1,x2,x3 ),2)
        return value