#!/usr/bin/python3
"""Fabric script that creates and distributes an archive to web servers."""
from datetime import datetime
from fabric.api import env, local, put, run, settings
import os
import sys

if not any(a.startswith(('-H', '--hosts')) for a in sys.argv):
    env.hosts = ['52.55.249.213', '54.157.32.137']

_archive = None


def do_pack():
    """Create a .tgz archive from the contents of web_static.

    Returns:
        The archive path if generated correctly, otherwise None.
    """
    now = datetime.now().strftime("%Y%m%d%H%M%S")
    archive_path = "versions/web_static_{}.tgz".format(now)

    try:
        with settings(warn_only=True):
            if not os.path.isdir("versions"):
                local("mkdir -p versions")
            print("Packing web_static to {}".format(archive_path))
            result = local("tar -cvzf {} web_static".format(archive_path))
            if result.failed:
                return None
        size = os.path.getsize(archive_path)
        print("web_static packed: {} -> {}Bytes".format(archive_path, size))
        return archive_path
    except Exception:
        return None


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


def deploy():
    """Create an archive and distribute it to the web servers.

    Returns:
        The return value of do_deploy, or False if no archive was created.
    """
    global _archive
    if _archive is None:
        _archive = do_pack()
    if _archive is None:
        return False
    return do_deploy(_archive)