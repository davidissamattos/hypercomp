import copy
from Algorithms.Algorithm import Algorithm

from Algorithms.Hyperopt import RandomSearch, TPE, ATPE
from Algorithms.NiaPy import NiaPyABC, NiaPyBat,NiaPyCuckooSearch, NiaPyDifferentialEvolution, NiaPyFireflyAlgorithm, NiaPyGeneticAlgorithm,NiaPyGWO,NiaPyNelderMead, NiaPyPSO, NiaPySimulatedAnnealing
from Algorithms.BayesianOpt import BayesOptEILatin, BayesOptLCBLatin, BayesOptEIRandom, BayesOptMPILatin, BayesOptMPIRandom, BayesOptLCBRandom
from Algorithms.CMAES import CMAES
from Algorithms.HpbandsterAlgorithms import hpbandsterBOHB, hpbandsterHyperBand
from Algorithms.SMAC import SMAC
from Algorithms.RandomXN import RandomSearch2, RandomSearch4, RandomSearch10
from Algorithms.mLGHOO import mLGHOO, HOO




bayesian  = ['BayesOptEIRandom', 'BayesOptEILatin',
            # 'BayesOptLCBRandom', 'BayesOptLCBLatin'
            #'BayesOptMPIRandom', 'BayesOptMPILatin'
             ]

mlghoo = ['mLGHOO', 'HOO']

others = ['CMAES']

smac = ['SMAC']

hpbandster = ['hpbandsterBOHB','hpbandsterHyperBand']

tpe = ['TPE','ATPE']

random_search = ['RandomSearch', 'RandomSearch2', 'RandomSearch4', 'RandomSearch10']

niapy = [ 'NiaPyABC',
            'NiaPyBat',
            'NiaPyCuckooSearch',
            'NiaPyDifferentialEvolution',
            'NiaPyFireflyAlgorithm',
            'NiaPyGeneticAlgorithm',
            'NiaPyGWO',
            'NiaPyNelderMead',
            'NiaPyPSO',
            'NiaPySimulatedAnnealing']


niapy_random_search = niapy + random_search

bayes_only = hpbandster + smac + bayesian

no_bayesian = niapy + random_search + tpe + others + mlghoo

all_algorithms = bayesian + mlghoo + others + smac + hpbandster + tpe + random_search + niapy