import numpy as np
import logging
from timeit import default_timer as timer
logger = logging.getLogger(__name__)
logger.propagate = False
from abc import ABC, abstractmethod
from multiprocessing import Process, Queue


class Algorithm(ABC):
        """
        This is the class that implements all the simulations
        The class initializes receiving a CostFunction class as parameter and other simulation parameters such as number of iterations, noise and simulation

        To extend we implement a new function that loops thorugh the number of iterations and give the output result
        This result must be saved and appended in the results vector
        """

        def __init__(self, algorithm_name, objective, maxfeval):
            self.objective = objective # This is the instantiated objective
            # number of iterations for the algorithm. Number of function evaluations
            self.maxfeval = maxfeval
            self.results = []
            self.algorithm_name= algorithm_name


        def run(self,timeout):
            """
            Optimize the algorithm
            """

            self.assemblespace()
            start = timer()
            if self.algorithm_name in['BOHB', 'HyperBand']:
                best_arm, success  = self.optimizeInSeparateProcess(timeout=timeout)
            else:
                best_arm, success, self.objective = self.optimizeInSeparateProcess(timeout=timeout)

            end = timer()
            timetocomplete = end - start
            result = self.objective.GenerateInfo(best_arm=best_arm,
                                                 timetocomplete=timetocomplete,
                                                 algorithm_name=self.algorithm_name,
                                                 success=success)
            return result

        def optimizeProcess(self, queue):
            #Because BOHB and Hyperband are not working this way
            if self.algorithm_name in ['BOHB', 'HyperBand']:
                best_arm, success = self.optimize()
                queue.put((best_arm, success))
            else:
                best_arm, success, self.objective = self.optimize()
                queue.put((best_arm, success, self.objective))

        def optimizeInSeparateProcess(self, timeout):
            queue = Queue()
            p = Process(target=self.optimizeProcess, args=(queue,))
            if self.algorithm_name in ['BOHB', 'HyperBand']:
                try:
                    p.start()
                    p.join(timeout)  # this blocks until the process terminates
                    best_arm, success = queue.get()
                    if success:
                        logger.info('Algorithm '+ str(self.algorithm_name) +' terminated succesfully')
                    else:
                        logger.info('Algorithm ' + str(self.algorithm_name) + ' failed to give a result')
                    return best_arm, success
                except:
                    print('Process failed')
                    exitcode = p.exitcode
                    logger.critical('Error with the optimization process thread in ' + str(self.algorithm_name) + ' with cost function '+ str(self.objective.GetCostFunctionName()))
                    logger.critical('Process terminated with exit code ' + str(exitcode))
                    best_arm, success = np.nan, False
                    return best_arm, success
            else:
                try:
                    p.start()
                    p.join(timeout)  # this blocks until the process terminates
                    best_arm, success, self.objective = queue.get()
                    if success:
                        logger.info('Algorithm '+ str(self.algorithm_name) +' terminated succesfully')
                    else:
                        logger.info('Algorithm ' + str(self.algorithm_name) + ' failed to give a result')
                    return best_arm, success,self.objective
                except:
                    print('Process failed')
                    exitcode = p.exitcode
                    logger.critical('Error with the optimization process thread in ' + str(self.algorithm_name) + ' with cost function '+ str(self.objective.GetCostFunctionName()))
                    logger.critical('Process terminated with exit code ' + str(exitcode))
                    best_arm, success = np.nan, False
                    return best_arm, success, self.objective

        @abstractmethod
        def optimize(self):
            pass

        @abstractmethod
        def assemblespace(self):
            pass
