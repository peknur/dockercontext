from setuptools import setup

with open("README.md", 'r') as f:
    long_description = f.read()

name = "dockercontext"

setup(
    name=name,
    version="0.1",
    description="Docker container context manager",
    long_description=long_description,
    author="Pekka Nurmi",
    author_email="peknur@gmail.com",
    packages=[name],
    install_requires=["docker==4.4.0"],
    python_requires=">=3.8"
)
