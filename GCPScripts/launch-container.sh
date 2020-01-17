#!/bin/bash
#one argument that is the instance name
#Here we are launching the latests container in a new configured virtual machine in GCP

#we use this script as launch-container nameofisntance
#!/bin/bash
#we use this script as launch-container nameofisntance
gcloud beta compute instances create-with-container $1 \
  --zone=europe-north1-a \
  --machine-type=n1-standard-4   \
  --service-account=387854631027-compute@developer.gserviceaccount.com  \
  --metadata=google-logging-enabled=true \
  --service-account=script@hypercomp.iam.gserviceaccount.com \
  --scopes=https://www.googleapis.com/auth/cloud-platform \
  --image=cos-stable-79-12607-80-0 \
  --image-project=cos-cloud \
  --container-privileged \
  --container-env GCP_INSTANCE_NAME=$1 \
  --container-env-file=./ExpGroupEnvSetup/$1.txt  \
  --container-image=eu.gcr.io/hypercomp/launcher:latest \
  --container-arg=main1