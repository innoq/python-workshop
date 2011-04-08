AUTHOR = 'FND'
AUTHOR_EMAIL = 'fnd@example.org'
NAME = 'mysample'
DESCRIPTION = 'lorem ipsum dolor sit amet'
VERSION = '0.1'


import os

from setuptools import setup, find_packages


setup(
    name = NAME,
    version = VERSION,
    description = DESCRIPTION,
    long_description = open(os.path.join(os.path.dirname(__file__), 'README')).read(),
    author = AUTHOR,
    author_email = AUTHOR_EMAIL,
    url = 'http://pypi.python.org/pypi/%s' % NAME,
    platforms = 'Posix; MacOS X; Windows',
    packages = find_packages(exclude=['test']),
    install_requires = ['setuptools'],
    zip_safe = False
)
