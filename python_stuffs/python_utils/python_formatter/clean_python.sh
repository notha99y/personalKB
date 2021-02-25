#!/bin/bash
echo "Cleaning up " "$@""..."
echo "Sorting your imports so you don't have to"
isort $@
echo "Formatting code to have a max length of 79"
black $@ -l 79 -v 
echo "Analysing code.."
flake8 $@ --max-line-length=79