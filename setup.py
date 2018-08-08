from setuptools import setup, find_packages
import os


ROOT = os.path.dirname(__file__)


with open("README.md", "r") as fh:
    long_description = fh.read()


def get_version():
    return open(os.path.join(ROOT, 'VERSION')).read()


setup(
    name="test_fungi-d",
    version=get_version(),
    author="Example Author",
    author_email="author@example.com",
    description="A small example package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pypa/sampleproject",
    packages=find_packages(where='projname', exclude=['tests*']),
    package_dir={"": "projname"},
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
