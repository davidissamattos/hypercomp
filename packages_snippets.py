import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import logging

from CostFunctions import *
from hyperopt import fmin, tpe, hp, rand
from Comparator import *
from bayes_opt import BayesianOptimization
from bayes_opt import UtilityFunction
import cma
from smac.facade.func_facade import fmin_smac




# SMAC

# x, cost, _ = fmin_smac(func=objective,
    #                        x0=[-3, -4],
    #                        bounds=[(-5, 10), (-5, 10)],
    #                        maxfun=100,
    #                        rng=3)  # Passing a seed makes fmin_smac determistic
    #
    # print("Optimum at {} with cost of {}".format(x, cost))




# CMA-ES
# https://botorch.org/tutorials/optimize_with_cmaes
#
# print(cma.CMAOptions('maxfeval'))
# options = {'maxfeval': 900,
#            'verb_disp': 0}
# xopt, es = cma.fmin2(objective_function=objective,
#          x0=objective.functionProperties['x0'],
#          sigma0=0.5,options=options)
#
# print(xopt)





# Bayesian Optimization

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



# TPE and Random search from hyperopt
# ### Using Hyperopt TPE
#     hyperopt_objective1 = SixHumpCamelBack(functionProperties=SixHumpCamelBack.functionProperties,
#     sd=0,
#     maxfeval=100)

#     space = [hp.uniform('x1',-1,1),hp.uniform('x2',-1,1)]

#     best = fmin(fn=hyperopt_objective1,
#         space= space,
#         algo=tpe.suggest,
#         max_evals=100)
#     print(best)

# ### Using Hyperopt Random search
#     hyperopt_objective2 = SixHumpCamelBack(functionProperties=SixHumpCamelBack.functionProperties,
#     sd=0,
#     maxfeval=100)
#     space = [hp.uniform('x1',-1,1),hp.uniform('x2',-1,1)]
#     best = fmin(fn=hyperopt_objective2,
#         space= space,
#         algo=rand.suggest,
#         max_evals=100)
#     print(best)



## This is a non working wrappter for the SMAC3 HPO from the hypercomp file
    # def RunSMACHPO(self):
    #     """
    #     Runs SMACHPO
    #     """
    #     objective = self.objFuncClass(functionProperties=self.objFuncClass.functionProperties,
    #                                   sd=self.maxfeval,
    #                                   maxfeval=self.maxfeval)
    #     obj_space = self.objFuncClass.functionProperties['searchSpace']
    #     x0 = self.objFuncClass.functionProperties['x0']
    #     obj_space_type = self.objFuncClass.functionProperties['spaceType']
    #
    #
    #     # assembling the space
    #     cs = ConfigurationSpace()
    #     i = 0
    #     space = []
    #     for dim_i in obj_space:
    #         spc = None
    #         varname = 'x' + str(i)
    #         if obj_space_type[i] == 'uniform':
    #             spc = UniformFloatHyperparameter(varname, dim_i[0], dim_i[1],x0[i])
    #         # TODO: categorical
    #         if obj_space_type[i] == 'categorical':
    #             raise TypeError('This algorithm doesnt accept categorical variables')
    #         space.append(spc)
    #         i = i + 1
    #     cs.add_hyperparameters(space)
    #
    #     #assembling the scenario object
    #     # Scenario object
    #     scenario = Scenario({"run_obj": "quality",  # we optimize quality (alternatively runtime)
    #                          "runcount-limit": self.maxfeval,
    #                          # max. number of function evaluations; for this example set to a low number
    #                          "cs": cs,  # configuration space
    #                          "deterministic": "false"
    #                          })
    #
    #     # run the random search algorithm
    #     smac = SMAC4HPO(scenario=scenario,
    #                     tae_runner=objective)
    #     start = timer()
    #     smac.optimize()
    #     end = timer()
    #     timetocomplete = end - start
    #
    #     # saving the results
    #     algo = 'SMACHPO'
    #     result = objective.GenerateInfo(best_arm=x,
    #                                     timetocomplete=timetocomplete,
    #                                     algorithm_name=algo)
    #     self.results.append(result)
    #     return





##### BOHB and hyperband

# import logging
# logging.basicConfig(level=logging.WARNING)
#
# import argparse
#
# import hpbandster.core.nameserver as hpns
# import hpbandster.core.result as hpres
#
# from hpbandster.optimizers import BOHB as BOHB
# from hpbandster.examples.commons import MyWorker
#
# import ConfigSpace as CS
# from hpbandster.core.worker import Worker
# import numpy as np
#
#
# class MyWorker(Worker):
#
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#
#     def compute(self, config, budget, **kwargs):
#         """
#         Simple example for a compute function
#         The loss is just a the config + some noise (that decreases with the budget)
#
#         For dramatization, the function can sleep for a given interval to emphasizes
#         the speed ups achievable with parallel workers.
#
#         Args:
#             config: dictionary containing the sampled configurations by the optimizer
#             budget: (float) amount of time/epochs/etc. the model can use to train
#
#         Returns:
#             dictionary with mandatory fields:
#                 'loss' (scalar)
#                 'info' (dict)
#         """
#         x1 = config['x1']
#         x2 =config['x2']
#         print(config)
#         res = np.cos(x1) * np.cos(x2) * np.exp(-(x1 - np.pi) ** 2 - (x2 - np.pi) ** 2)
#
#         return ({
#             'loss': float(res),  # this is the a mandatory field to run hyperband
#             'info': res  # can be used for any user-defined information - also mandatory
#         })
#
#     @staticmethod
#     def get_configspace():
#         config_space = CS.ConfigurationSpace()
#         config_space.add_hyperparameter(CS.UniformFloatHyperparameter('x1', lower=-5, upper=5))
#         config_space.add_hyperparameter(CS.UniformFloatHyperparameter('x2', lower=-5, upper=5))
#         return(config_space)
#
# # Step 1: Start a nameserver
# # Every run needs a nameserver. It could be a 'static' server with a
# # permanent address, but here it will be started for the local machine with the default port.
# # The nameserver manages the concurrent running workers across all possible threads or clusternodes.
# # Note the run_id argument. This uniquely identifies a run of any HpBandSter optimizer.
# NS = hpns.NameServer(run_id='example1', host='127.0.0.1', port=None)
# NS.start()
#
# # Step 2: Start a worker
# # Now we can instantiate a worker, providing the mandatory information
# # Besides the sleep_interval, we need to define the nameserver information and
# # the same run_id as above. After that, we can start the worker in the background,
# # where it will wait for incoming configurations to evaluate.
# w = MyWorker(nameserver='127.0.0.1',run_id='example1')
# w.run(background=True)
#
# # Step 3: Run an optimizer
# # Now we can create an optimizer object and start the run.
# # Here, we run BOHB, but that is not essential.
# # The run method will return the `Result` that contains all runs performed.
# bohb = BOHB(  configspace = w.get_configspace(),
#               run_id = 'example1', nameserver='127.0.0.1',
#               min_budget=1, max_budget=1
#            )
# print('Running bohb now')
# res = bohb.run(n_iterations=100)
#
# # Step 4: Shutdown
# # After the optimizer run, we must shutdown the master and the nameserver.
# bohb.shutdown(shutdown_workers=True)
# NS.shutdown()
#
# # Step 5: Analysis
# # Each optimizer returns a hpbandster.core.result.Result object.
# # It holds informations about the optimization run like the incumbent (=best) configuration.
# # For further details about the Result object, see its documentation.
# # Here we simply print out the best config and some statistics about the performed runs.
# id2config = res.get_id2config_mapping()
# incumbent = res.get_incumbent_id()
#
# print('Best found configuration:', id2config[incumbent]['config'])
# print('A total of %i unique configurations where sampled.' % len(id2config.keys()))
# print('A total of %i runs where executed.' % len(res.get_all_runs()))




# ### Using Hyperopt ATPE search
#     hyperopt_objective3 = SixHumpCamelBack(functionProperties=SixHumpCamelBack.functionProperties,
#     sd=0,
#     maxfeval=100)
#     space = [hp.uniform('x1',-1,1),hp.uniform('x2',-1,1)]
#     best = fmin(fn=hyperopt_objective2,
#         space= space,
#         algo=atpe.suggest,
#         max_evals=100)
#     print(best)






#### Using the NiaPY
# task = StoppingTask(D=10, nFES=maxfeval, benchmark=Sphere())
# mysphere = Sphere(Lower=-1, Upper=1)
# print(mysphere.Lower)
# print(mysphere.Upper)
# algo = GreyWolfOptimizer(NP=40)
# best = algo.run(task)
# print(best)






#BAYOPT

# func = GPyOpt.objective_examples.experiments1d.forrester()
# domain = [{'name': 'var1', 'type': 'continuous', 'domain': (0, 1)}]
# X_init = np.array([[0.0], [0.5], [1.0]])
# Y_init = func.f(X_init)
# print('Xinit : ', X_init)
# print('Yinit : ', Y_init)
# iter_count = 10
# current_iter = 0
# X_step = X_init
# Y_step = Y_init
#
# while current_iter < iter_count:
#     bo_step = GPyOpt.methods.BayesianOptimization(f=None, domain=domain, X=X_step, Y=Y_step)
#     x_next = bo_step.suggest_next_locations()
#     print('x_next', x_next)
#     y_next = func.f(x_next)
#     print('y_next', y_next)
#     X_step = np.vstack((X_step, x_next))
#     Y_step = np.vstack((Y_step, y_next))
#
#     current_iter += 1

# max_iter = 15
# x0=objective.functionProperties['x0']
# X_init = np.array([x0])
# Y_init = np.array([[objective(x0)]])
# print('Xinit : ', X_init)
# print('Yinit : ', Y_init)
# iter_count = 10
# current_iter = 0
# X_step = X_init
# Y_step = Y_init
# bounds = [{'name': 'x1', 'type': 'continuous', 'domain': (-100, 100)},
#           {'name': 'x2', 'type': 'continuous', 'domain': (-100, 100)}]
# while current_iter < iter_count:
#     bo_step = GPyOpt.methods.BayesianOptimization(f=None, domain=bounds,
#                                                   X=X_step,
#                                                   Y=Y_step,
#                                                   exact_feval=False,
#                                                   acquisition_type='EI')
#     x_next = bo_step.suggest_next_locations()
#     print('x_next', x_next)
#     y_next = objective(x_next[0])
#     print('y_next', y_next)
#     X_step = np.vstack((X_step, x_next))
#     Y_step = np.vstack((Y_step, y_next))
#
#     current_iter += 1
#
# bo_step = GPyOpt.methods.BayesianOptimization(f=None, domain=bounds,
#                                               X=X_step,
#                                               Y=Y_step,
#                                               exact_feval=False,
#                                               acquisition_type='EI')
# bo_step._compute_results()
# print('x_opt: ', bo_step.x_opt)



