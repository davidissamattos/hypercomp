"""
Implementation of the SchmidtVetters.py function

# Created by davidis at 2020-02-14
"""

from CostFunctions import CostFunctions
import numpy as np

__all__ = ['SchmidtVetters']


class SchmidtVetters(CostFunctions):
    """
    Implementation of the SchmidtVetters.py function from 
    M. Jamil and X.-S. S. Yang, “A Literature Survey of Benchmark Functions For Global Optimization Problems,” Int. J. Math. Model. Numer. Optim., vol. 4, no. 2, p. 150, Aug. 2013.
    """
    functionProperties = {
        'minimumValue': 3.0,
        'optimalArms': [[0.78547, 0.78547, 0.78547]],
        'searchSpace': [[0.1, 10], [0.1, 10], [0.1, 10]],
        'spaceType': ['uniform', 'uniform'],
        'x0': [np.random.uniform(0.1, 10), np.random.uniform(0.1, 10),np.random.uniform(0.1, 10)],
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
        value = 1.0/(1.0 + (x1 - x2)**2.0) + np.sin((np.pi*x2 + x3)/2.0) + np.exp(((x1 + x2)/x2 - 2)**2.0)
        return value