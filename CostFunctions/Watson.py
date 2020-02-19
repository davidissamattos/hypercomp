"""
Implementation of the Watson.py function

# Created by davidis at 2020-02-19
"""

from CostFunctions import CostFunctions
import numpy as np

__all__ = ['Watson']


class Watson(CostFunctions):
    """
    Implementation of the Watson.py function from 
    M. Jamil and X.-S. S. Yang, “A Literature Survey of Benchmark Functions For Global Optimization Problems,” Int. J. Math. Model. Numer. Optim., vol. 4, no. 2, p. 150, Aug. 2013.
    """
    functionProperties = {
        'minimumValue': 0.002288,
        'optimalArms': [[-0.0158, 1.012, -0.2329, 1.260, -1.513, 0.9928]],
        'searchSpace': [[-10, 5], [-10, 5], [-10, 5], [-10, 5], [-10, 5], [-10, 5]],
        'spaceType': ['uniform', 'uniform','uniform','uniform','uniform','uniform'],
        'x0': [np.random.uniform(-10, 5),
               np.random.uniform(-10, 5),
               np.random.uniform(-10, 5),
               np.random.uniform(-10, 5),
               np.random.uniform(-10, 5),
               np.random.uniform(-10, 5)],
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
        """
        vec = np.zeros((31,))
        div = (np.arange(29) + 1.0) / 29.0
        s1 = 0.0
        dx = 1.0

        for j in range(1, 6):
            s1 += j * dx * x[j]
            dx *= div

        s2 = 0.0
        dx = 1.0

        for j in range(6):
            s2 += dx * x[j]
            dx *= div

        vec[:29] = s1 - s2 ** 2.0 - 1.0
        vec[29] = x[0]
        vec[30] = x[1] - x[0] ** 2 - 1

        value= np.sum(vec ** 2.0)
        return value