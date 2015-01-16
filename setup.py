from setuptools import setup, find_packages
from ice_setup import __version__

setup(
    name='ice_setup',
    author='Inktank',
    version=__version__,
    packages=find_packages(),
    zip_safe=False,
)
