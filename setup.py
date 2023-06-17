#!/usr/bin/env python
from setuptools import find_packages
from setuptools import setup

setup(packages=find_packages(include=['pytm', 'pytm.*']),
      install_requires=[
          'Flask==2.3.2',
          'Flask-Cors==3.0.10',
          'matplotlib==3.7.1'
      ])
