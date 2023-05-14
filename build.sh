#!/bin/bash

if [ ! -f "pyvenv.cfg" ]; then
    python -m venv .
    . ./bin/activate
    ./bin/pip3 install -r requirements.txt
    deactivate
fi

if [ "$1" = "run" ]; then
    shift 1
    . ./bin/activate 
    python3 ./backuper.py $@
    deactivate
fi
