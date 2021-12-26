import setuptools
from setuptools import setup

setup(
    name="sukima-py",
    version="0.0.1a",
    description="API wrapper for Sukima",
    url="https://github.com/hitomi-team/sukima.py",

    install_requires=["pydantic",
                      "aiohttp"],
    # package_dir={"": "sukipy"}
    packages=setuptools.find_packages(),
)
