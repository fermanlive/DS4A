#!/bin/bash -e
#
# Install this repository in the current directory

# Remove already existing virtualenv
if [ -d "venv" ]; then rm -Rf venv; fi

# Create virtualenv "venv"
virtualenv venv --python=python3.8

# Activate the environment
source venv/bin/activate

pip install -U pip

# Install repository
#pip install -r requirements.txt