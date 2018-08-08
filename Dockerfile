FROM ubuntu:16.04
MAINTAINER sdq <shidanqingnet@gmail.com>

ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update && apt-get install -y \
    python-pip python \
    nginx gunicorn supervisor

# Setup flask application
COPY app /var/www/app
RUN pip install --upgrade pip
RUN pip install --upgrade setuptools
RUN apt-get install -y libmysqlclient-dev
RUN pip install -r /var/www/app/requirements.txt

# Setup nginx
RUN rm /etc/nginx/sites-enabled/default 
COPY nginx/nginx.conf /etc/nginx/sites-available/
COPY cert /etc/nginx/cert
RUN ln -s /etc/nginx/sites-available/nginx.conf /etc/nginx/sites-enabled/nginx.conf
RUN echo "daemon off;" >> /etc/nginx/nginx.conf

# Setup supervisord
COPY supervisor/supervisord.conf /etc/supervisor/conf.d/supervisord.conf
RUN pip install gevent
COPY gunicorn/gunicorn.conf /etc/supervisor/conf.d/gunicorn.conf

CMD ["/usr/bin/supervisord"]
