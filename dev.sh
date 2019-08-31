#!/usr/bin/env bash

python3 -m venv venv
source venv/bin/activate

python -m pip install --upgrade pip wheel setuptools twine tox flake8 pylint pylama
pip install -e .

tox
