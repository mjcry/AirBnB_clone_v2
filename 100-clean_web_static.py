#!/usr/bin/python3
"""
Fabric script (based on the file 3-deploy_web_static.py)
that deletes out-of-date archives using the function do_clean
"""

from fabric.api import *
from os import path

env.hosts = ['<IP web-01>', '<IP web-02>']
env.user = 'ubuntu'  # replace with your username
env.key_filename = '/path/to/your/private/key'


def do_clean(number=0):
    """Deletes all out-of-date archives"""
    number = int(number)

    if number < 1:
        number = 1

    # Get a list of all archives in the versions folder
    with cd('/data/web_static/releases'):
        archives = run('ls -t').split()

    # Keep only the number most recent archives
    archives_to_keep = archives[:number]

    # Remove all other archives from the versions folder
    for archive in archives:
        if archive not in archives_to_keep:
            run('rm -f {}'.format(path.join('/data/web_static/releases', archive)))

    # Get a list of all archives in the web server root folder
    with cd('/data/web_static/releases'):
        archives = run('ls -t /data/web_static/releases').split()

    # Keep only the number most recent archives
    archives_to_keep = archives[:number]

    # Remove all other archives from the web server root folder
    for archive in archives:
        if archive not in archives_to_keep:
            run('rm -f {}'.format(path.join('/data/web_static/releases', archive)))


