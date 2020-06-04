#!/bin/bash
#we copy from the folder $1 in the bucket to local
gsutil -m cp -r gs://hypercom-experiment-data-europe-west1/$1 ./DataAnalysis/