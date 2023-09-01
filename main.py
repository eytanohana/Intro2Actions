import sys
import os


if __name__ == "__main__":
    print(sys.version)
    tag = os.environ.get('DOCKER_TAG', 'no tag available')
    print(tag)
