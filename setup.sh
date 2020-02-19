#!/bin/bash
echo "Provisioning virtual machine..."
echo "Installing Basics"
echo "Current folder"
ls
    apt-get update
    apt-get install git cmake build-essential swig -y apt-utils
    cd $1

echo "Installing Python3.6 packages"
    apt-get install -y python3-pip
    python3 -m pip install --upgrade pip
    python3 -m pip install --upgrade setuptools
    python3 -m pip install -r requirements.txt