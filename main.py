#!/usr/bin/env python
import time
import sys, os
import click
import importlib
import googleapiclient.discovery
import logging
import colorlog

from tqdm import tqdm

from CostFunctions import bbob, bbob_no_n10, smalltest, nobbob, set1, set2,  set3, set4, set5, set6, all_benchmarks
from Comparator import *

if sys.version_info[0] < 3:
    raise Exception("Must be using Python 3")


def setLogLevels(loglevel, usegcp):
    if usegcp:
        import google.cloud.logging
        from google.cloud.logging.handlers import CloudLoggingHandler, setup_logging
        client = google.cloud.logging.Client()
        client.setup_logging()
        handler = CloudLoggingHandler(client)

    else:
        handler = logging.StreamHandler()
        LOGFORMAT = "  %(log_color)s%(levelname)-8s%(reset)s | %(log_color)s%(message)s%(reset)s"
        handler.setFormatter(colorlog.ColoredFormatter(LOGFORMAT))

    # Specifying which files I want with log levels
    logger = logging.getLogger(__name__)
    algorithm_logger = logging.getLogger('Algorithms')
    costfunctions_logger = logging.getLogger('CostFunctions')
    comparator_logger = logging.getLogger('Comparator')


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
    else:
        LOG_LEVEL = logging.INFO
    print('Using log level type: ' + loglevel)

    logger.setLevel(LOG_LEVEL)
    algorithm_logger.setLevel(LOG_LEVEL)
    costfunctions_logger.setLevel(LOG_LEVEL)
    comparator_logger.setLevel(LOG_LEVEL)

    loggers_to_shut_up = [
        "hyperopt.tpe",
        "hyperopt.fmin",
        "hyperopt.pyll.base",
    ]
    for l in loggers_to_shut_up:
        logging.getLogger(l).setLevel(logging.ERROR)

    # handlers
    logger.addHandler(handler)
    algorithm_logger.addHandler(handler)
    costfunctions_logger.addHandler(handler)
    comparator_logger.addHandler(handler)

    # removing progagation from loggers
    logger.propagate = False
    algorithm_logger.propagate = False
    costfunctions_logger.propagate = False
    comparator_logger.propagate = False

#Main function that is called
def run(sd, maxfeval, path, nsim, usegcp, bucketname, funcrange_min,
        funcrange_max, func, timeout, loglevel,nfevalbydimensions,algorithmgroup):
    # configuring log level
    # levels per file
    if usegcp:
        os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = './gcpcredentials.json'
        logger.info('Using GCP')

    setLogLevels(loglevel,usegcp)

    # defining the scope of functions to run
    benchmark = []
    maxfeval = int(maxfeval)
    nsim = int(nsim)

    ##Dealing with func and funcrange
    # If we dont set both ranges
    if funcrange_min == None or funcrange_max == None:
        if func == 'all' or func == None:
            logger.info('Using all benchmark functions')
            benchmark = all_benchmarks
        elif func == 'bbob':
            benchmark = bbob
        elif func == 'set1':
            benchmark = set1
        elif func == 'set2':
            benchmark = set2
        elif func == 'set3':
            benchmark = set3
        elif func == 'set4':
            benchmark = set4
        elif func == 'set5':
            benchmark = set5
        elif func == 'set6':
            benchmark = set6
        elif func == 'bbob_no_n10':
            benchmark = bbob_no_n10
        elif func == 'smalltest':
            benchmark = smalltest
        elif func == 'nobbob':
            benchmark = nobbob
        elif func in all_benchmarks:
            benchmark = [func]
            logger.info('Using only functions : '+str(benchmark))
        else:
            logger.error('The function selected is not valid. It should be included in: ' + str(all_benchmarks))
            raise Exception
    else:
        minRange = funcrange_min
        maxRange = funcrange_max
        if minRange == None:
            minRange = 0
        if maxRange == None:
            maxRange = len(all_benchmarks)
        minRange = int(minRange)
        maxRange = int(maxRange)
        if minRange < 0:
            logger.error("Minimum range value should be 0")
            raise Exception
        elif maxRange > len(all_benchmarks):
            logger.error("Maximum range value should smaller or equal: " + str(len(all_benchmarks)))
            raise Exception
        else:
            logger.info('Using only functions in range: ' + str(minRange) + ' ' + str(maxRange))
            benchmark = all_benchmarks[minRange:maxRange]
            logger.info('Using benchmark functions : ' + str(benchmark))

    logger.info('Using timeout of :' +str(timeout))
    for cname in tqdm(benchmark):
        module = importlib.import_module('CostFunctions')
        cl = getattr(module, cname)  # cl is a class of the CostFunctions imported dynamically
        filename = cname + '-sd-' + str(sd) + '-feval-' + str(maxfeval) + '-i-'
        sim = Comparator(objFuncClass=cl,
                         results_folder=path,
                         filename=filename,
                         sd=sd,
                         maxfeval=maxfeval,
                         nsim=nsim,
                         useGCP=usegcp,
                         GCPbucketName=bucketname,
                         timeout_min=timeout,
                         nfevalbydimensions=nfevalbydimensions,
                         algorithmgroup=algorithmgroup)
        sim.run()


#for command line
@click.group()
def hypercomp():
    pass

# this command we run passing everything as command line arguments in the local pc
@hypercomp.command()
@click.option('--sd', required=True, type=float,
              help='(REQUIRED) Specify the standard deviation used in the cost functions. The same value will be used for all')
@click.option('--maxfeval', required=True, type=int,
              help='(REQUIRED) Specify the maximum number of evaluations for the cost function for each algorithm. This is the budget. Same budget will be used for all algorithms and functions')
@click.option('--path', '-p', default=None, required=True, type=str,
              help='Specify a true an exisitng path to save the data')
@click.option('--nsim', '-n', default=1, required=False, type=int,
              help=' Specify the number of time the same function will be simulated by the same algorithm. Default value is 1. For statistical analysis it is recommended at least 30.')
@click.option('--usegcp', default=False, required=False, type=bool, help='Save results in GCP')
@click.option('--bucketname', default=None, required=False, type=str, help='GCP bucket name')
@click.option('--funcrange_min', required=False, type=int,
              help='Specify the min range of the list of functions that we will run.  Varies from 0 to ?. Values should be an integer')
@click.option('--funcrange_max', required=False, type=int,
              help='Specify the max range of the list of functions that we will run.  Varies from 0 to ?. Values should be an integer')
@click.option('--func', default='all', required=False, type=str,
              help='Specify only one the available cost functions by the name, all for all functions or a specific name defined in the init file of the cost functions e.g. bbob')
@click.option('--timeout', default=15, required=False, type=int,
              help='Time in minutes. Specify the timeout for one algorithm to optimize one function. Default is 15min.')
@click.option('--loglevel', default='info', required=False, type=str,
              help='Specify the level of information that appears on the screen, equal to the logging levels in python. Default value is info. Possible values: debug, info, warning, critical, error')
@click.option('--nfevalbydimensions', default=False, required=False, type=bool,
              help='Specify if the number of function evaluations will depend on the dimensions. If True the maxfeval will be maxfeval*Dimensions')
@click.option('--algorithmgroup', default='all', required=False, type=str,
              help='Specify the group of algorithms to run. Options all, niapy, etc..')
def runcli(sd, maxfeval, path, nsim, usegcp, bucketname, funcrange_min,
            funcrange_max, func, timeout, loglevel,nfevalbydimensions, algorithmgroup):
    run(sd=sd,
        maxfeval=maxfeval,
        path=path,
        nsim=nsim,
        usegcp=usegcp,
        bucketname=bucketname,
        funcrange_min=funcrange_min,
        funcrange_max=funcrange_max,
        func=func,
        timeout=timeout,
        loglevel=loglevel,
        nfevalbydimensions=nfevalbydimensions,
        algorithmgroup=algorithmgroup)


# this we are reading environmental variables --> for running with docker without passing this much arguments
# not recommended
# not fully tested

@hypercomp.command()
def runenv():
    sd = os.environ.get('HYPERCOMP_SD')
    if sd is not None:
        sd = float(sd)
    else:
        sd=0

    maxfeval = os.environ.get('HYPERCOMP_MAXFEVAL')
    if maxfeval is not None:
        maxfeval=int(maxfeval)
    else:
        maxfeval=1

    path = os.environ.get('HYPERCOMP_PATH')
    if path is not None:
        path=str(path)
    else:
        path='data'

    nsim = os.environ.get('HYPERCOMP_NSIM')
    if nsim is not None:
        nsim = int(nsim)
    else:
        nsim=1

    usegcp = os.environ.get('HYPERCOMP_USEGCP')
    if usegcp is not None:
        usegcp=bool(usegcp)
    else:
        usegcp=False

    funcrange_min = os.environ.get('HYPERCOMP_FUNCRANGE_MIN')
    if funcrange_min is not None:
        funcrange_min = int(funcrange_min)

    funcrange_max = os.environ.get('HYPERCOMP_FUNCRANGE_MAX')
    if funcrange_max is not None:
        funcrange_max = int(funcrange_max)

    func = os.environ.get('HYPERCOMP_FUNC')
    print(func)
    if func is not None:
        func=str(func)
    else:
        func='all'

    timeout = os.environ.get('HYPERCOMP_TIMEOUT')
    if timeout is not None:
        timeout=float(timeout)
    else:
        timeout=5

    loglevel = os.environ.get('HYPERCOMP_LOGLEVEL')
    if loglevel is not None:
        loglevel = str(loglevel)
    else:
        loglevel = 'info'

    nfevalbydimensions = os.environ.get('HYPERCOMP_NFEVALBYDIMENSIONS')
    if nfevalbydimensions is not None:
        nfevalbydimensions = bool(nfevalbydimensions)
    else:
        nfevalbydimensions=False

    algorithmgroup = os.environ.get('HYPERCOMP_ALGORITHMGROUP')
    if algorithmgroup is not None:
        algorithmgroup = str(algorithmgroup)
    else:
        algorithmgroup = 'no_bayesian'

    bucketname = os.environ.get('GCP_BUCKET')
    if bucketname is not None:
        bucketname = str(bucketname)

    simproperties={
                'sd' : sd,
                'maxfeval' : maxfeval,
                'path' : path,
                'nsim' : nsim,
                'usegcp' : usegcp,
                'bucketname' : bucketname,
                'funcrange_min' : funcrange_min,
                'funcrange_max' : funcrange_max,
                'func' : func,
                'timeout' : timeout,
                'loglevel' : loglevel,
                'nfevalbydimensions' : nfevalbydimensions,
                'algorithmgroup' : algorithmgroup}

    print('Running with simulator with properties: ',
          simproperties)

    run(sd=sd,
        maxfeval=maxfeval,
        path=path,
        nsim=nsim,
        usegcp=usegcp,
        bucketname=bucketname,
        funcrange_min=funcrange_min,
        funcrange_max=funcrange_max,
        func=func,
        timeout=timeout,
        loglevel=loglevel,
        nfevalbydimensions=nfevalbydimensions,
        algorithmgroup=algorithmgroup)



    def cleanUpGCP():
        compute = googleapiclient.discovery.build('compute', 'v1')
        logging.info('Deleting instance')
        project_id = str(os.environ.get('GCP_PROJECT_ID'))
        zone = str(os.environ.get('GCP_ZONE'))
        instance_name = str(os.environ.get('GCP_INSTANCE_NAME'))

        compute.instances().delete(
            project=project_id,
            zone=zone,
            instance=instance_name).execute()

    #after we run we delete instances if we have any
    time.sleep(60)
    cleanUpGCP()


@hypercomp.command()
def listAllFunctions():
    print('There are: ', len(all_benchmarks), " benchmark functions")
    print('The benchmark functions available are: ', all_benchmarks)


if __name__ == "__main__":
    hypercomp()
