#!/usr/bin/env bash
from fabric.api import local, env
from datetime import datetime

env.hosts = ['localhost']


def do_pack():
    """
    Generates a .tgz archive from the contents of the web_static folder of
    your AirBnB Clone repo
    """
    now = datetime.now()
    dt_string = now.strftime("%Y%m%d%H%M%S")
    archive_path = "versions/web_static_{}.tgz".format(dt_string)

    local("mkdir -p versions")
    result = local("tar -cvzf {} web_static".format(archive_path))

    if result.succeeded:
        return archive_path
    else:
        return None
