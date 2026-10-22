#!/usr/bin/python3
"""Fabric script that distributes an archive to web servers."""
from fabric.api import env, put, run, settings
import os

env.hosts = ['52.55.249.213', '54.157.32.137']


def do_deploy(archive_path):
    """Distribute an archive to the web servers.

    Returns:
        True if all operations succeeded, otherwise False.
    """
    if not os.path.isfile(archive_path):
        return False

    archive_file = os.path.basename(archive_path)
    name = os.path.splitext(archive_file)[0]
    release = "/data/web_static/releases/{}".format(name)
    tmp_path = "/tmp/{}".format(archive_file)

    commands = [
        "mkdir -p {}/".format(release),
        "tar -xzf {} -C {}/".format(tmp_path, release),
        "rm {}".format(tmp_path),
        "mv {}/web_static/* {}/".format(release, release),
        "rm -rf {}/web_static".format(release),
        "rm -rf /data/web_static/current",
        "ln -s {}/ /data/web_static/current".format(release),
    ]

    try:
        with settings(warn_only=True):
            if put(archive_path, tmp_path).failed:
                return False
            for cmd in commands:
                if run(cmd).failed:
                    return False
        print("New version deployed!")
        return True
    except Exception:
        return False
