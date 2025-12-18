#setup.py is responsible for creating the package distribution. and deploy in pypi
from setuptools import setup, find_packages # Importing necessary functions from setuptools
from typing import List

def get_requirements(file_path: str) -> list[str]:
    """Reads the requirements from a given file and returns them as a list."""
    requirements = []
    with open(file_path, 'r') as file:
        requirements = file.readlines()
        requirements = [req.replace("\n", "") for req in requirements] # Remove newline characters
        #-e . is used for editable installs, we don't want to include it in the requirements
        if '-e .' in requirements:
            requirements.remove('-e .') # Remove editable install line if present   
    return requirements

setup(
    name="mlproject", # Name of the package
    version="0.1", # Version of the package
    author="Batman", # Author of the package
    author_email="bhuvanbn01@gmail.com", # Author's email
    packages=find_packages(), # Automatically find packages in the directory
    install_requires= get_requirements('requirements.txt') # Function to read dependencies from requirements.txt
)
# setup.py finds the packages in the directory by looking for __init__.py files and includes them in the distribution.
# eg : if we want src folder to be included in the package we need to add __init__.py file in src folder.