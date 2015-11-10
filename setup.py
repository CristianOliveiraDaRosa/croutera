#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

from croutera import version

def publish():
    """Publish to PyPi"""
    os.system("python setup.py sdist upload")

if sys.argv[-1] == "publish":
    publish()
    sys.exit()

setup(name='croutera',
      version= version(),
      description='Simple Cli Router Admin',
      long_description=open('README.md').read(),
      url='https://github.com/cristianoliveira/croutera',
      author='Cristian Oliveira',
      author_email='contato@cristianoliveira.com.br',
      license='MIT',
      packages=[
      'croutera',
      'croutera/http',
      'croutera/models',
      'croutera/models/tplink',
      'croutera/models/dlink'
      ],
      scripts=['bin/croutera'],
      zip_safe=False)