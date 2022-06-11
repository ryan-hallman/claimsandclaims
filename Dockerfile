# syntax=docker/dockerfile:1

FROM python:3.8-slim-buster

# set work directory
WORKDIR /usr/src/app

# set environment variables
## Prevents Python from writing pyc files to disc
ENV PYTHONDONTWRITEBYTECODE 1
## Prevents Python from buffering stdout and stderr
ENV PYTHONUNBUFFERED 1

# install system dependencies
RUN apt-get update && apt-get install -y netcat

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt /usr/src/app/requirements.txt
RUN pip install -r requirements.txt

# copy project
COPY . /usr/src/app/

#CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]
# run entrypoint.sh
ENTRYPOINT ["/usr/src/app/entrypoint.sh"]