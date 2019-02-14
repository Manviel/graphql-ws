#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import find_packages, setup

with open("README.rst") as readme_file:
    readme = readme_file.read()

readme = ""

with open("HISTORY.rst") as history_file:
    history = history_file.read()

requirements = [
    "graphql-core",
    # TODO: put package requirements here
]

setup_requirements = [
    "pytest-runner",
    # TODO(graphql-python): put setup requirements (distutils extensions,
    # etc.) here
]

test_requirements = [
    "pytest",
    # TODO: put package test requirements here
]

setup(
    name="graphql-ws-django",
    version="0.3.7",
    description="Websocket server for GraphQL subscriptions",
    long_description=readme + "\n\n" + history,
    author="Manviel",
    author_email="Mihaylo.Merezhko@kname.edu.ua",
    url="https://github.com/Manviel/graphql-ws",
    packages=find_packages(
        include=["graphql_ws_django", "graphql_ws_django.*"]),
    include_package_data=True,
    install_requires=requirements,
    license="MIT license",
    zip_safe=False,
    keywords=["graphql", "subscriptions", "graphene", "websockets"],
    classifiers=[
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "Programming Language :: Python :: 3"
    ],
    test_suite="tests",
    tests_require=test_requirements,
    setup_requires=setup_requirements,
)
