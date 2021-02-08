# Python Orbit

🪐 Light Orbit API wrapper written in Python

[![Latest Version](https://img.shields.io/pypi/v/python-orbit.svg)](https://pypi.python.org/pypi/python-orbit/)
[![codecov](https://codecov.io/gh/astagi/python-orbit/branch/master/graph/badge.svg)](https://codecov.io/gh/astagi/python-orbit)
[![CircleCI](https://circleci.com/gh/astagi/python-orbit.svg?style=svg)](https://circleci.com/gh/astagi/python-orbit)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://github.com/astagi/python-orbit/blob/master/LICENSE)

⚠️ This project is WIP

## Install

```sh
pip install python-orbit
```

## Usage

If you need some code ready to use, [spike.py](https://github.com/astagi/python-orbit/blob/master/spike.py) is a good starting point

### Execute queries

Python Orbit client allows you to use [Orbit API](https://docs.orbit.love/reference) with Python.

```py
from orbit import Orbit


client = Orbit(auth="YourAuthKey")

print (client.get_workspaces())
```

### Deal with errors

If there's an error in your query, a `OrbitException` will be raised

```py
from orbit import Orbit, OrbitException


client = Orbit(auth="YourAuthKey")
try:
    client.get_workspaces()
except OrbitException as ex:
    print (ex)
```

## Run tests

```sh
pip install -r requirements-dev.txt
make test
```
