from setuptools import setup, find_packages

setup(
    name="genz-calculator",
    version="1.0.0",
    author="aryan6673",
    description="✨ A minimalistic calculator with pastel aesthetics",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/aryan6673/genz-calculator",
    packages=find_packages(),
    install_requires=[
        "ttkthemes>=2.4.0",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
