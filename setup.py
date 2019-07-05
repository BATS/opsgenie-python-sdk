# coding: utf-8

"""
    Python SDK for Opsgenie REST API

    Python SDK for Opsgenie REST API  # noqa: E501

    The version of the OpenAPI document: 2.0.0
    Contact: support@opsgenie.com
    Generated by: https://openapi-generator.tech
"""


import os

from setuptools import setup, find_packages  # noqa: H301

NAME = "opsgenie-sdk"
VERSION = "2.0.0b3"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = ["urllib3 >= 1.15", "six >= 1.10", "certifi", "python-dateutil", "numpy >= 1.16.3", "retry >= 0.9.2"]

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name=NAME,
    version=VERSION,
    author="OpsGenie",
    author_email="support@opsgenie.com",
    description="Python SDK for Opsgenie REST API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/opsgenie/opsgenie-python-sdk",
    packages=find_packages(exclude=['samples']),
    keywords=["OpenAPI", "OpenAPI-Generator", "Python SDK for Opsgenie REST API", "OpsGenie", "Opsgenie"],
    install_requires=REQUIRES,
    include_package_data=True,
    project_urls={
        'Documentation': 'https://docs.opsgenie.com/docs/opsgenie-python-api',
        'Source': 'https://github.com/opsgenie/opsgenie-python-sdk',
        'Tracker': 'https://github.com/opsgenie/opsgenie-python-sdk/issues',
    },
    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: Apache Software License',
        "Operating System :: OS Independent",
    ]
)
