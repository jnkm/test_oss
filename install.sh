#!/bin/bash

if [[ $TRAVIS_OS_NAME == 'osx' ]]; then
  brew update
  brew outdated openssl || brew upgrade openssl
  brew outdated readline || brew upgrade readline
  
  brew outdated pyenv || brew upgrade pyenv
  brew install pyenv-virtualenv
  pyenv install $PYTHON
  export PYENV_VERSION=$PYTHON
  export PATH="/Users/travis/.pyenv/shims:${PATH}"
#   pyenv virtualenv venv
  pyenv virtualenv $PYTHON venv
  ls
  ls ~
  pwd
  source venv/bin/activate
  python --version
  pip -V
  python pip3 install --upgrade pip
  python --version
  pip -V
  
fi
