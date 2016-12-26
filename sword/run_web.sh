#!/bin/bash
# -*- mode: shell-script -*-

# wait for PSQL server to start
sleep 10

python manage.py makemigrations sword
python manage.py migrate
python manage.py runserver 0.0.0.0:32642
