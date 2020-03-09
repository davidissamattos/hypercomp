import unittest
from CostFunctions import all_benchmarks as bm
from CostFunctions import *
import numpy as np
import importlib
import logging
import colorlog

LOG_LEVEL = logging.INFO

handler = logging.StreamHandler()
LOGFORMAT = "  %(log_color)s%(levelname)-8s%(reset)s | %(log_color)s%(message)s%(reset)s"
handler.setFormatter(colorlog.ColoredFormatter(LOGFORMAT))
logger = logging.getLogger(__name__)
logger.addHandler(handler)
logger.propagate = False
logger.setLevel(LOG_LEVEL)

class TestBenchmark(unittest.TestCase):
    def IsFoptimalEqualToFmin(self, obj):
        x = obj.functionProperties['optimalArms']
        opt_value = obj.functionProperties['minimumValue']
        tol = obj.functionProperties['tol'] #we use the function tolerance (default 0.001)
        for xi in x:
            value = obj(xi)
            diff = np.abs(value - opt_value)
            msg = 'Function: '+ str(type(obj))+ \
                  ' arm_evaluated: '+ str(xi)+ \
                  ' optimal arm: ' + str(x) +\
                  ' optimal value: ' + str(opt_value) + \
                  ' obtained value: '+ str(value) + \
                  ' diff: ' + str(diff)

            self.assertLess(diff,tol,msg=msg)

    def AreTheDimensionsCorrect(self, obj):
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


    def IsFminTheMinimumByRandomSearchX100(self,obj):
        n=100
        opt_value = obj.functionProperties['minimumValue']
        searchSpace = obj.functionProperties['searchSpace']
        D = obj.functionProperties['Ndimensions']
        for i in range(n):
            sample = []
            for j in range(D):
                low = searchSpace[j][0]
                high = searchSpace[j][1]
                sample.append(np.random.uniform(low=low,high=high,size=1)[0])
            result = obj(sample)
            msg="The optimal value is not the minimum! " + \
             'Testing benchmark class: ' + str(type(obj)) + \
             ' sample ' + str(sample) + \
             ' result ' + str(result) + \
             ' theoretical optimal ' + str(opt_value)
            self.assertLess(opt_value,result,msg=msg)
        return

    def loopOverTestFunctions(self, fun):
        """
        Here we loop over all benchmark functions and execute teh function we want to test that is passed by fun
        fun must receive and benchmark function object instantiated
        :param fun:
        :return:
        """
        # Since some of the functions we don't a very good minimum
        for cname in bm:
            module = importlib.import_module('CostFunctions')
            cl = getattr(module, cname)
            # instantiating
            obj = cl(functionProperties=cl.functionProperties,
                     sd=0,
                     maxfeval=1e4)
            logger.debug('Testing benchmark class: ' + str(type(obj)))
            fun(obj)

    def test_IsFoptimalEqualToFmin(self):
        print()
        logger.info('Testing if the proposed optimal value equals to the set minimum value')
        self.loopOverTestFunctions(self.IsFoptimalEqualToFmin)

    def test_AreTheDimensionsCorrect(self):
        print()
        logger.info('Testing if the initial point, arms and search spaces have the same dimensions')
        self.loopOverTestFunctions(self.AreTheDimensionsCorrect)

    def test_IsFminTheMinimumByRandomSearchX100(self):
        print()
        logger.info('Random sampling to verify minimum')
        self.loopOverTestFunctions(self.IsFminTheMinimumByRandomSearchX100)

    # def test_allCostFunctionClasses(self):
    #     #Since some of the functions we don't a very good minimum
    #     for cname in bm:
    #         module = importlib.import_module('CostFunctions')
    #         cl = getattr(module, cname)
    #         #instantiating
    #         obj = cl(functionProperties=cl.functionProperties,
    #                         sd=0,
    #                         maxfeval=10)
    #         print('Testing benchmark class: ', type(obj))
    #         self.MinValue(obj)
    #         self.DimensionsTest(obj)



if __name__ == '__main__':
    # Run only the tests in the specified classes
    unittest.main()
