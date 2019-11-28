"""
Implementation of the ElAttarVidyasagarDutta.py function

# Created by davidis at 2019-11-22
"""

from CostFunctions import CostFunctions
import numpy as np

__all__ = ['ElAttarVidyasagarDutta']


class ElAttarVidyasagarDutta(CostFunctions):
    """
    Implementation of the ElAttarVidyasagarDutta.py function from 
    M. Jamil and X.-S. S. Yang, “A Literature Survey of Benchmark Functions For Global Optimization Problems,” Int. J. Math. Model. Numer. Optim., vol. 4, no. 2, p. 150, Aug. 2013.
    https://www.al-roomi.org/benchmarks/unconstrained/2-dimensions/121-el-attar-vidyasagar-dutta-s-function
    """
    functionProperties = {
        'minimumValue': 1.712780354862198,
        'optimalArms': [[3.4091868222,-2.1714330361]],
        'searchSpace': [[-500, 500], [-500, 500]],
        'spaceType': ['uniform', 'uniform'],
        'x0': [np.random.uniform(-500, 500), np.random.uniform(-500, 500)],
        'Continuous': 'Continuous',
        'Differentiability': 'Differentiable',
        'Separability': 'Non-Separable',
        'Scalability': 'Non-Scalable',
        'Modality': 'Unimodal',
        'Ndimensions': 2
    }

    def func(self, x):
        """
        x is an array E.g.
        x1 = x[0]
        x2 = x[1]
        """
        x1 = x[0]
        x2 = x[1]
        value = np.power(np.power(x1,2)+ x2 -10,2) + np.power(x1 + np.power(x2,2)-7, 2) + np.power(np.power(x1,2) + np.power(x2,3) -1, 2)

        return value