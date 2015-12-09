#!/usr/bin/env python2

from distutils.core import setup

setup(name='Rovio',
      version='1.0',
      description='Remote robot control',
      author='Innokenty Lebedev (RobotsCityAmsterdam)',
      author_email='innlebedev@gmail.com',
      url='http://robotscityamsterdam.com',
      packages=['rovio_base', 'main', 'utils'],
      scripts=['rovio'],
      data_files=[('/etc/rovio/', ['rovio.cfg'])]
      )
