import sys
import os


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def mulitply(a, b):
    return a * b


def divide(a, b):
    return a / b



if __name__ == "__main__":
    print(f'System path is:      {sys.path}')
    print(f'Python version is:   {sys.version}')
    tag = os.environ.get('DOCKER_TAG', 'no tag available')
    print(f'Docker tag is:       {tag}')
