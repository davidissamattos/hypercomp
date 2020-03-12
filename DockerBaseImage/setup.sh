#!/bin/bash
echo "Installing Basics"
  apt-get update
  apt-get install git cmake build-essential swig -y apt-utils


echo "Installing Python3.6 packages"
  apt-get install -y python3-pip
  python3 -m pip install --upgrade pip
  python3 -m pip install --upgrade setuptools
  python3 -m pip install -r requirements.txt