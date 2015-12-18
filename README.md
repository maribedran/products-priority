# Products priority

Django app for displaying products

## Setting up Virtualenv

```shell
  $ mkvirtualenv products-priority
  $ workon products-priority
  $ pip install -r requirements.txt
```

## Configuring posrtgres


```shell
  $ psql
```

```posrtgres
  # CREATE DATABASE products;
  # CREATE USER admin WITH PASSWORD 'admin';
  # GRANT ALL PRIVILEGES ON DATABASE products TO admin;
  # ALTER USER admin CREATEDB;
  # \q
```

## Loading the database

```
  $ python manage.py loaddata products.json
```
