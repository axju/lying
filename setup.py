import os
from setuptools import find_packages, setup

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
    README = readme.read()

setup(
    name='lying',
    version='0.0.1a2',
    description='run a fake terminal',
    long_description=README,
    url='https://github.com/axju/lying',
    author='Axel Juraske',
    author_email='axel.juraske@short-report.de',
    license='MIT',
    classifiers=[
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],

    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'pyfiglet',
    ],
    entry_points = {
        'console_scripts': [
            'lying=lying.cli:main',
        ]
    }
)
