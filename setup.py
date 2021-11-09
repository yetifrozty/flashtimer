from setuptools import setup

VERSION='1.0.0'
DESCRIPTION='A speedruntimer coded in python'

setup(
    name='flashtimer',
    version=VERSION,
    description=DESCRIPTION,
    author='yetifrozty',
    packages=['flashtimer'],
    install_requires=['keyboard', 'colorama', 'pyfiglet']
)