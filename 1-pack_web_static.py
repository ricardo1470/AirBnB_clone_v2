#!/usr/bin/python3
""" a Fabric script """
from fabric.api import *
from datetime import datetime


def do_pack():
    """ script that generates a .tgz archive """
    date_now = datetime.utcnow()
    year = date_now.year
    month = date_now.month
    day = date_now.day,
    hour = date_now.hour,
    minute = date_now.minute,
    second = date_now.second

    file_date = "versions/web_static_{}{}{}{}{}{}.tgz".format(year, month, day,
                                                              hour, minute,
                                                              second)

    local("mkdir -p versions")
    local("tar -cvzf {} web_static".format(file_date))

    return (file_date)
