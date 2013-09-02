#!/usr/bin/python

from distutils.core import setup

setup(
    name="rsthome",
    version="0.1.0",
    description="Restructured Text Homepage",
    author="Bertrand Janin",
    author_email="tamentis@neopulsar.org",
    url="http://tamentis.com/",
    packages=["rsthome"],
    install_requires=[
        "jinja2",
        "pygments",
        "docutils",
        "cheetah",
    ],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: ISC License (ISCL)",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: POSIX",
        "Programming Language :: Python :: 2.5",
        "Programming Language :: Python :: 3.0",
        "Programming Language :: Python :: 3.1",
    ],
    scripts=[
        "scripts/rsthome_cheetah",
        "scripts/rsthome_home",
        "scripts/rsthome_render",
    ],
)
