from setuptools import find_packages
from setuptools import setup

with open("requirements.txt") as f:
    content = f.readlines()
requirements = [x.strip() for x in content if "git+" not in x]

setup(name='sign_language',
      version="1.0",
      description="learning sign language streamlit app",
      author="Stu Howarth",
      install_requires=requirements,
      packages=find_packages(),
      classifiers=[
        "Programming Language :: Python :: 3.10.6",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
      ])
