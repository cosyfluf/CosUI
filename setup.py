from setuptools import setup, find_packages
import pathlib

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text(encoding="utf-8")

setup(
    name="CosUI",
    version="0.2.0",
    description="A modern, custom-drawn GUI framework for Python.",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/cosyfluf/cosui",
    author="cosyfluf",
    author_email="cosyfluf@gmail.com",
    license="MIT",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: User Interfaces",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    keywords="gui ui framework modern custom render widget",
    packages=find_packages(exclude=["tests", "examples"]),
    include_package_data=True,
    install_requires=[
        "pygame>=2.0.0",  # Used only for window creation and low-level drawing
    ],
    python_requires=">=3.7",
    project_urls={
        "Bug Reports": "https://github.com/cosyfluf/cosui/issues",
        "Source": "https://github.com/cosyfluf/cosui",
    },
)