import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import logging

from CostFunctions import *
from hyperopt import fmin, tpe, hp, rand

from hypercomp import *
from bayes_opt import BayesianOptimization
from bayes_opt import UtilityFunction


import cma

from smac.facade.func_facade import fmin_smac

msg = "Starting message"

if __name__ == '__main__':
    #https://botorch.org/tutorials/optimize_with_cmaes
    #
    objective = Easom(functionProperties=Easom.functionProperties,
                                 sd=0,
                                 maxfevals=100)

    # sim1 = Simulator(objFuncClass = SixHumpCamelBack,
    #                 sd = 0.1,
    #                 maxfeval=10,
    #                 nsim=1)
    # sim1.run()
    # sim1.saveResults()


    x, cost, _ = fmin_smac(func=objective,
                           x0=[-3, -4],
                           bounds=[(-5, 10), (-5, 10)],
                           maxfun=100,
                           rng=3)  # Passing a seed makes fmin_smac determistic

    print("Optimum at {} with cost of {}".format(x, cost))


    # print(cma.CMAOptions('maxfevals'))
    # options = {'maxfevals': 900,
    #            'verb_disp': 0}
    # xopt, es = cma.fmin2(objective_function=objective,
    #          x0=objective.functionProperties['x0'],
    #          sigma0=0.5,options=options)
    #
    # print(xopt)


    # def black_box_function(x, y):
    #     return -x ** 2 - (y - 1) ** 2 + 1

    # pbounds = {'x': (2, 4), 'y': (-3, 3)}
    # optimizer = BayesianOptimization(
    #     f=None,
    #     pbounds=pbounds,
    #     random_state=1,
    #     verbose=0 #silent mode
    # )

    # #
    # utility = UtilityFunction(kind='ucb', kappa=2.5, xi=0.0)

    # for i in range(2):
    #     next_point_to_probe = optimizer.suggest(utility)
    #     print("Next point to probe is:", next_point_to_probe)
    #     #evaluate the black box function
    #     target = black_box_function(**next_point_to_probe)
    #     #register in the algo
    #     optimizer.register(
    #         params=next_point_to_probe,
    #         target = target
    #     )
    # print(optimizer.max)

    # #EI
    # optimizer.maximize(
    #     init_points=0,
    #     n_iter=100,
    #     acq="ei",
    #     xi=1e-4)
    # #Probability of improvement
    # optimizer.maximize(
    #     init_points=0,
    #     n_iter=100,
    #     acq="poi",
    #     xi=1e-4)
    # #UCB
    # optimizer.maximize(
    #     init_points=0,
    #     n_iter=100,
    #     acq="ucb",
    #     kappa=10.0)
    # print(optimizer.max)

# ### Using Hyperopt TPE
#     hyperopt_objective1 = SixHumpCamelBack(functionProperties=SixHumpCamelBack.functionProperties,
#     sd=0,
#     maxfevals=100)

#     space = [hp.uniform('x1',-1,1),hp.uniform('x2',-1,1)]

#     best = fmin(fn=hyperopt_objective1,
#         space= space,
#         algo=tpe.suggest,
#         max_evals=100)
#     print(best)

# ### Using Hyperopt Random search
#     hyperopt_objective2 = SixHumpCamelBack(functionProperties=SixHumpCamelBack.functionProperties,
#     sd=0,
#     maxfevals=100)
#     space = [hp.uniform('x1',-1,1),hp.uniform('x2',-1,1)]
#     best = fmin(fn=hyperopt_objective2,
#         space= space,
#         algo=rand.suggest,
#         max_evals=100)
#     print(best)

# ### Using Hyperopt ATPE search
#     hyperopt_objective3 = SixHumpCamelBack(functionProperties=SixHumpCamelBack.functionProperties,
#     sd=0,
#     maxfevals=100)
#     space = [hp.uniform('x1',-1,1),hp.uniform('x2',-1,1)]
#     best = fmin(fn=hyperopt_objective2,
#         space= space,
#         algo=atpe.suggest,
#         max_evals=100)
#     print(best)
