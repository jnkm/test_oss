#!/bin/bash

if [[ $TRAVIS_OS_NAME == 'osx' ]]; then
  brew update
  brew outdated openssl || brew upgrade openssl
  brew outdated readline || brew upgrade readline
  
  brew outdated readline || brew upgrade readline
  pyenv install $PYTHON
  export PYENV_VERSION=$PYTHON
  export PATH="/Users/travis/.pyenv/shims:${PATH}"
  virtualenv venv -p python3
  source venv/bin/activate
  python --version
]
fi
