from setuptools import setup, find_packages
import os


with open("README.md", "r") as fh:
    long_description = fh.read()


# get __version__ variable
exec(open("xfer/__version__.py").read())


setup(
    name="test_fungi-d",
    version=__version__,
    author="Example Author",
    author_email="author@example.com",
    description="A small example package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pypa/sampleproject",
    packages=find_packages(exclude=['tests*']),
    license="Apache License 2.0",
    classifiers=(
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'License :: OSI Approved :: Apache Software License',
        "Operating System :: OS Independent",
    ),
)
