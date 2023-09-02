FROM python:3.11-slim-bullseye

WORKDIR /app

COPY . .

ARG DOCKER_TAG
ENV DOCKER_TAG=$DOCKER_TAG

ENV VENV=venv
RUN python -m venv $VENV
ENV PATH="$VENV/bin:$PATH"
RUN pip install --upgrade pip -r requirements.txt


ENTRYPOINT ["python", "main.py"]
