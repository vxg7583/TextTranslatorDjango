#!/bin/bash
PATH = $(pwd)
if  which python3
then
    echo "python there"
    pip install --user virtualenv
    python -m venv env
    source /env/bin/activate
    activate
    pip install -r requirements.txt
    python manage.py runserver
else 
    echo "Please install python 3+ and source or set it as the environment variable"
fi

