# internDocker

- Install

 - Clone repository
 
 - Ma .env file in the projecroot folder and fill it with setti
 
 ```
DEBUG=0
SECRET_KEY=bfdgnmfthktrdhtyjtykghjgyjgyj
DJANGO_ALLOWED_HOSTS=localhost 127.0.0.1 [::1]
SQL_ENGINE=django.db.backends.postgresql_psycopg2
SQL_DATABASE=vocabularydb
SQL_USER=vocabularyU
SQL_PASSWORD=vocabularydbp
SQL_HOST=db
SQL_PORT=5432
POSTGRES_USER=vocabularyU
POSTGRES_PASSWORD=vocabularydbp
POSTGRES_DB=vocabularydb
 ```
 
DJANGO_ALLOWED_HOSTS list hosts that are allowed for site dividing them with spaces

SQL_ENGINE=django.db.backends.postgresql_psycopg2

SQL_DATABASE= db name

SQL_USER= db user

SQL_PASSWORD= database password

SQL_HOST=db

SQL_PORT=5432

POSTGRES_USER= db user

POSTGRES_PASSWORD password

POSTGRES_DB = db name

- run commands in root

```
docker-compose x up -d --build
docker-compose  exec web python manage.py migrate --noinput
docker-compose  exec web python manage.py collectstatic --no-input --clear
```
 

 
