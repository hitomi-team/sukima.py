from setuptools import setup

setup(
    name="sukima.py",
    version="sticks and rocks",
    description="API wrapper for Sukima",
    url="https://github.com/hitomi-team/sukima.py",

    install_requires=["pydantic",
                      "aiohttp"]
)