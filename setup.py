#!/usr/bin/env python
from setuptools import setup

setup(
    name="tap-googleplay",
    version="0.1.0",
    description="Singer.io tap for extracting data from the Google Play Console",
    author="dpmn",
    url="https://github.com/dpmn",
    classifiers=["Programming Language :: Python :: 3 :: Only"],
    py_modules=["tap_googleplay"],
    install_requires=[
        # NB: Pin these to a more specific version for tap reliability
        "singer-python",
        "requests",
        "google-cloud-storage",
    ],
    entry_points="""
    [console_scripts]
    tap-googleplay=tap_googleplay:main
    """,
    packages=["tap_googleplay"],
    package_data = {
        "schemas": ["tap_googleplay/schemas/*.json"]
    },
    include_package_data=True,
)
