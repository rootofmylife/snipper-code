from setuptools import setup, find_packages

from snipper_code import __version__

setup(
    name='snipper-code',
    version=__version__,

    url='https://github.com/rootofmylife/snipper-code',
    author='Duc Do',
    author_email='dotrananhduc@gmail.com',

    packages=find_packages(),
    license='MIT',
    description='Short one-liner code snippets for Python',
)