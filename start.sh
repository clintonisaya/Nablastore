#!/bin/sh

# Install dependencies
python setup.py install

# Start the web server
gunicorn nablastore.wsgi
