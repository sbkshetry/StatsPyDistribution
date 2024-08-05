from setuptools import setup, find_packages

setup(
    name="StatsPyDistribution",
    version='0.0.3',
    description="Statistics probability distribution",
    author='Shankar Kshetry',
    author_email='sbkshetry@gmail.com',
    url="https://github.com/sbkshetry/StatsPyDistribution",
    packages=find_packages(exclude=['contrib', 'docs', 'tests', '*.tests', '*.tests.*', 'tests.*']),
    classifiers=["Programming Language :: Python :: 3", "License :: OSI Approved :: Apache Software License", "Operating System :: OS Independent"]
)