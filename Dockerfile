FROM python:3.8.0-alpine3.10

USER root


WORKDIR /source
COPY source/ /source/
COPY ./requirements.txt /source
RUN ls -la /source


RUN python3 --version
RUN pip3 install --upgrade pip
RUN pip3 install --no-cache-dir -r /source/requirements.txt
RUN pip3 list --format=columns

USER 1001



