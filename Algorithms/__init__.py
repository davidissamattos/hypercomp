import copy
from Algorithms.Algorithm import Algorithm

from Algorithms.Hyperopt import RandomSearch, TPE, ATPE
from Algorithms.NiaPy import NiaPyABC, NiaPyCuckooSearch, NiaPyDifferentialEvolution, NiaPyGWO, NiaPyNelderMead, NiaPyPSO, NiaPySimulatedAnnealing
from Algorithms.BayesianOpt import BayesOptEILatin, BayesOptLCBLatin, BayesOptEIRandom, BayesOptMPILatin, BayesOptMPIRandom, BayesOptLCBRandom
from Algorithms.CMAES import CMAES
from Algorithms.HpbandsterAlgorithms import hpbandsterBOHB, hpbandsterHyperBand
from Algorithms.SMAC import SMAC
from Algorithms.RandomXN import RandomSearch2, RandomSearch4, RandomSearch10
from Algorithms.mLGHOO import mLGHOO, HOO


all_algorithms = ['RandomSearch','TPE','ATPE',
                  'NiaPyGWO','NiaPyNelderMead','NiaPyPSO','NiaPyABC','NiaPyCuckooSearch','NiaPyDifferentialEvolution','NiaPySimulatedAnnealing',
                  'BayesOptEIRandom', 'BayesOptEILatin', 'BayesOptLCBRandom', 'BayesOptLCBLatin', 'BayesOptMPIRandom', 'BayesOptMPILatin',
                  'CMAES',
                  'hpbandsterBOHB','hpbandsterHyperBand',
                  'SMAC',
                  'RandomSearch2', 'RandomSearch4', 'RandomSearch10',
                  'mLGHOO', 'HOO',
                  ]