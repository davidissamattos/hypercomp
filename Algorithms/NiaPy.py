from Algorithms import Algorithm
from utils import *
import logging
logger = logging.getLogger('Algorithms')

from NiaPy.algorithms.basic import GreyWolfOptimizer
from NiaPy.algorithms.other import NelderMeadMethod
from NiaPy.algorithms.basic import ArtificialBeeColonyAlgorithm
from NiaPy.algorithms.basic import ParticleSwarmAlgorithm
from NiaPy.algorithms.basic import GeneticAlgorithm
from NiaPy.algorithms.basic.ga import UniformCrossover, UniformMutation
from NiaPy.algorithms.basic import CuckooSearch
from NiaPy.algorithms.basic import DifferentialEvolution
from NiaPy.algorithms.other import SimulatedAnnealing
from NiaPy.algorithms.other.sa import coolLinear
from NiaPy.task import StoppingTask
from NiaPy.benchmarks.benchmark import Benchmark
from NiaPy.algorithms.basic import BatAlgorithm
from NiaPy.algorithms.basic import FireflyAlgorithm

__all__ = [ 'NiaPyABC',
            'NiaPyBat',
            'NiaPyCuckooSearch',
            'NiaPyDifferentialEvolution',
            'NiaPyFireflyAlgorithm',
            'NiaPyGeneticAlgorithm',
            'NiaPyGWO',
            'NiaPyNelderMead',
            'NiaPyPSO',
            'NiaPySimulatedAnnealing']

class NiaPy(Algorithm):
    """
    Runs several algorithms from the NiaPy package
        The default values  comes from the Jie-ShengWang & Shu-Xia Li paper

    """

    def __init__(self, algorithm_name, objective, maxfeval, population=30):
        super().__init__(algorithm_name, objective, maxfeval)
        self.algorithm_name = algorithm_name
        self.algo = None #this is the suggest function from hyperopt
        if algorithm_name not in __all__:
            raise Exception('NiaPy does not have algorithm :' + str(algorithm_name))

        elif self.algorithm_name == 'NiaPyABC':
            self.algo = ArtificialBeeColonyAlgorithm(NP=population, Limit=2)

        elif self.algorithm_name == 'NiaPyBat':
            self.algo = BatAlgorithm(NP=population)

        elif self.algorithm_name == 'NiaPyCuckooSearch':
            self.algo = CuckooSearch(N=population, pa=0.25, alpha=0.01)

        elif self.algorithm_name == 'NiaPyDifferentialEvolution':
            self.algo = DifferentialEvolution(NP=population, F=1, CR=0.7)  # default from the paper

        elif self.algorithm_name == 'NiaPyFireflyAlgorithm':
            self.algo = FireflyAlgorithm(NP=population, alpha=0.5, betamin=0.2, gamma=1.0)

        elif self.algorithm_name == 'NiaPyGeneticAlgorithm':
            self.algo = FireflyAlgorithm(NP=population, Crossover=UniformCrossover, Mutation=UniformMutation, Cr=0.45, Mr=0.9)


        elif self.algorithm_name == 'NiaPyGWO':
            self.algo = GreyWolfOptimizer(NP=population)
        # config
        elif self.algorithm_name == 'NiaPyNelderMead':
            self.algo = NelderMeadMethod(NP=population)
        # config
        elif self.algorithm_name == 'NiaPyPSO':
            self.algo = ParticleSwarmAlgorithm(NP=population, C1=2, C2=2, w=0.9, vMin=1.5, vMax=1.5)


        # config

        # config
               # config
        elif self.algorithm_name == 'NiaPySimulatedAnnealing':
            self.algo = SimulatedAnnealing(coolingMethod=coolLinear)


    def assemblespace(self):
        """
        We need to create a variable self.space to store the space to be used by the algorithm
        Changes between algorithms

        """
        try:
            obj_space = self.objective.functionProperties['searchSpace']
            self.x0 = self.objective.functionProperties['x0']
            obj_space_type = self.objective.functionProperties['spaceType']
            lower = []
            higher = []
            for v in obj_space:
                lower.append(v[0])
                higher.append(v[1])

            self.lowerBound = min(lower)
            self.higherBound = max(higher)
        except:
            logger.error('Error assembling the space for ' + str(self.algorithm_name) + ' with cost function: ' + str(
                self.objective.GetCostFunctionName()))
            #since it will fail later in the optimize function we pass here
            pass




    def optimize(self):
        """
        The main optimization procedure
        Should return the best arm as and array/ list
        :return:

        THe instance to be optimized is the self.objective value
        """
        try:
            class MyBenchmark(Benchmark):
                def __init__(self,benchmark_objective, Lower=self.lowerBound, Upper=self.higherBound):
                    self.benchmark_objective = benchmark_objective
                    Benchmark.__init__(self, Lower, Upper)
                def function(self):
                    bench = self.benchmark_objective
                    def evaluate(D,sol):
                        val = bench(sol)
                        return val
                    return evaluate


            # run the random search algorithm
            task = StoppingTask(D=len(self.x0),
                                nFES=self.maxfeval,
                                benchmark=MyBenchmark(benchmark_objective=self.objective,
                                                      Lower=self.lowerBound,
                                                      Upper=self.higherBound)
                                )
            best = self.algo.run(task)
            #Some classes in the NiaPy return different formats for the best result
            xopt = []
            for xi in best[0]:
               xopt.append(xi)
            success = True
            best_arm = convertToArray(xopt)
        except:
            logger.warning('Optimization for ' + str(self.algorithm_name) + ' failed.')
            best_arm = NAN
            success = False
        return best_arm, success, self.objective


class NiaPyBat(NiaPy):
    def __init__(self, objective, maxfeval):
        super().__init__(objective=objective,
                         maxfeval=maxfeval,
                         algorithm_name='NiaPyBat')
class NiaPyABC(NiaPy):
    def __init__(self, objective, maxfeval):
        super().__init__(objective=objective,
                         maxfeval=maxfeval,
                         algorithm_name='NiaPyABC')

class NiaPyCuckooSearch(NiaPy):
    def __init__(self, objective, maxfeval):
        super().__init__(objective=objective,
                         maxfeval=maxfeval,
                         algorithm_name='NiaPyCuckooSearch')

class NiaPyDifferentialEvolution(NiaPy):
    def __init__(self, objective, maxfeval):
        super().__init__(objective=objective,
                         maxfeval=maxfeval,
                         algorithm_name='NiaPyDifferentialEvolution')

class NiaPyFireflyAlgorithm(NiaPy):
    def __init__(self, objective, maxfeval):
        super().__init__(objective=objective,
                         maxfeval=maxfeval,
                         algorithm_name='NiaPyFireflyAlgorithm')


class NiaPyGWO(NiaPy):
    def __init__(self, objective, maxfeval):
        super().__init__(objective=objective,
                         maxfeval=maxfeval,
                         algorithm_name='NiaPyGWO')

class NiaPyGeneticAlgorithm(NiaPy):
    def __init__(self, objective, maxfeval):
        super().__init__(objective=objective,
                         maxfeval=maxfeval,
                         algorithm_name='NiaPyGeneticAlgorithm')

class NiaPyNelderMead(NiaPy):
    def __init__(self, objective, maxfeval):
        super().__init__(objective=objective,
                         maxfeval=maxfeval,
                         algorithm_name='NiaPyNelderMead')

class NiaPyPSO(NiaPy):
    def __init__(self, objective, maxfeval):
        super().__init__(objective=objective,
                         maxfeval=maxfeval,
                         algorithm_name='NiaPyPSO')


class NiaPySimulatedAnnealing(NiaPy):
    def __init__(self, objective, maxfeval):
        super().__init__(objective=objective,
                         maxfeval=maxfeval,
                         algorithm_name='NiaPySimulatedAnnealing')
