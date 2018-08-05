# Grupo Zap Spottipos Chalenge

Grupo ZAP coding challenge, let's help the Spottipos!!!

* Python 3.7
* Pipenv
* Flask
* Pandas
* OpenAPi spec + SwaggerUi
* Docker

## Models

Pandas where used for this in memory test, because its scalable and really efficient on very large datasets

## Api Resources

Flask restplus library where used to generate swagger and provide better documentation for the rest api.

## Project structure

Inspired a little by the DDD guidelines, tried to separate domain classes from infrastructure ones.

Since i am not very fond of using global variables and prefer to inject them on my instances, i've used a DIC style, by simply creating a container.py file wich would take care of all classes dependency injection around.

I've also used a service layer for my domain

## Why python 3.7?
Well i felt in love with dataclasses, what else can i say?

## Install dependencies on develop mode
```
$ pip install pipenv
$ pipenv shell
$ pipenv install
``` 

## run application
```
$ gunicorn application:app
```

## Running tests

```
$ python -m unittest tests.py
```

## Docker
Well, use docker-compose up to run the container, its properly confgured

## References
* Python 3.7 - https://docs.python.org/3/whatsnew/3.7.html
* Pandas - https://pandas.pydata.org/
* DDD - https://en.wikipedia.org/wiki/Domain-driven_design
* Service Layer - https://martinfowler.com/eaaCatalog/serviceLayer.html
* Dependency Injection - https://en.wikipedia.org/wiki/Dependency_injection
* Flask-Restplus - http://flask-restplus.readthedocs.io/en/stable/
* Swagger - https://swagger.io/
* Docker Compose - https://docs.docker.com/compose/
