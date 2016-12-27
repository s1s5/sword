#!/bin/bash
# -*- mode: shell-script -*-

python manage.py collectstatic --noinput

# wait for PSQL server to start
sleep 5
python manage.py makemigrations
python manage.py migrate
echo "from django.contrib.auth.models import User; None if User.objects.filter(username='admin').count() else User.objects.create_superuser('admin', 'admin@example.com', 'admin')" | python manage.py shell

python manage.py runserver 0.0.0.0:32642
