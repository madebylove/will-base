import os
from fabric.api import *
CTAG = os.environ.get("CTAG", "")

DOCKER_BUILDS = [
        {
            "ctagname": "heywill/will-base:2.7-alpine-%s" % CTAG,
            "name": "heywill/will-base:2.7-alpine",
            "dir": "base-2.7/",
            "latest": False
        },
        {
            "ctagname": "heywill/will-base:3.7-alpine-%s" % CTAG,
            "name": "heywill/will-base:3.7-alpine",
            "dir": "base-3.7/",
            "latest": True

        }
    ]

DOCKER_PATH = os.path.join(os.getcwd(), ".")

@task
def docker_build():
    print("Building Docker Images...")
    with lcd(DOCKER_PATH):
        for b in DOCKER_BUILDS:
            local("docker build -t %(ctagname)s %(dir)s" % b)
@task
def docker_tag():
    print ("Tagging Images....")
    with lcd(DOCKER_PATH):
        for b in DOCKER_BUILDS:
            local("docker tag %(ctagname)s %(name)s" % b)
            if b['latest'] == True:
                local("docker tag %(ctagname)s heywill/will-base:latest" % b)


def docker_push(c):
    print("Pushing Docker to Docker Cloud...")
    with lcd(DOCKER_PATH):
        for b in DOCKER_BUILDS:

            local("docker push %(ctagname)s" % b)
            local("docker push %(name)s" % b)
        local("docker push heywill/will-base:latest")

@task
def docker_deploy():
    docker_build()
    docker_tag()
    docker_push()
