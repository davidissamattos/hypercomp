"""
Implementation of the Damavandi.py function

# Created by davidis at 2019-11-22
"""

from CostFunctions import CostFunctions
import numpy as np

__all__ = ['Damavandi']


class Damavandi(CostFunctions):
    """
    Implementation of the Damavandi.py function from 
    M. Jamil and X.-S. S. Yang, “A Literature Survey of Benchmark Functions For Global Optimization Problems,” Int. J. Math. Model. Numer. Optim., vol. 4, no. 2, p. 150, Aug. 2013.
    """
    functionProperties = {
        'minimumValue': 0,
        'optimalArms': [[2.000000001, 2.000000001]],
        'searchSpace': [[0, 14], [0, 14]],
        'spaceType': ['uniform', 'uniform'],
        'x0': [np.random.uniform(0, 14), np.random.uniform(0, 14)],
        'Continuous': 'Continuous',
        'Differentiability': 'Differentiable',
        'Separability': 'Non-Separable',
        'Scalability': 'Non-Scalable',
        'Modality': 'Multimodal',
        'Ndimensions': 2
    }

    def func(self, x):
        x1 = x[0]
        x2 = x[1]
        fabs = np.abs((np.sin(np.pi*(x1-2))*np.sin(np.pi*(x2-2)))/(np.power(np.pi,2)*(x1-2)*(x2-2)))
        f1= (1-np.power(fabs,5))
        f2 = 2 + np.power(x1-7,2) + 2*np.power(x2-7,2)
        value = f1*f2
        return value