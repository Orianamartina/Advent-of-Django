#!/usr/bin/env bash
# exit on error
set -o errexit

poetry install
python manage.py collectstatic --no-input
python manage.py migrate advent_days
python manage.py migrate