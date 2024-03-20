import setuptools
from typing import List

Hyphen_e = '-e .'

def get_requirements(filepath: str) -> List[str]: 
    """Returns list of requirements
    Input = Filepath(str),
    Output= List of required packages(str)
    """
    requirements = []
    try:
        with open(filepath) as file_object:
            requirements = [line.replace("\n", "") for line in file_object.readlines()]
            requirements = [line for line in requirements if Hyphen_e not in line]
    except FileNotFoundError:
        print(f"Requirements file not found at {filepath}")
    return requirements

setuptools.setup(
    name="MlProject",
    version="0.0.1",
    author="Chirag",
    author_email="chirag@example.com",  # Provide a valid email address here
    description="A small python package for ml app",
    install_requires=get_requirements("Requirements.txt")
)
