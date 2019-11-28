import numpy as np
import pandas as pd
import logging
from timeit import default_timer as timer
logging.basicConfig(level=logging.CRITICAL)
logger = logging.getLogger(__name__)
import os, re, shutil
from abc import ABC, abstractmethod

#GoogleCloud bucket
from google.cloud import storage
# say where your private key to google cloud exists

from CostFunctions import *
from utils import *

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

        def run(self):
            """
            Optimize the algorithm
            """
            print('Starting to run algorithm: ', str(self.algorithm_name))
            self.assemblespace()
            start = timer()
            best_arm = self.optimize()
            end = timer()
            timetocomplete = end - start
            result = self.objective.GenerateInfo(best_arm=best_arm,
                                                 timetocomplete = timetocomplete,
                                                 algorithm_name=self.algorithm_name)
            return result


        @abstractmethod
        def optimize(self):
            pass

        @abstractmethod
        def assemblespace(self):
            pass
