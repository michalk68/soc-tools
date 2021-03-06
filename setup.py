import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="soc-tools",
    version="0.1",
    author="Michal Kavan",
    author_email="me@michalkavan.cz",
    description="Set of tools that can be useful for SOC analysts",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/michalk68/soc-tools",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)