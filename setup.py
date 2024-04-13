from setuptools import setup, find_packages

VERSION = '1.0.0'
DESCRIPTION = 'Kinesis video parser'

setup(
    name='parser',
    packages=find_packages(),
    version='0.1.0',
    description='kvs_consumer',
    author='seema',
    packages=find_packages(),
    install_requires=['boto3','timeit','imageio','re'],
)