from setuptools import setup, find_packages

setup(
    name = "hypixel_py",
    version = "0.1.0",
    description = "A Python wrapper for the Hypixel API.",
    long_description = open("README.md").read(),
    long_description_content_type = "text/markdown",
    author = "Cursor-Gaming",
    author_email = "cursorgaming463@gmail.com",
    url = "https://github.com/Cursor-Gaming/hypixel_py",
    packages = find_packages(),
    install_requires = [
        "requests"
    ],
    classifiers = [
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires = '>=3.6',
)