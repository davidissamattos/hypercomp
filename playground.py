import logging
import colorlog
handler = logging.StreamHandler()
LOG_LEVEL = logging.INFO
LOGFORMAT = "  %(log_color)s%(levelname)-8s%(reset)s | %(log_color)s%(message)s%(reset)s"
handler.setFormatter(colorlog.ColoredFormatter(LOGFORMAT))


#Specifying which files I want with log levels
logger = logging.getLogger(__name__)
algorithm_logger = logging.getLogger('Algorithm')
costfunctions_logger = logging.getLogger('CostFunctions')
comparator_logger = logging.getLogger('Comparator')

#handlers
logger.addHandler(handler)
algorithm_logger.addHandler(handler)
costfunctions_logger.addHandler(handler)
comparator_logger.addHandler(handler)

#levels per file
logger.setLevel(LOG_LEVEL)
algorithm_logger.setLevel(LOG_LEVEL)
costfunctions_logger.setLevel(LOG_LEVEL)
comparator_logger.setLevel(LOG_LEVEL)

#removing progagation from loggers
logger.propagate = False
algorithm_logger.propagate = False
costfunctions_logger.propagate = False
comparator_logger.propagate = False



from CostFunctions import *


from Comparator import *
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'gcpcredentials.json'


if __name__ == '__main__':

    maxfeval =1000
    nsim=1
    sd=0



    # sim = Comparator(objFuncClass=Easom,
    #                      results_folder='data',
    #                      filename = 'test.csv',
    #                      sd=0,
    #                      maxfeval=10,
    #                      nsim=1,
    #                  useGCP=True,
    #                  GCPbucketName='hypercomp-experiment-data')DeVilliersGlasser01

    func = SixHumpCamelBack(functionProperties=SixHumpCamelBack.functionProperties,maxfeval=100, sd=0)
    print('Best ',[-0.0898, 0.7126],' ' ,func([-0.0898, 0.7126]))
    print(func([0, 0]))
    print(func([1, 1]))
    print(func([-1, -1]))

    sim = Comparator(objFuncClass=SixHumpCamelBack,
                         results_folder='data',
                         filename ='test.csv',
                         sd=sd,
                         maxfeval=maxfeval,
                         nsim=nsim,
                         timeout_min=15)
    #
    # sim.run()
    # logger.info('My info')
    # logger.debug('My debug')
    # logger.warning('My warning')
    # logger.critical('My critical')

    from Algorithms.SMAC import SMAC
    from Algorithms.HpbandsterAlgorithms import hpbandsterHyperBand, hpbandsterBOHB
    # from Algorithms.Hyperopt import RandomSearch

    # sim.run_algorithm(hpbandsterHyperBand)
    # sim.run_algorithm(hpbandsterBOHB)
    # sim.run_algorithm(SMAC)


    # from Algorithms.NiaPy import NiaPyABC
    # sim.run_algorithm(NiaPyABC)

    from Algorithms.mLGHOO import mLGHOO
    sim.run_algorithm(mLGHOO)














