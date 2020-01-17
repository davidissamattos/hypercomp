from Algorithms import Algorithm
from utils import *
import logging
logger = logging.getLogger('Algorithms')


__all__ = ['RandomSearch2','RandomSearch4','RandomSearch10']

class RandomSearchN(Algorithm):
    """
    Runs several algorithms from the NiaPy package
        The default values  comes from the Jie-ShengWang & Shu-Xia Li paper

    """

    def __init__(self, algorithm_name, objective, maxfeval, N):
        super().__init__(algorithm_name, objective, maxfeval)
        self.N = N
        self.algorithm_name = algorithm_name


    def assemblespace(self):
        """
        We need to create a variable self.space to store the space to be used by the algorithm
        Changes between algorithms

        """
        try:
            self.obj_space = self.objective.functionProperties['searchSpace']
            self.x0 = self.objective.functionProperties['x0']
            # print(self.obj_space)

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
        best_arm = self.x0
        best_f = self.objective(best_arm)
        # print('Initial best arm and best f: ', best_arm, best_f)

        try:
            for i in range(int(np.floor(self.maxfeval/self.N) - 1)):
                #this is the sample we will test
                new_arm = []
                for v in self.obj_space:
                    low = v[0]
                    high = v[1]
                    new_arm.append(np.random.uniform(low=low, high=high, size=1)[0])

                new_f_vector = []
                for j in range(self.N):
                    new_f_vector.append(self.objective(new_arm))

                new_f = np.mean(new_f_vector)
                # print(new_f_vector, new_f)

                if new_f < best_f: #here we check if we got a lower value
                    # print('Before was: ', best_arm, best_f)
                    best_arm = new_arm
                    best_f = new_f
                    # print('Now is: ', best_arm, best_f)

            success = True
            best_arm = convertToArray(best_arm)
        except:
            logger.warning('Optimization for ' + str(self.algorithm_name) + ' failed.')
            best_arm = NAN
            success = False

        return best_arm, success


class RandomSearch2(RandomSearchN):
    def __init__(self, objective, maxfeval):
        super().__init__(objective=objective,
                         maxfeval=maxfeval,
                         algorithm_name='RandomSearch2', N=2)

class RandomSearch4(RandomSearchN):
    def __init__(self, objective, maxfeval):
        super().__init__(objective=objective,
                         maxfeval=maxfeval,
                         algorithm_name='RandomSearch4', N=4)

class RandomSearch10(RandomSearchN):
    def __init__(self, objective, maxfeval):
        super().__init__(objective=objective,
                         maxfeval=maxfeval,
                         algorithm_name='RandomSearch10', N=10)