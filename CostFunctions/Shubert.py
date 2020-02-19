"""
Implementation of the Shubert.py function

# Created by davidis at 2020-02-17
"""

from CostFunctions import CostFunctions
import numpy as np

__all__ = ['Shubert']


class Shubert(CostFunctions):
    """
    Implementation of the Shubert.py function from 
    M. Jamil and X.-S. S. Yang, “A Literature Survey of Benchmark Functions For Global Optimization Problems,” Int. J. Math. Model. Numer. Optim., vol. 4, no. 2, p. 150, Aug. 2013.
    """
    functionProperties = {
        'minimumValue': -186.7309,
        'optimalArms': [[-7.0835, 4.8580],
                        [-7.0835, -7.7083],
                        [-1.4251, -7.0835],
                        [-1.4251, -0.8003],
                        [-7.7083, -7.0835],
                        [-7.7083, -0.8003],
                        [-0.8003, -7.7083],
                        [-0.8003, 4.8580],
                        [5.4828, -7.7083],
                        [5.4828, -1.4251],
                        [5.4828, 4.8580],
                        [4.8580, 5.4828],
                        [-7.0835, -1.4251],
                        [-7.7083, 5.4828],
                        [-0.8003, -1.4251],
                        [-1.4251, 5.4828],
                        [4.8580, -7.0835],
                        [4.8580, -0.8003]
    ],
        'searchSpace': [[-10, 10], [-10, 10]],
        'spaceType': ['uniform', 'uniform'],
        'x0': [np.random.uniform(-10, 10), np.random.uniform(-10, 10)],
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
        """
        s1 = s2 = 0.0
        for i in range(1, 6):
            s1 = s1 + i * np.cos((i + 1) * x[0] + i)
            s2 = s2 + i * np.cos((i + 1) * x[1] + i)

        value = s1 * s2
        return value