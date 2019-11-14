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