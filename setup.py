from setuptools import find_packages, setup

setup(
    name="prsaw",
    version="0.3.0",
    description="PRSAW, an acronym for `Python Random Stuff API Wrapper`, is a wrapper for the Random Stuff API.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/CodeWithSwastik/prsaw",
    author="Swas.py",
    author_email="cwswas.py@gmail.com",
    license="MIT",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
    ],
    keywords="random stuff, api, wrapper",
    packages=find_packages(),
    install_requires=["instant-api-client==0.1.1"],
)
