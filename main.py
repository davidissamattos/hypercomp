#!/usr/bin/env python

import sys, os
import click
import importlib

# os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'gcpcredentials.json'

from CostFunctions import all_benchmarks as bm
from Comparator import *
from CostFunctions import *

if sys.version_info[0] < 3:
    raise Exception("Must be using Python 3")

@click.group()
def hypercomp():
    pass

@hypercomp.command()
@click.option('--path', '-p', default=None, type=str, help='Specify the path to save the data. Default value is in the current location')
@click.option('--nsim', '-n', default=1, type=int, help='Specify the number of time the same function will be simulated by the same algorithm. Default value is 1. For statistical analysis it is recommended at least 30.')
@click.option('--sd', required=True, type=float, help='Specify the standard deviation used in the cost functions. The same value will be used for all')
@click.option('--maxfeval', required=True, type=int,  help='Specify the maximum number of evaluations for the cost function for each algorithm. This is the budget. Same budget will be used for all algorithms and functions')
@click.option('--maxfevalBydimensions', default=False, type=bool, help='Specify if the algorithm is going to be run with maximum function evaluations dependent on the dimensions of the problem')
def run_all(sd,maxfeval,path,nsim,maxfevalbydimensions):
    runcomp(sd=sd,
            maxfeval=maxfeval,
            path=path,
            nsim=nsim,
            maxfevalBydimensions=maxfevalbydimensions,
            func='all')

@hypercomp.command()
@click.option('--path', '-p', default=None, type=str, help='Specify the path to save the data. Default value is in the current location')
@click.option('--nsim', '-n', default=1, type=int, help='Specify the number of time the same function will be simulated by the same algorithm. Default value is 1. For statistical analysis it is recommended at least 30.')
@click.option('--sd', required=True, type=float, help='Specify the standard deviation used in the cost functions. The same value will be used for all')
@click.option('--maxfeval', required=True, type=int,  help='Specify the maximum number of evaluations for the cost function for each algorithm. This is the budget. Same budget will be used for all algorithms and functions')
@click.option('--maxfevalBydimensions', default=False, type=bool, help='Specify if the algorithm is going to be run with maximum function evaluations dependent on the dimensions of the problem')
@click.option('--func', default='all',required=True, type=str, help='Specify only one the available cost functions by the name or all for all functions')
def run_function(sd,maxfeval,path,nsim,maxfevalbydimensions,func):
    runcomp(sd=sd,
            maxfeval=maxfeval,
            path=path,
            nsim=nsim,
            maxfevalBydimensions=maxfevalbydimensions,
            func=func)


@hypercomp.command()
@click.option('--path', '-p', default=None, type=str, help='Specify the path to save the data. Default value is in the current location')
@click.option('--nsim', '-n', default=1, type=int, help='Specify the number of time the same function will be simulated by the same algorithm. Default value is 1. For statistical analysis it is recommended at least 30.')
@click.option('--sd', required=True, type=float, help='Specify the standard deviation used in the cost functions. The same value will be used for all')
@click.option('--maxfeval', required=True, type=int,  help='Specify the maximum number of evaluations for the cost function for each algorithm. This is the budget. Same budget will be used for all algorithms and functions')
@click.option('--maxfevalBydimensions', default=False, type=bool, help='Specify if the algorithm is going to be run with maximum function evaluations dependent on the dimensions of the problem')
@click.option('--funcrange', nargs=2, required=True, type=(int, int),  help='Specify a range of the list of functions that we will run. This is a two value argument. Varies from 0 to ?. Values should be an integer')
def run_range(sd,maxfeval,path,nsim,maxfevalbydimensions,funcrange):
    runcomp(sd=sd,
            maxfeval=maxfeval,
            path=path,
            nsim=nsim,
            maxfevalBydimensions=maxfevalbydimensions,
            funcrange=funcrange)

def runcomp(sd=0, maxfeval=30, path=None, nsim=1, func=None, funcrange=None, maxfevalBydimensions=False):
    #defining the scope of functions to run
    benchmark=[]
    maxfeval = int(maxfeval)
    nsim = int(nsim)
    if path==None:
        path = os.getcwd()
    elif not os.path.isdir(path):
        path = os.getcwd()
        print('Path does not exist. Using the current working directory')
    if funcrange==None:
        if func=='all' or func==None:
            benchmark = bm
        elif func in bm:
            benchmark=[func]
    else:
        minRange, maxRange = funcrange
        if minRange<0:
            raise Exception("Minimum range value should be 0")
        elif maxRange > len(bm):
            raise Exception("Maximum range value should smaller or equal: " + str(len(bm)))
        else:
            benchmark =bm[int(minRange),int(maxRange)]

    for cname in benchmark:
        module = importlib.import_module('CostFunctions')
        cl = getattr(module, cname) #cl is a class of the CostFunctions imported dynamically
        filename = cname + '-sd-' + str(sd) + '-feval-' + str(maxfeval) + '-nsim-' + str(nsim) + '.csv'
        sim = Comparator(objFuncClass=cl,
                         results_folder=path,
                         filename = filename,
                         sd=sd,
                         maxfevalBydimensions=maxfevalBydimensions,
                         maxfeval=maxfeval,
                         nsim=nsim)
        sim.run()

if __name__ == "__main__":
    hypercomp()