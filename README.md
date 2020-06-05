# HyperComp
A package for simulating a number of different algorithms for black-box optimization of expensive functions against several benchmark functions

## Pre-requisites
* Dockerfile create a VM with everything configure 
* if using GCP you neeed a gcpcredentials.json file

# Usage
Utilize the main.py file with the appropriate options
Type main.py --help to get a help menu
Or read through the main to see which environment options to choose


# Development
The package CostFunctions contain all the benchmark functions used for comparisons.
All cost functions inherit from the CostFunctions class. This base class do most of the logging and measurement so it is not a responsibility of each package. This way we also adjust to make sure we are measuring the same thing with every package
New algorithms should inherit from the Algorithms class


# Deployments
We suggest using the docker image to launch independent machines for each experimental group 

# Notes
* When installing everything from requirements.txt the ConfigSpace package will fail but later it will work...

## Files
* playground.py a file to test if everything is working properly
* package_snippets.py nothing relevant. Just some helper snippets commented
* hypercomp.py This file contains a class that calls all the algorithms. It receives only a function subclassed from the CostFunctions package, sd for the noise, maximum of function evaluations and number of times everything is simulated
* CostFunctions.py Class that implements the benchmark functions. All log functionalities are implemented here

