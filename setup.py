#!/usr/bin/env python
# -*- coding: utf-8 -*-
from scikit_small_ensemble import __VERSION__

from setuptools import find_packages, setup

setup(
    name='scikit_small_ensemble',
    version=__VERSION__,
    author='Stewart Park',
    url='https://github.com/stewartpark/scikit-small-ensemble',
    author_email='hello@stewartjpark.com',
    license='MIT',
    install_requires=['lz4', 'joblib'],
    packages=find_packages(),
    zip_safe=False
)
