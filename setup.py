from setuptools import setup

name = "dockercontext"

setup(
    name=name,
    version="0.1",
    description="Docker container context manager",
    author="Pekka Nurmi",
    author_email="peknur@gmail.com",
    packages=[name],
    install_requires=["docker==4.4.0"],
    python_requires=">=3.8"
)
