from Algorithms import Algorithm
import GPy
import GPyOpt
from GPyOpt.methods import BayesianOptimization
from GPyOpt.experiment_design import initial_design
from utils import *
import logging
logger = logging.getLogger('Algorithms')

__all__ = ['BayesOptEIRandom', 'BayesOptEILatin', 'BayesOptLCBRandom', 'BayesOptLCBLatin', 'BayesOptMPIRandom', 'BayesOptMPILatin']

class BayesOpt(Algorithm):
    """
    From the GPyOpt package
    """
    def __init__(self, objective, maxfeval, acquisition_function, model_type, initial_design_type):

        self.algorithm_name = 'BO-' + str(acquisition_function) + '-' + str(model_type) + '-' + str(initial_design_type)

        super().__init__(self.algorithm_name, objective, maxfeval)

        self.acquisition_function = acquisition_function
        self.model_type = model_type
        self.initial_design_type = initial_design_type

        self.algo = None  # this is the suggest function from hyperopt
        if acquisition_function not in ['EI', 'LCB', 'MPI']:
            logger.error('GPyOpt does not have acquisition function :' + str(acquisition_function))
            raise Exception
        if model_type not in ['GP']:
            logger.error('GPyOpt does not have model_type :' + str(model_type))
            raise Exception
        if initial_design_type not in ['latin', 'random']:
            logger.error('GPyOpt does not have initial_design_type :' + str(initial_design_type))
            raise Exception

    def assemblespace(self):
        """
        We need to create a variable self.space to store the space to be used by the algorithm
        Changes between algorithms

        """
        try:
            obj_space = self.objective.functionProperties['searchSpace']
            obj_space_type = self.objective.functionProperties['spaceType']
            self.x0 = self.objective.functionProperties['x0']

            # assembling the space
            i = 0
            self.space = []
            for dim_i in obj_space:
                spc = {}
                varname = 'x' + str(i)
                if obj_space_type[i] == 'uniform':
                    spc['name'] = varname
                    spc['type'] = 'continuous'
                    spc['domain'] = (dim_i[0], dim_i[1])
                # TODO: categorical
                if obj_space_type[i] == 'categorical':
                    raise TypeError('This algorithm doesnt accept categorical variables yet')
                self.space.append(spc)
                i = i + 1
        except:
            logger.error('Error assembling the space for ' + str(self.algorithm_name) + ' with cost function: ' + str(
                self.objective.GetCostFunctionName()))
            #since it will fail later in the optimize function we pass here
            pass

    def optimize(self):
        """
        The main optimization procedure
        Should return the best arm as and array/ list
        :return:

        THe instance to be optimized is the self.objective value
        """
        try:
            X_init = np.array([self.x0])
            Y_init = np.array([[self.objective(self.x0)]])
            X_step = X_init
            Y_step = Y_init
            for i in range(self.maxfeval - 1):  # because one evaluation was already computed for the start
                bo_step = GPyOpt.methods.BayesianOptimization(f=None, domain=self.space,
                                                              X=X_step,
                                                              Y=Y_step,
                                                              initial_design_type=self.initial_design_type,
                                                              exact_feval=False,  # the outputs are not exect
                                                              model_type=self.model_type,
                                                              acquisition_type=self.acquisition_function,
                                                              verbosity=False,
                                                              verbosity_model=False)
                x_next = bo_step.suggest_next_locations()
                y_next = self.objective(x_next[0])  # only suggests one and we need to unpack
                X_step = np.vstack((X_step, x_next))
                Y_step = np.vstack((Y_step, y_next))

            # Now we need to compute the results
            bo_step = GPyOpt.methods.BayesianOptimization(f=None, domain=self.space,
                                                          X=X_step,
                                                          Y=Y_step,
                                                          initial_design_type=self.initial_design_type,
                                                          exact_feval=False,  # the outputs are not exect
                                                          model_type=self.model_type,
                                                          acquisition_type=self.acquisition_function)
            bo_step._compute_results()
            best_arm = convertToArray(bo_step.x_opt)
            success = True
        except:
            logger.debug('Optimization for ' + str(self.algorithm_name) + ' failed with cost function: ' + str(
                self.objective.GetCostFunctionName()))
            best_arm = NAN
            success = False
        #Return value should be a list/array
        return best_arm, success, self.objective

class BayesOptEIRandom(BayesOpt):
    def __init__(self, objective, maxfeval):
        super().__init__(objective=objective,
                         maxfeval=maxfeval,
                         acquisition_function='EI',
                         model_type='GP',
                         initial_design_type= 'random')

class BayesOptEILatin(BayesOpt):
    def __init__(self, objective, maxfeval):
        super().__init__(objective=objective,
                         maxfeval=maxfeval,
                         acquisition_function='EI',
                         model_type='GP',
                         initial_design_type='latin')

class BayesOptLCBRandom(BayesOpt):
    def __init__(self, objective, maxfeval):
        super().__init__(objective=objective,
                         maxfeval=maxfeval,
                         acquisition_function='LCB',
                         model_type='GP',
                         initial_design_type= 'random')

class BayesOptLCBLatin(BayesOpt):
    def __init__(self, objective, maxfeval):
        super().__init__(objective=objective,
                         maxfeval=maxfeval,
                         acquisition_function='LCB',
                         model_type='GP',
                         initial_design_type='latin')

class BayesOptMPIRandom(BayesOpt):
    def __init__(self, objective, maxfeval):
        super().__init__(objective=objective,
                         maxfeval=maxfeval,
                         acquisition_function='MPI',
                         model_type='GP',
                         initial_design_type= 'random')

class BayesOptMPILatin(BayesOpt):
    def __init__(self, objective, maxfeval):
        super().__init__(objective=objective,
                         maxfeval=maxfeval,
                         acquisition_function='MPI',
                         model_type='GP',
                         initial_design_type='latin')