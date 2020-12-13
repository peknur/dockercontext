from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

name = "dockercontext"

setup(
    name=name,
    version="0.1",
    description="Run Docker containers within Python context manager",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Pekka Nurmi",
    author_email="peknur@gmail.com",
    url="https://github.com/peknur/dockercontext",
    install_requires=["docker"],
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
    python_requires=">=3.8"
)
