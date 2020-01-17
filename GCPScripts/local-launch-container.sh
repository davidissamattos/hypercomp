#!/bin/bash
#one argument that is the instance name
#Here we are launching the latests container in a new configured virtual machine in GCP

#we use this script as launch-container nameofisntance
#!/bin/bash
#we use this script as launch-container nameofisntance


docker run --env-file=./ExpGroupEnvSetup/$1.txt --env GCP_INSTANCE_NAME=$1 hypercomp run-env