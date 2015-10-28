from setuptools import setup
from os import path

here = path.abspath(path.dirname(__file__))

setup(
    name='mesoslxc',

    version='0.0.1',

    description='',
    long_description='',

    url='',

    author='Lukasz Adamczyk',
    author_email='l.adamczyk@avsystem.com',

    keywords='mesos lxc external containerizer executor',

    packages=['mesoslxc', 'mesoslxc.ec', 'mesoslxc.ex', 'mesoslxc.interface'],
    zip_safe=False,
)
