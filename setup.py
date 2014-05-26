import sys
import jsonlinedb

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name = 'jsonlinedb',
    version = jsonlinedb.__version__,
    author = 'Andrey Usov',
    author_email = 'ownport@gmail.com',
    url = 'https://github.com/ownport/jsonlinedb',
    description = ('Simple JSONlines Storage'),
    long_description = open('README.md').read(),
    license = "BSD",
    keywords = "json python database index search",
    packages = ['jsonlinedb',],
    include_package_data = True,
    classifiers = [
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: POSIX',
        'Operating System :: POSIX :: Linux',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
    ],
)
