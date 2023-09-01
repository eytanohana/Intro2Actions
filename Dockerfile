FROM python:3.11


WORKDIR /app

RUN echo $(python --version)

COPY . .

ARG DOCKER_TAG
ENV DOCKER_TAG=$DOCKER_TAG

ENTRYPOINT ["python", "main.py"]