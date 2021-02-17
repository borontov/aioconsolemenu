#!/usr/bin/env bash

isort --force-single-line-imports aioconsolemenu
autoflake --recursive --remove-all-unused-imports --remove-unused-variables --in-place aioconsolemenu
black aioconsolemenu
isort aioconsolemenu