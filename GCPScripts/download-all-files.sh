#!/bin/bash
#we copy from the folder $1 in the bucket to $2 locally
gsutil -m cp -r gs://hypercom-experiment-data-europe-west1/$1 ./data/