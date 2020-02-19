from Algorithms import Algorithm
#SMAC3
import numpy as np
from smac.configspace import ConfigurationSpace
from ConfigSpace.hyperparameters import UniformFloatHyperparameter
# Import SMAC-utilities
from smac.scenario.scenario import Scenario
from smac.facade.smac_hpo_facade import SMAC4HPO
from utils import *
import copy
import logging
logger = logging.getLogger('Algorithms')

__all__ = ['SMAC']

class SMAC(Algorithm):
    """
    Implement the algorithms of the SMAC package

    Parameters from the super class to keep track

    """

    def __init__(self, objective, maxfeval):
        super().__init__(algorithm_name='SMAC', objective=objective, maxfeval=maxfeval)

    def assemblespace(self):
        """
        We need to create a variable self.space to store the space to be used by the algorithm
        Changes between algorithms

        """
        try:
            obj_space = self.objective.functionProperties['searchSpace']
            self.x0 = self.objective.functionProperties['x0']
            obj_space_type = self.objective.functionProperties['spaceType']

            # assembling the space
            self.cs = ConfigurationSpace()

            i = 0
            self.space = []
            for dim_i in obj_space:
                spc = None
                varname = 'x' + str(i)
                if obj_space_type[i] == 'uniform':
                    spc = UniformFloatHyperparameter(varname, dim_i[0], dim_i[1], default_value=self.x0[i])
                    # spc = (dim_i[0], dim_i[1])
                # TODO: categorical
                if obj_space_type[i] == 'categorical':
                    logger.error('Functionality not implemented yet')
                    raise TypeError('This algorithm doesnt accept categorical variables yet')
                self.space.append(spc)
                i = i + 1
            self.cs.add_hyperparameters(self.space)

            # # Scenario object
            self.scenario = Scenario({"run_obj": "quality",  # we optimize quality (alternatively runtime)
                                 "runcount-limit": self.maxfeval,
                                 # max. number of function evaluations; for this example set to a low number
                                 "cs": self.cs,  # configuration space
                                 "deterministic": "false"
                                 })
        except:
            logger.error('Error assembling the space for ' + str(self.algorithm_name) + ' with cost function: ' + str(
                self.objective.GetCostFunctionName()))
            pass

    def optimize(self):
        """
        The main optimization procedure
        Should return the best arm as and array/ list
        :return:

        THe instance to be optimized is the self.objective value
        """
        #it is quite weird how the the smac and tae runner does with the objective function
        #it kind of only uses a deep copy of the objective and reinstantiate it so the logging does not work well
        #So I am retrivieving these values after occuring and re-assembling the objective function
        try:
            smac = SMAC4HPO(scenario=self.scenario,
                            tae_runner=self.objective)
            xopt = smac.optimize()
            self.objective.outputValues = smac.get_X_y()[1].tolist()
            self.objective.requestedArms = smac.get_X_y()[0].tolist()
            self.objective._nfeval = len(self.objective.outputValues)
            best_arm = convertToArray(xopt)
            success = True
        except:
            logger.warning('Optimization for ' + str(self.algorithm_name) + ' failed with cost function: ' + str(
                self.objective.GetCostFunctionName()))
            best_arm = NAN
            success = False
        return best_arm, success, self.objective
