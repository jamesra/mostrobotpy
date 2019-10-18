#!/usr/bin/env python3

import os
from os.path import dirname, exists, join
import sys, subprocess
from setuptools import find_packages, setup

if sys.version_info.major < 3 or (
    sys.version_info.major == 3 and sys.version_info.minor < 6
):
    sys.stderr.write("ERROR: RobotPy requires Python 3.6+\n")
    exit(1)

setup_dir = dirname(__file__)
git_dir = join(setup_dir, "..", ".git")
base_package = "wpilib"
version_file = join(setup_dir, base_package, "version.py")

# Automatically generate a version.py based on the git version
if exists(git_dir):
    p = subprocess.Popen(
        ["git", "describe", "--tags", "--long", "--dirty=-dirty"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    out, err = p.communicate()
    # Make sure the git version has at least one tag
    if err:
        print("Error: You need to create a tag for this repo to use the builder")
        sys.exit(1)

    # Convert git version to PEP440 compliant version
    # - Older versions of pip choke on local identifiers, so we can't include the git commit
    v, commits, local = out.decode("utf-8").rstrip().split("-", 2)
    if commits != "0" or "-dirty" in local:
        v = "%s.post0.dev%s" % (v, commits)

    # Create the version.py file
    with open(version_file, "w") as fp:
        fp.write(
            "# novalidate\n# Autogenerated by setup.py\n__version__ = '{0}'".format(v)
        )

if exists(version_file):
    with open(version_file, "r") as fp:
        exec(fp.read(), globals())
else:
    __version__ = "master"

with open(join(setup_dir, "README.rst"), "r") as readme_file:
    long_description = readme_file.read()

setup(
    name="wpilib",
    version=__version__,
    description="WPILib",
    long_description=long_description,
    author="Peter Johnson, Dustin Spicuzza",
    author_email="robotpy@googlegroups.com",
    url="https://github.com/robotpy/robotpy-wpilib",
    keywords="frc first robotics wpilib",
    packages=find_packages(),
    install_requires=["pynetworktables>=2019.0.1"],
    license="BSD License",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Intended Audience :: Education",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Topic :: Scientific/Engineering",
    ],
)
