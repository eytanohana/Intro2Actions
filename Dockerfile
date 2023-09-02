FROM python:3.11-slim-bullseye

WORKDIR /app

COPY . .

ARG DOCKER_TAG
ENV DOCKER_TAG=$DOCKER_TAG

RUN pip install --upgrade pip -r requirements.txt

ENTRYPOINT ["python", "main.py"]
