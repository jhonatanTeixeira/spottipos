FROM python:3.7-jessie

RUN pip install pipenv

COPY ./ /var/www

WORKDIR /var/www

RUN pipenv install --system

CMD ["gunicorn", "application:app"]