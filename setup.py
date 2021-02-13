#!/usr/bin/env python
# coding=utf-8

from setuptools import setup, find_packages

def parse_requirements(filename):
    """ load requirements from a pip requirements file """
    lineiter = (line.strip() for line in open(filename))
    return [line for line in lineiter if line and not line.startswith("#")]


setup(
    name="python-tvmaze",
    version="1.0.3a1",
    description="A Python client for the TvMaze API.",
    license="MIT",
    author="Yakup Adaklı",
    author_email="yakup.adakli@gmail.com",
    url="http://github.com/yakupadakli/python-tvmaze.git",
    packages=find_packages(exclude=["tests"]),
    install_requires=parse_requirements("requirements.txt"),
    keywords="tvmaze library",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Software Development :: Libraries",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.6",
    ],
    zip_safe=True,
)
