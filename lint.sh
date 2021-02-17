#!/usr/bin/env bash

set -x
mypy aioconsolemenu
flake8 aioconsolemenu
isort --check-only aioconsolemenu
black --check aioconsolemenu --diff