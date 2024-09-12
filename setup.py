from setuptools import find_packages, setup
from typing import List
def get_requirements(file_path : str)->List[str]:
    '''
    This function will return the list of requirements.
    '''
    requirements = []
    with open(file_path) as f:
        requirements= f.readlines()
        requirements = [line.replace('\n', '') for line in requirements]
        if '-e .' in requirements:
            requirements.remove('-e .')
        return requirements
    
setup(
    name = 'mlproject',
    version='0.0.1',
    author='Shyam',
    author_email='golishyamgolisai@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)