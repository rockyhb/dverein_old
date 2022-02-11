FROM python:3.9-slim
# alpine

WORKDIR /code

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
# RUN apk update
RUN apt-get update &&\
    apt-get install -y python3-dev default-libmysqlclient-dev build-essential
RUN pip install --upgrade pip

# RUN apk add --no-cache mariadb-connector-c-dev ;\
#     apk add --no-cache --virtual .build-deps \
#         build-base \
#         libc-dev \
#         mariadb-dev ;\
#     pip install mysqlclient uwsgi;\
#     apk del .build-deps 

# RUN apk add python3-dev
# RUN apk add gpgme-dev
# RUN apk add libc-dev
# RUN apk add gcc jpeg-dev zlib-dev libffi-dev freetype-dev musl-dev lcms2-dev openjpeg-dev tiff-dev tk-dev tcl-dev cairo-dev pango-dev gdk-pixbuf-dev
# RUN apk add mariadb-dev

COPY requirements.txt /code/
RUN pip install -r requirements.txt

COPY dverein /code/
COPY docker-setup/uwsgi-app.ini /etc/uwsgi/apps-enabled/uwsgi-app.ini
COPY docker-setup/init_and_run.sh /sbin/init_and_run.sh
RUN chmod a+x /sbin/init_and_run.sh

EXPOSE 8000

CMD ["/sbin/init_and_run.sh"]
