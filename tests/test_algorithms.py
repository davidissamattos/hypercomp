import unittest
from Algorithms import all_algorithms
from CostFunctions import *
import numpy as np
import importlib

class TestBenchmark(unittest.TestCase):
    """
    Not to be used always, because not always the algorithms converge...

    """
    def test_allAlgorithms(self):
        maxfeval = 50
        sd = 0
        tol = 0.5 #large tolerance
        all_algorithms.remove('CMAES')#not made for 1D
        for cname in all_algorithms:
            #We need to recreate the function for every algorithm
            objective = simpleQuadratic(functionProperties=simpleQuadratic.functionProperties,
                                        sd=sd,
                                        maxfeval=maxfeval)
            module = importlib.import_module('Algorithms')
            algoClass = getattr(module, cname)
            algo = algoClass(objective=objective,
                             maxfeval=maxfeval)
            result = algo.run()

            TrueRewardDifference = result['TrueRewardDifference']
            EuclideanDistance = result['EuclideanDistance']
            msg1 = 'Algorithm: ' + str(type(algo)) + ' |f(x_hat) - f(x)|: ' + str(TrueRewardDifference)
            msg2 = 'Algorithm: ' + str(type(algo)) + ' ||x_hat - x||_2: ' + str(EuclideanDistance)
            self.assertLess(TrueRewardDifference, tol, msg=msg1)
            self.assertLess(EuclideanDistance, tol, msg=msg2)


if __name__ == '__main__':
    # Run only the tests in the specified classes
    unittest.main()