#!/usr/bin/env sh
cd /code
python3 manage.py wait_for_db
python3 manage.py migrate || { echo 'migrate failed' ; exit 1; }
python3 manage.py collectstatic --noinput
python3 manage.py initadmin
python3 manage.py initial_data
python3 manage.py runserver 0.0.0.0:8000
