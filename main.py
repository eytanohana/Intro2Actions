import sys
import os


if __name__ == "__main__":
    print(sys.version)
    print(sys.path)
    tag = os.environ.get('DOCKER_TAG', 'no tag available')
    print(tag)
