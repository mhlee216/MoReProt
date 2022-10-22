from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()
    
setup(name='moreprot', 
      version="1.0.0", 
      url='https://github.com/mhlee216/MoReProt', 
      packages=find_packages(), 
      author='Myeonghun Lee', 
      author_email="leemh216@gmail.com", 
      description='Molecular Fingerprint Recombination-based Protein Fingerprint', 
      long_description=long_description, 
      install_requires=["numpy >= 1.19.0", "rdkit >= 2021.09.2"],
      classifiers=['Programming Language :: Python :: 3', 'License :: OSI Approved :: MIT License'])
