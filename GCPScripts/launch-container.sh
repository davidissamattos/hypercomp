#!/bin/bash
#one argument that is the instance name
#Here we are launching the latests container in a new configured virtual machine in GCP
# Here we are using a high performance with high CPU and medium memory machine
#it costs approximately 4sek an hour
#we use this script as launch-container nameofisntance
#!/bin/bash
#we use this script as launch-container nameofisntance
echo "Launching container using configuration file from folder: "
echo $1
echo "File: "
echo $2
gcloud beta compute instances create-with-container $2 \
  --zone=europe-west1-b \
  --machine-type=n1-standard-4 \
  --network-tier=PREMIUM \
  --service-account=387854631027-compute@developer.gserviceaccount.com  \
  --metadata=google-logging-enabled=true \
  --service-account=script@hypercomp.iam.gserviceaccount.com \
  --scopes=https://www.googleapis.com/auth/cloud-platform \
  --image=cos-stable-81-12871-96-0 \
  --image-project=cos-cloud \
  --container-privileged \
  --container-env GCP_INSTANCE_NAME=$2 \
  --container-env-file=$1/$2.env  \
  --container-image=eu.gcr.io/hypercomp/launcher:latest \
  --container-arg=runenv


  #some alternatives
  #  --machine-type=n1-highcpu-16 \