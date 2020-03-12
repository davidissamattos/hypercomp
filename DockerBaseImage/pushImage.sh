#!/bin/bash
echo "Building image"
docker build --tag davidissamattos/hypercomp_base .
echo "Pushing image"
docker push davidissamattos/hypercomp_base
echo "Done"