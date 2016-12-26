# sword django app
## to use postgres
- update settings.py
- add "psycopg2" to requirements.txt
- docker-compose build && docker-compose up
```py
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'postgres',
        'USER': 'postgres',
        'PASSWORD': 'postgres',
        'HOST': os.environ.get('DB_PORT_5432_TCP_ADDR', 'db'),
        'PORT': os.environ.get('DB_PORT_5432_TCP_PORT', 5432),
    }
}
```
