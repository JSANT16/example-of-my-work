FROM python:3.9

ENV PYTHONUNBUFFERED 1
ENV DJANGODIR=/django

RUN mkdir $DJANGODIR

WORKDIR $DJANGODIR

COPY ./requirements.txt $DJANGODIR
ADD ./frontend/build/ $DJANGODIR/frontend/build/
RUN python -m pip install -r requirements.txt
COPY . $DJANGODIR

ADD /.docker/django/docker-entrypoint.sh /docker-entrypoint.sh
RUN chmod a+x /docker-entrypoint.sh
ENTRYPOINT ["/docker-entrypoint.sh"]