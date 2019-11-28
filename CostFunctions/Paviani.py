from CostFunctions import CostFunctions
import numpy as np

__all__ = ['Paviani']


class Paviani(CostFunctions):
    functionProperties = {
        'minimumValue': -45.778,
        'optimalArms': [[9.351, 9.351, 9.351, 9.351, 9.351, 9.351, 9.351, 9.351, 9.351, 9.351]],
        'searchSpace': [[2.0001, 10],
                        [2.0001, 10],
                        [2.0001, 10],
                        [2.0001, 10],
                        [2.0001, 10],
                        [2.0001, 10],
                        [2.0001, 10],
                        [2.0001, 10],
                        [2.0001, 10],
                        [2.0001, 10]],
        'spaceType': ['uniform',
                      'uniform',
                      'uniform',
                      'uniform',
                      'uniform',
                      'uniform',
                      'uniform',
                      'uniform',
                      'uniform',
                      'uniform'],
        'x0': [np.random.uniform(2.0001, 10),
               np.random.uniform(2.0001, 10),
               np.random.uniform(2.0001, 10),
               np.random.uniform(2.0001, 10),
               np.random.uniform(2.0001, 10),
               np.random.uniform(2.0001, 10),
               np.random.uniform(2.0001, 10),
               np.random.uniform(2.0001, 10),
               np.random.uniform(2.0001, 10),
               np.random.uniform(2.0001, 10)],
        'Continuous': 'Continuous',
        'Differentiability': 'Differentiable',
        'Separability': 'Non-Separable',
        'Scalability': 'Scalable',
        'Modality': 'Multimodal',
        'Ndimensions': 10
    }

    def func(self, x):
        psum = 0
        product = 1
        for i in range(1,10+1):
            xi = x[i-1]
            interm = np.power((np.log(xi - 2)),2) + np.power((np.log(10 - xi)),2)
            psum = psum + interm
            product = xi * product
        value = psum - np.power(product, 0.2)
        return value
