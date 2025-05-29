#!/bin/bash


if [[ "$VIRTUAL_ENV" != "" ]]; then
    deactivate
fi

python3 -m venv .venv
source .venv/bin/activate
export $(cat .env)
pip install -r requirements.txt

python3 app.py
