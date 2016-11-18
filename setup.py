try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

from os import path

README = path.abspath(path.join(path.dirname(__file__), 'README.rst'))

setup(
      name='python-redis-log',
      version='0.1.25',
      description='Redis pub/sub/list logging handler for python',
      long_description=open(README).read(),
      author='Phil Willett',
      author_email='24_Seven@yahoo.com',
      url='https://github.com/phil-willett/python-redis-log',
      packages=['redislog'],
      license='MIT',
      install_requires=['redis', 'simplejson']
)
