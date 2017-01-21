#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

from setuptools import setup, find_packages

package = 'tt'
version = '0.1'

setup(
    name=package,
    version=version,
    description="Personal Portfolio Tracking Tool",
    packages=find_packages(include=['tt', 'tt.*']),
    package_data={root.replace(os.sep, '.'):
                  ['*.pyi', '*.pyx', '*.pxi', '*.pxd']
                  for root, dirnames, filenames in os.walk('tt')
                  if '__pycache__' not in root},
    url='')
