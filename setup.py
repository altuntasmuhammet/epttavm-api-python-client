import os
from setuptools import setup

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

requirements_filename = os.path.join(os.path.dirname(__file__), 'requirements.txt')
with open(requirements_filename) as f:
    PACKAGE_INSTALL_REQUIRES = [line[:-1] for line in f]

setup(
    name = "epttavm_api_python_client",
    version = "0.0.1b",
    author = "Muhammed Ali Altuntas",
    author_email = "altuntasmuhammet96@gmail.com",
    description = ("Unofficial ePttAVM API Python Client"),
    license = "MIT",
    url="https://github.com/altuntasmuhammet/epttavm-api-python-client",
    packages=['epttavm_api_client'],
    long_description=read('README.md'),
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache License, 2.0",
        "Operating System :: OS Independent",
    ],
    install_requires=PACKAGE_INSTALL_REQUIRES,
    python_requires=">=3.8",
)
