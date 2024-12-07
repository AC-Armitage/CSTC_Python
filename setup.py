# setup.py
from setuptools import setup, find_packages

setup(
    name="CSTC_PyPack_IP2Bin",
    version="0.1",
    packages=find_packages(),
    description="An example package for class, converts your public ip to binary ",
    author="Abderrahim Chabir",
    author_email="chabirabd@gmail.com",
    url="https://github.com/AC-Armitage/CSTC_Python"
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)

