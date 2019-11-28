"""
Implementation of the CrossInTray.py function

# Created by davidis at 2019-11-22
"""

from CostFunctions import CostFunctions
import numpy as np

__all__ = ['CrossInTray']


class CrossInTray(CostFunctions):
    """
    Implementation of the CrossInTray.py function from 
    M. Jamil and X.-S. S. Yang, “A Literature Survey of Benchmark Functions For Global Optimization Problems,” Int. J. Math. Model. Numer. Optim., vol. 4, no. 2, p. 150, Aug. 2013.
    """
    functionProperties = {
        'minimumValue': -2.06261218,
        'optimalArms': [[1.349406685353340, 1.349406608602084],
                        [-1.349406685353340, 1.349406608602084],
                        [1.349406685353340, -1.349406608602084],
                        [-1.349406685353340, -1.349406608602084]],
        'searchSpace': [[-10, 10], [-10, 10]],
        'spaceType': ['uniform', 'uniform'],
        'x0': [np.random.uniform(-10, 10), np.random.uniform(-10, 10)],
        'Continuous': 'Continuous',
        'Differentiability': 'Non-Differentiable',
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
        fexp = np.exp(np.abs(100 - np.sqrt(np.power(x1,2)+np.power(x2,2))/np.pi))
        value = -0.0001*np.power(np.abs(np.sin(x1)*np.sin(x2)*fexp) + 1, 0.1)
        return value