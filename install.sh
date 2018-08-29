#!/bin/bash

if [[ $TRAVIS_OS_NAME == 'osx' ]]; then
  brew update
  brew outdated openssl || brew upgrade openssl
  brew outdated readline || brew upgrade readline
  brew install python3
  virtualenv venv -p python$PYTHON
  source venv/bin/activate
  python --version
]
fi
