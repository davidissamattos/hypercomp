#!/usr/bin/env python

import sys, os
import click
import importlib

import logging
import colorlog
handler = logging.StreamHandler()
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



#removing progagation from loggers
logger.propagate = False
algorithm_logger.propagate = False
costfunctions_logger.propagate = False
comparator_logger.propagate = False


from tqdm import tqdm

from CostFunctions import all_benchmarks as bm
from Comparator import *


if sys.version_info[0] < 3:
    raise Exception("Must be using Python 3")

@click.group()
def hypercomp():
    pass

#This is the main command, the others are mostly for debugging
@hypercomp.command()
@click.option('--sd', required=True, type=float, help='(REQUIRED) Specify the standard deviation used in the cost functions. The same value will be used for all')
@click.option('--maxfeval', required=True, type=int,  help='(REQUIRED) Specify the maximum number of evaluations for the cost function for each algorithm. This is the budget. Same budget will be used for all algorithms and functions')
@click.option('--path', '-p', default=None, required=False,type=str, help='Specify the path to save the data. Default value is in the current location')
@click.option('--nsim', '-n', default=1, required=False, type=int, help=' Specify the number of time the same function will be simulated by the same algorithm. Default value is 1. For statistical analysis it is recommended at least 30.')
@click.option('--maxfevalBydimensions', default=False, required=False, type=bool, help='Specify if the algorithm is going to be run with maximum function evaluations dependent on the dimensions of the problem')
@click.option('--usegcp', default=False,required=False, type=bool, help='Save results in GCP')
@click.option('--gcpcredentials', default=None, required=False, type=str, help='Path to the credentials if needed')
@click.option('--bucketname', default=None, required=False, type=str, help='GCP bucket name')
@click.option('--funcrange', nargs=2, required=False, type=int,  help='Specify a range of the list of functions that we will run. This is a two value argument. Varies from 0 to ?. Values should be an integer')
@click.option('--func', default='all',required=False, type=str, help='Specify only one the available cost functions by the name or all for all functions')
@click.option('--timeout', default=15,required=False, type=int, help='Time in minutes. Specify the timeout for one algorithm to optimize one function. Default is 15min.')
@click.option('--loglevel', default='info', required=False, type=str, help='Specify the level of information that appears on the screen, equal to the logging levels in python. Default value is info. Possible values: debug, info, warning, critical, error')
def run(sd,maxfeval,path,nsim,maxfevalbydimensions,usegcp,gcpcredentials,bucketname,funcrange,func,timeout, loglevel):

    #configuring log level
    # levels per file

    loglevel = loglevel.lower()
    if loglevel == 'debug':
        LOG_LEVEL = logging.DEBUG
    elif loglevel == 'info':
        LOG_LEVEL = logging.INFO
    elif loglevel == 'warning':
        LOG_LEVEL = logging.WARNING
    elif loglevel == 'critical':
        LOG_LEVEL = logging.CRITICAL
    elif loglevel == 'error':
        LOG_LEVEL = logging.ERROR
    print('Using log level type: ' + loglevel)
    logger.setLevel(LOG_LEVEL)
    algorithm_logger.setLevel(LOG_LEVEL)
    costfunctions_logger.setLevel(LOG_LEVEL)
    comparator_logger.setLevel(LOG_LEVEL)


    # defining the scope of functions to run
    benchmark = []
    maxfeval = int(maxfeval)
    nsim = int(nsim)

    # Dealing with the path
    if path == None:
        path = os.getcwd()
    elif not os.path.isdir(path):
        path = os.getcwd()
        logger.info('Path does not exist. Using the current working directory')

    ##Dealing with func and funcrange
    # If the function range option is empty (tuple has size zero) we say ignore it
    if len(funcrange)==0:
        if func == 'all' or func == None:
            benchmark = bm
        elif func in bm:
            benchmark = [func]
        else:
            logger.error('The function selected is not valid. It should be included in: '+str(bm))
            raise Exception

    #Tuple is not empty
    else:
        minRange, maxRange = funcrange
        if minRange==None:
            minRange=0
        if maxRange==None:
            maxRange = len(bm)
        minRange = int(minRange)
        maxRange = int(maxRange)
        if minRange < 0:
            logger.error("Minimum range value should be 0")
            raise Exception
        elif maxRange > len(bm):
            logger.error("Maximum range value should smaller or equal: " + str(len(bm)))
            raise Exception
        else:
            logger.info('Using only functions in range: '+ str(minRange)+ ' '+ str(maxRange))
            benchmark = bm[minRange:maxRange]

    if usegcp:
        if os.environ.get('GOOGLE_APPLICATION_CREDENTIALS') is None:
            try:
                os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = gcpcredentials
            except:
                logger.error("Could not find the credentials")
                raise KeyError('Could not find the credentials')

    for cname in tqdm(benchmark):
        module = importlib.import_module('CostFunctions')
        cl = getattr(module, cname)  # cl is a class of the CostFunctions imported dynamically
        filename = cname + '-sd-' + str(sd) + '-feval-' + str(maxfeval) + '-nsim-' + str(nsim) + '.csv'
        sim = Comparator(objFuncClass=cl,
                         results_folder=path,
                         filename=filename,
                         sd=sd,
                         maxfevalBydimensions=maxfevalbydimensions,
                         maxfeval=maxfeval,
                         nsim=nsim,
                         useGCP=usegcp,
                         GCPbucketName=bucketname,
                         timeout_min=timeout)
        sim.run()

@hypercomp.command()
def listAllFunctions():
    print('The benchmark functions available at the moment are: ', bm)

if __name__ == "__main__":
    hypercomp()