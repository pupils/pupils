# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='pupils',
    version='0.0.1',
    description='Application for the management of any event related to \
				educational, sports or leisure, in which the protagonists are children.',
    long_description=readme,
    author='Fco Javier Lucena / Serafín Vélez Barrera',
    author_email='fran@pupils.es / serafin@pupils.es',
    url='https://github.com/pupils/pupils',
    license=license,
    packages=find_packages(exclude=('tests', 'docs', 'helpers'))
)
