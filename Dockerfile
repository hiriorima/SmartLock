 FROM python:3.6
 ENV PYTHONUNBUFFERED 1

 RUN apt-get update && apt-get install -y sudo

 RUN mkdir /code
 WORKDIR /code
 ADD requirements.txt /code/
 RUN  pip install -r requirements.txt
 RUN sudo pip install wiringpi2
 ADD . /code/
