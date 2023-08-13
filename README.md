# Book-Flight-Ticket
simple django application for booking flight-ticket 

## Table of contents
* [General info](#general-info)
* [Technologies](#technologies)
* [Setup](#setup)
* [Commands](#commands)
* [App endpoints](#app-endpoints)
* [API Documentation](#api-documentation)

## General info
Book-Flight-Ticket

## Technologies
* Python
* Django
* Django Rest Framework
* Docker
* SQlite3

### Setup
## Installation on Linux, Mac OS and Windows
* Clone project from the develop branch
```
git clone https://github.com/lilcoded7/Mid-level-Django-Test.git
```

* To create a normal virtualenv (example .venv) and activate it (see Code below).

  ```
  virtualenv --python=python3.10.6 .venv
  
  . .venv/bin/activate

  (.venv) $ pip install -r requirements.txt

  (.venv) $ python manage.py makemigrations

  (.venv) $ python manage.py migrate

  (.venv) $ python manage.py createsuperuser 

  (.venv) $ python manage.py runserver
  ```

## To Run Docker Application
```
  docker-compose up --build
```

* Copy the IP address provided once your server has completed building the site. (It will say something like >> Serving at http://0.0.0.0:8000).
* Open the address in the browser

## Commands
Open docker commands with 
```
docker ps
docker exec -it <CONTAINER_NAME> bash
```

## Endpoints
```
http://127.0.0.1:8000/api/v1/account/register/
```
```
http://127.0.0.1:8000/api/v1/account/login/
```
```
http://127.0.0.1:8000/api/v1/book/flight/ticket/
```

## API Documentation
http://127.0.0.1:8000/api/doc

