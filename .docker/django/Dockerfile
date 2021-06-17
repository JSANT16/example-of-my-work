FROM python:3.9

ENV PYTHONUNBUFFERED 1
ENV DJANGODIR=/django

RUN mkdir $DJANGODIR

WORKDIR $DJANGODIR

COPY ./requirements.txt $DJANGODIR

RUN python -m pip install -r requirements.txt
COPY . $DJANGODIR
# RUN python manage.py makemigrations
# RUN python manage.py migrate
