import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import logging

from CostFunctions import *
from hyperopt import fmin, tpe, hp, rand

from Comparator import *
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'gcpcredentials.json'

import GPy
import GPyOpt
from GPyOpt.methods import BayesianOptimization
from GPyOpt.experiment_design import initial_design


import cma

from smac.facade.func_facade import fmin_smac

from NiaPy.algorithms.basic import GreyWolfOptimizer
from NiaPy.task import StoppingTask
from NiaPy.benchmarks import Sphere

msg = "Starting message"
import importlib
from CostFunctions import all_benchmarks as bm


if __name__ == '__main__':

    maxfeval =20
    nsim=1
    sd=0



    # sim = Comparator(objFuncClass=Easom,
    #                      results_folder='data',
    #                      filename = 'test.csv',
    #                      sd=0,
    #                      maxfeval=10,
    #                      nsim=1,
    #                  useGCP=True,
    #                  GCPbucketName='hypercomp-experiment-data')
    sim = Comparator(objFuncClass=Easom,
                         results_folder='data',
                         filename ='test.csv',
                         sd=sd,
                         maxfeval=maxfeval,
                         nsim=nsim)

    # sim.run()


    from Algorithms.SMAC import SMAC
    from Algorithms.Hyperopt import RandomSearch

    # sim.run_algorithm(RandomSearch)
    sim.run_algorithm(SMAC)


    # from Algorithms.NiaPy import NiaPyABC
    # sim.run_algorithm(NiaPyABC)















