import os


if __name__ == "__main__":
    tag = os.environ.get('DOCKER_TAG', 'no tag available')
    print(tag)
