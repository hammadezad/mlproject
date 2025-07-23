from setuptools import find_packages, setup
from typing import List

HYPHEN_DOT = "-e ."

def get_requirements(file_path:str)-> List[str]:
    requirements=[]
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.strip() for req in requirements]

        if HYPHEN_DOT in requirements:
            requirements.remove(HYPHEN_DOT)
    return requirements

setup(
    name='mlproject',
    version='0.0.1',
    description= "General ML project for any project package",
    author='hammad_ezad',
    author_email='hammadezad@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)