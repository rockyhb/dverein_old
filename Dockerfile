FROM python:3.9-alpine
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt
COPY dverein /code/
COPY docker-setup/init_and_run.sh /sbin/init_and_run.sh
RUN chmod a+x /sbin/init_and_run.sh
EXPOSE 8000
CMD ["/sbin/init_and_run.sh"]
