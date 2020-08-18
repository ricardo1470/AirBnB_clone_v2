#!/usr/bin/python3
""" a Fabric script that distributes
    an archive to your web servers """
from fabric.api import env, run, put, sudo, local
from datetime import datetime
import os.path

env.hosts = ["35.243.141.246", "54.227.41.202"]


def do_pack():
    """ script that generates a .tgz archive """
    date_now = datetime.utcnow()
    year = date_now.year
    month = date_now.month
    day = date_now.day
    hour = date_now.hour
    minute = date_now.minute
    second = date_now.second

    file_date = "versions/web_static_{}{}{}{}{}{}.tgz".format(year, month, day,
                                                              hour, minute,
                                                              second)

    local("sudo mkdir -p versions")
    local("sudo tar -cvzf {} web_static".format(file_date))

    return (file_date)


def do_deploy(archive_path):
    """Function that distributes an archive to your web servers"""
    """local: sudo tar -cvzf versions/web_static_202081833632.tgz web_static"""

    if os.path.exists(archive_path) is False:
        return False

    status = True

    upload = put(archive_path, '/tmp/')
    if upload.failed:
        status = False

    archive_name = archive_path.replace("versions/", "")
    directory_name = archive_name.replace(".tgz", "")

    folder = '/data/web_static/releases/{}/'.format(directory_name)

    directory = run("mkdir -p {}".format(folder))
    if directory.failed:
        status = False

    unpack_cmd = 'tar -xzf /tmp/{} -C {}'.format(archive_name, folder)
    unpack = run(unpack_cmd)
    if unpack.failed:
        status = False

    remove = run('rm /tmp/{}'.format(archive_name))
    if remove.failed:
        status = False

    move = run('mv {}web_static/* {}'.format(folder, folder))
    if move.failed:
        status = False

    remove = run('rm -rf {}web_static'.format(folder))
    if remove.failed:
        status = False

    remove = run('rm -rf /data/web_static/current')
    if remove.failed:
        status = False

    link = run('ln -s {} /data/web_static/current'.format(folder))
    if link.failed:
        status = False

    return status
