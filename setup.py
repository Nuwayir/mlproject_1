from setuptools import setup, find_packages
from typing import List

HYPEN_E_DOT='-e .'
def get_requirements(file_path:str)->List[str]:
    '''
    this function will return the list of requirements
    '''
    requirements=[]
    with open(file_path)as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","")for req in requirements]# beacuse i want the liberries only not the \n 
        # to remove -e . from the requiremrns file :
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    return requirements
    
    
setup(
    name="mlproject_1",
    version="0.1.0",
    author="Nuwayir",
    author_email="nuwaiyr@gmail.com",
    description="A brief description of your project",
    # long_description=open('README.md').read(),
    # long_description_content_type="text/markdown",
    url="https://github.com/Nuwayir/yourproject",
    packages=find_packages(),  # Automatically find all packages in your project
    # for more practiacl way we have to create function : get_requirements()
    install_requires=get_requirements('requirement.txt')
)
