#!/bin/bash

if [[ $TRAVIS_OS_NAME == 'osx' ]]; then
  brew update
  
  wget https://repo.continuum.io/miniconda/Miniconda3-3.7.0-Linux-x86_64.sh -O ~/miniconda.sh
  bash ~/miniconda.sh -b -p $HOME/miniconda
  export PATH="$HOME/miniconda/bin:$PATH"
  
  conda create --yes -q -n build-env python=$PYTHON
fi
