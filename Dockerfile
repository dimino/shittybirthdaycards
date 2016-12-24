FROM python:3.6
ENV PYTHONUNBUFFERED 1
RUN mkdir /src
WORKDIR /src
ADD requirements.txt /src/
ADD test_requirements.txt /src/
RUN pip install --upgrade pip # pip is outdated on python 3.6 base image
RUN pip install -r requirements.txt -r test_requirements.txt
ADD . /src/
