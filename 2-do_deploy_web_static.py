#!/usr/bin/python3
""" a Fabric script that distributes
    an archive to your web servers """
from fabric.api import env, run, put, sudo
import os.path
from fabric.main import main

env.hosts = ['35.243.141.246', '54.227.41.202']
env.user = 'ubuntu'


def do_deploy(archive_path):
    """ distributes an archive to your web servers """
    if not archive_path:
        return False
    file_arg = archive_path.split("/")[-1]
    new = '/data/web_static/release' + "{}".format(file_arg.split('.')[0])
    current = 'data/web_static/current'
    try:
        put(archive_path, '/tmp/')
        run('sudo mkdir -p {}/'.format(new))
        run('sudo tar -xzf {} -C {}/'.format(file_arg, new))
        run('sudo rm /tmp/{}'.format(file_arg))
        run('sudo mv {}/web_static {}/'.format(new))
        run('sudo rm -rf {}'.format(current))
        run('sudo ln -s {}/ {}'.format(new, current))
        return True
    except:
        return False
