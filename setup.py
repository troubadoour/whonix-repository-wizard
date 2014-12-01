#!/usr/bin/env python

from distutils.core import setup
import sys, os
SHARE='share'

datafiles = []
for root, dirs, files in os.walk(SHARE):
    datafiles.append((os.path.join(sys.prefix, root),
                      [os.path.join(root, f) for f in files]))

setup(
    name='whonix-repository-wizard',
    version='1.0',
    description='Wizard running whonix_repository',
    author='troubadoour',
    author_email='trobador@riseup.net',
    url='https://github.com/troubadoour/whonix-repository-wizard',
    packages=['whonix_repository_wizard'],
    scripts=['whonix-repository-wizard'],
    data_files=datafiles
)