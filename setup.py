from setuptools import find_packages,setup
from typing import List
#Hypen_e_dot='-e.'

def get_requirements(file_path:str)->List[str]:
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","")for req in requirements]

        return requirements

       ## if Hypen_e_dot in requirements:
         #   requirements.remove[]
setup(
    name='DYNAMIC PRICING STRATEGY',
    version='0.0.1',
    author='GARJALA MEGHANSH RAO',
    author_email='garjala14@gmail.com',
    install_requires=get_requirements("requirements.txt"),
    packages=find_packages()
)
