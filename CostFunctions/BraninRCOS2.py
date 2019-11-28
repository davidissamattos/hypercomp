from CostFunctions import CostFunctions
import numpy as np

__all__ = ['BraninRCOS2']


class BraninRCOS2(CostFunctions):
    """
    function from https://www.al-roomi.org/benchmarks/unconstrained/2-dimensions/137-branin-s-rcos-function-no-2

    """
    functionProperties = {
        'minimumValue': -0.179891239069905,
        'optimalArms': [[-3.196988423389338 , 12.526257883092258]],
        'searchSpace': [[-5, 10], [0, 15]],
        'spaceType': ['uniform', 'uniform'],
        'x0': [np.random.uniform(-5,10),np.random.uniform(0,15)],
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
        a =1
        b = 5.1/(4*np.power(np.pi,2))
        c= 5/np.pi
        d= 6
        e =10
        g = 1/(8*np.pi)
        f1 = a*np.power(x2-b*np.power(x1,2)+ c*x1- d,2)
        f2= e*(1-g) *np.cos(x1)*np.cos(x2)
        f3 = np.log(np.power(x1,2)+np.power(x2,2) + 1)
        value = (-1)/(f1 +f2 +f3 + e)

        return value