import os
import re
import setuptools

requires = ['amazon.ion>=0.5.0,<1]

setuptools.setup(
    name='pythonplaygroundz',
    version='1.0.1',
    description='description',
    long_description='long_description',
    long_description_content_type='text/markdown',
    author='byron',
    packages=setuptools.find_packages(),
    install_requires=requires,
    license="Apache License 2.0z"
)
  
