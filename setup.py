from setuptools import setup, find_packages

with open("requirements.txt") as f:
    required_packages = f.read().splitlines()

setup(
    name="dconfig",
    version="0.1",
    description="A configuration lib, fully interchangable with detectron2.config, with minimal dependencies",
    author="Alexander Goryunov",
    packages=find_packages(),
    install_requires=required_packages,
)