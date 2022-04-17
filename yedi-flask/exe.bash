#!/bin/bash

source myvenv/Scripts/activate

export FLASK_APP=main.py
export FLASK_DEBUG=1

flask run