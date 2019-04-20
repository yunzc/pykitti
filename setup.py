from setuptools import setup

setup(
    name='pykitti',
    version='0.4.0',
    description='A minimal set of tools for working with the KITTI dataset in Python',
    author='Lee Clement',
    author_email='lee.clement@robotics.utias.utoronto.ca',
    url='https://github.com/yunzc/pykitti',
    license='MIT',
    packages=['pykitti'],
    install_requires=['numpy', 'matplotlib', 'Pillow', 'pandas']
)
