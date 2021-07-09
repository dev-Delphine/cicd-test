from setuptools import find_packages, setup
from cicd_test import __version__

setup(
    name="cicd_test",
    packages=find_packages(exclude=["tests", "tests.*"]),
    setup_requires=["wheel"],
    version=__version__,
    description="Databricks Labs CICD Templates Sample Project",
    author="delphine",
)
