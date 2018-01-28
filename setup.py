from setuptools import setup, find_packages

setup(
    name='urbanoctowaddle',
    version=0.1,
    description='A test repo',
    author='Tai Sakuma',
    author_email='tai.sakuma@gmail.com',
    packages=find_packages(exclude=['docs', 'tests']),
)
