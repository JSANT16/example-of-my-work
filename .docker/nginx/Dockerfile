FROM nginx:1.19.2-alpine
RUN rm /etc/nginx/conf.d/default.conf
COPY ./.docker/nginx/conf.d/local.conf /etc/nginx/conf.d/

ADD ./staticfiles/ /usr/share/nginx/html/static/
