#!/bin/bash

#We source this file before we run the script
export HYPERCOMP_SD=0
export HYPERCOMP_MAXFEVAL=30
export HYPERCOMP_PATH=no_bayesian_smalltest
export HYPERCOMP_NSIM=2
export HYPERCOMP_USEGCP=true
export HYPERCOMP_TIMEOUT=5
export HYPERCOMP_LOGLEVEL=warning
export HYPERCOMP_NFEVALBYDIMENSIONS=true
export HYPERCOMP_FUNC=smalltest
export HYPERCOMP_ALGORITHMGROUP=no_bayesian

export GCP_BUCKET=hypercom-experiment-data-europe-west1
export GCP_PROJECT_ID=hypercomp
export GCP_ZONE=europe-west1-b
