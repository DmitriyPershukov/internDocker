# internDocker

# Installing

 - Clone repository
 
 - Create vocdb.env file in the project root folder and fill it with db name,user and password, docker will make database using these settings
 ```
POSTGRES_USER=vocabularyU
POSTGRES_PASSWORD=vocabularydbp
POSTGRES_DB=vocabularydb
 ```
 
 - Create vc.env file in the root folder of project and set api_secret and secret key and allowed_hosts. use db settings from previous step
 
 ```
DEBUG=0
SECRET_KEY=bfdgnmfthktrdhtyjtykghjgyjgyj
DJANGO_ALLOWED_HOSTS=localhost 127.0.0.1 [::1]
SQL_ENGINE=django.db.backends.postgresql_psycopg2
SQL_DATABASE=vocabularydb
SQL_USER=p
SQL_PASSWORD=password
SQL_HOST=db
SQL_PORT=5432
API_SECRET=secret
 ```
 
- open cli run commands in root folder of project

```
docker-compose up -d --build

```

- run these command in new cli, then press CTRL+C
```
docker-compose  exec web python manage.py migrate --noinput
docker-compose  exec web python manage.py collectstatic --noinput --clear
```
 
# Starting web server

- run these command from root folder of project in cli
```
docker-compose up -d
```
 
