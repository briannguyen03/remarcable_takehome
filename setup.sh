#!/bin/bash

set -e

if [ ! -d "venv" ]; then
	echo "Creating virtual enviroment..."
	python3 -m venv venv || { echo "Failed to create venv"; exit 1; }
fi

echo "Activating the virtual enviroment..."
source venv/bin/activate || { echo "Failed to activate venv"; exit 1; }


echo "Installing dependencies..."
pip install -r requirements.txt || { echo "Failed to install dependencies"; exit 1; }


echo "Starting server..."
python3 manage.py runserver
	
