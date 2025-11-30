from setuptools import setup, find_packages
import pathlib

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text(encoding="utf-8")

setup(
    name="CosUI",
    version="0.1.0",
    description="A modern, GPU-accelerated GUI framework for Python.",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/cosyfluf/cosui",
    author="YOUR NAME",
    author_email="cosyfluf@gmail.com",
    license="MIT",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: User Interfaces",
        "Topic :: Multimedia :: Graphics",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Operating System :: OS Independent",
    ],
    keywords="gui ui framework modern gpu interface widget",
    packages=find_packages(exclude=["tests", "examples"]),
    include_package_data=True,
    install_requires=[
        "pyglet>=2.0.0",
    ],
    python_requires=">=3.7",
    project_urls={
        "Bug Reports": "https://github.com/cosyfluf/cosui/issues",
        "Source": "https://github.com/cosyfluf/cosui",
    },
)