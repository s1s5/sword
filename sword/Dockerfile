FROM python:2.7
ENV PYTHONUNBUFFERED 1
ENV STATIC_ROOT /data/static
ENV MEDIA_ROOT /data/media
RUN mkdir /app
WORKDIR /app
ADD requirements.txt /app/
RUN pip install -U -r requirements.txt
ADD . /app/
