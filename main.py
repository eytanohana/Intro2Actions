import sys
import os


def add(a, b):
    """add"""
    return a + b


def subtract(a, b):
    """subtract"""
    return a - b


def mulitply(a, b):
    """multiply"""
    return a * b


def divide(a, b):
    """divide"""
    return a / b


def pow(a, b):
    """power"""
    return a ** b


def root(a, b):
    """root"""
    return a ** (1 / b)


def floor(a):
    return int(a)


def ceil(a):
    if a == int(a):
        return a
    return int(a + 1)


def plus_one(a):
    return a + 1


def minus_one(a):
    return a - 1


def minus_two(a):
    return a - 2


def minus_three(a):
    return a - 3


def minus_four(a):
    return a - 4


def add2(a):
    return a + 2


if __name__ == "__main__":
    print(f'System path is:      {sys.path}')
    print(f'Python version is:   {sys.version}')
    tag = os.environ.get('DOCKER_TAG', 'no tag available')
    print(f'Docker tag is:       {tag}')
