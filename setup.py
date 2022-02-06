#!/usr/bin/env python3

from setuptools import setup

setup(
    name='LibAnt',
    packages=['libAnt', 'libAnt.profiles', 'libAnt.drivers', 'libAnt.loggers'],
    version='0.1.4',
    description='Python Ant+ Lib',
    author='Tim Downey',
    author_email='timothy.downey@gmail.com',
    url='https://github.com/timothydowney/libant',
    download_url='https://github.com/timothydowney/libant/tarball/0.1.4',
    keywords = ['ant', 'antplus', 'ant+', 'antfs', 'thisisant'],
    install_requires=['pyusb>=1.0.0', 'pyserial>=3.1.1'],
)
