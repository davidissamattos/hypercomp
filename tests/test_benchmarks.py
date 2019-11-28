import unittest
from CostFunctions import all_benchmarks as bm
from CostFunctions import *
import numpy as np
import importlib

class TestBenchmark(unittest.TestCase):
    def MinValue(self, obj):
        x = obj.functionProperties['optimalArms']
        opt_value = obj.functionProperties['minimumValue']
        tol = obj.functionProperties['tol'] #we use the function tolerance (default 0.001)
        for xi in x:
            value = obj(xi)
            diff = np.abs(value - opt_value)
            msg = 'Function: '+ str(type(obj))+ \
                  ' arm_evaluated: '+ str(xi)+ \
                  ' optimal value: ' + str(opt_value) + \
                  ' obtained value: '+ str(value) + \
                  ' diff: ' + str(diff)

            self.assertLess(diff,tol,msg=msg)

    def DimensionsTest(self, obj):
        x0 = obj.functionProperties['x0']
        searchSpace = obj.functionProperties['searchSpace']
        optimalArms = obj.functionProperties['optimalArms']
        spaceType = obj.functionProperties['spaceType']
        Ndimensions = obj.functionProperties['Ndimensions']
        # check consistency in the initial point
        msg = 'Function: ' + str(type(obj)) + ' '
        self.assertEqual(len(x0), Ndimensions, msg=msg + 'x0 and N are incompatible')
        # check consistency in the size of the search space
        # e.g. len([[1,2],[2,3],[3,4]]) equals to 3
        self.assertEqual(len(searchSpace), Ndimensions, msg=msg + 'searchspace and N are incompatible')
        for arm in optimalArms:
            self.assertEqual(len(arm), Ndimensions, msg=msg + 'size of the arms and N are incompatible')
        self.assertEqual(len(spaceType), Ndimensions, msg=msg + 'size of the space type and N are incompatible')


    def test_allCostFunctionClasses(self):
        #Since some of the functions we don't a very good minimum
        for cname in bm:
            module = importlib.import_module('CostFunctions')
            cl = getattr(module, cname)
            #instantiating
            obj = cl(functionProperties=cl.functionProperties,
                            sd=0,
                            maxfeval=10)
            print('Testing benchmark class: ', type(obj))
            self.MinValue(obj)
            self.DimensionsTest(obj)



if __name__ == '__main__':
    # Run only the tests in the specified classes
    unittest.main()
