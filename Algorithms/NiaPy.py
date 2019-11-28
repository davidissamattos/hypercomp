from Algorithms import Algorithm
from utils import *

from NiaPy.algorithms.basic import GreyWolfOptimizer
from NiaPy.algorithms.other import NelderMeadMethod
from NiaPy.algorithms.basic import ArtificialBeeColonyAlgorithm
from NiaPy.algorithms.basic import ParticleSwarmAlgorithm
from NiaPy.algorithms.basic import CuckooSearch
from NiaPy.algorithms.basic import DifferentialEvolution
from NiaPy.algorithms.other import SimulatedAnnealing
from NiaPy.algorithms.other.sa import coolLinear
from NiaPy.task import StoppingTask
from NiaPy.benchmarks.benchmark import Benchmark

__all__ = ['NiaPyGWO','NiaPyNelderMead','NiaPyPSO','NiaPyABC','NiaPyCuckooSearch','NiaPyDifferentialEvolution','NiaPySimulatedAnnealing']

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
        elif self.algorithm_name == 'NiaPyGWO':
            self.algo = GreyWolfOptimizer(NP=population)
        # config
        elif self.algorithm_name == 'NiaPyNelderMead':
            self.algo = NelderMeadMethod(NP=population)
        # config
        elif self.algorithm_name == 'NiaPyPSO':
            self.algo = ParticleSwarmAlgorithm(NP=population, C1=2, C2=2, w=0.9, vMin=1.5, vMax=1.5)
        # config
        elif self.algorithm_name == 'NiaPyABC':
            self.algo = ArtificialBeeColonyAlgorithm(NP=population, Limit=2)
        # config
        elif self.algorithm_name == 'NiaPyCuckooSearch':
            self.algo = CuckooSearch(N=population, pa=0.25, alpha=0.01)
        # config
        elif self.algorithm_name == 'NiaPyDifferentialEvolution':
            self.algo = DifferentialEvolution(NP=population, F=1, CR=0.7)  # default from the paper
        # config
        elif self.algorithm_name == 'NiaPySimulatedAnnealing':
            self.algo = SimulatedAnnealing(coolingMethod=coolLinear)


    def assemblespace(self):
        """
        We need to create a variable self.space to store the space to be used by the algorithm
        Changes between algorithms

        """
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




    def optimize(self):
        """
        The main optimization procedure
        Should return the best arm as and array/ list
        :return:

        THe instance to be optimized is the self.objective value
        """
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
        if type(best[0]) == None:
            xopt=self.x0
        else:
            for xi in best[0]:
               xopt.append(xi)
        best_arm = convertToArray(xopt)
        # print('best_arm: ', best_arm, ' best0: ', best[0])
        return best_arm


class NiaPyGWO(NiaPy):
    def __init__(self, objective, maxfeval):
        super().__init__(objective=objective,
                         maxfeval=maxfeval,
                         algorithm_name='NiaPyGWO')

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

class NiaPySimulatedAnnealing(NiaPy):
    def __init__(self, objective, maxfeval):
        super().__init__(objective=objective,
                         maxfeval=maxfeval,
                         algorithm_name='NiaPySimulatedAnnealing')
