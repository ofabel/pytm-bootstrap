#!/usr/bin/env python
from setuptools import find_packages
from setuptools import setup

setup(name='pytm',
      version='0.1.0',
      author='Oliver Fabel',
      author_email='oliver.fabel@fhnw.ch',
      packages=find_packages(include=['pytm', 'pytm.*']),
      description='Skeleton for a Python Tool Manager exercise or tool',
      install_requires=[
          'Flask==2.0.1',
          'Flask-Cors==3.0.10'
      ])
