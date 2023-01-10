"""
SampleNote v1 (https://samplenote.github.io/).

Repository: https://github.com/SampleNote/samplenote-data
Documentation: https://samplenote.github.io/docs/
"""
from setuptools import find_packages, setup

import config

setup(
    name='webapp-flask',
    packages=find_packages(exclude=['tests']),
    version=config.VERSION,
    description='SampleNote Data Classes',
    author='Frederico Betting',
    install_requires=[],
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
    test_suite='tests',
)
