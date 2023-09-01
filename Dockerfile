FROM python:3.11

RUN echo $(python --version)

ENTRYPOINT ["python", "main.py"]
