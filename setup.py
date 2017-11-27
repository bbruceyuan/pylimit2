#!/usr/bin/env python
# created by Bruce Yuan on 17-11-27

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup
import pylimit

setup(
    name='pylimit2',
    version=pylimit.__version__,
    author=pylimit.__author__,
    author_email="bruceyuan123@gmail.com",
    url='https://github.com/hey-bruce/pylimit2',
    description='作为pylimit的升级版，支持py3.5+，使用更方便',
    packages=['pylimit'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ]
)
