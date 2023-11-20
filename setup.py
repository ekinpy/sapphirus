from setuptools import setup

with open("README.md", "r", encoding="utf-8") as file:
    LONG_DESCRIPTION = file.read()

setup(
    name="sapphirus",
    version="0.1.0",
    description="Transform your terminal into a canvas of colors with Sapphirus.",
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    url="https://github.com/ekinpy/sapphirus",
    author="Ekin Aksu",
    license="MIT License",
    keywords="terminal, style, color, coloring, cli, colors",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11"
    ]
)
