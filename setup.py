from setuptools import setup, find_packages
import sys

install_requires = []
if sys.version_info < (3, 4):
    install_requires.append('enum34')
    install_requires.append('asyncio==0.2.1')

setup(
    name="Vase",
    version="0.1.4",
    author="Vladimir Kryachko",
    author_email="v.kryachko@gmail.com",
    description = "Async Web framework based on Tulip/asyncio",
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.4",
    ],
    install_requires = install_requires,
    packages=find_packages(exclude=["*.tests", "*.tests.*", "tests.*", "tests"]),
)
