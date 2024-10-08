#!/usr/bin/env python

from setuptools import setup
from codecs import open
from os import path
import vdf

here = path.abspath(path.dirname(__file__))
with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='vdf',
    version=vdf.__version__,
    description='Library for working with Valve\'s VDF text format',
    long_description=long_description,
    url='https://github.com/solsticegamestudios/vdf',
    author='Rossen Georgiev / Solstice Game Studios',
    author_email='py-vdf@solsticegamestudios.com',
    license='MIT',
    python_requires=">=3.6",
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'Programming Language :: Python :: Implementation :: PyPy',
    ],
    keywords='valve keyvalue vdf tf2 dota2 csgo',
    packages=['vdf'],
    zip_safe=True,
)
