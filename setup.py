from setuptools import setup, find_packages

setup(
  name='prsaw',
  version='0.1.2',
  description='PRSAW, an acronym for `Python Random Stuff API Wrapper`, is a wrapper for the Random Stuff API.',
  long_description=open('README.md').read(),
  long_description_content_type = "text/markdown",
  url = "https://github.com/CodeWithSwastik/prsaw",  
  author='Swas.py',
  author_email='cwswas.py@gmail.com',
  license='MIT', 
  classifiers=[
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3'
  ],
  keywords='random stuff, api, wrapper', 
  packages=find_packages(),
  install_requires=['aiohttp'] 
)