import pathlib
from setuptools import setup
from setuptools import find_packages

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

setup(
    name="Chip8 Emulator",
    version="1.0.0",
    description="An OO oriented Python Chip8 Emulator",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/hasii2011/Chip8Emulator",
    packages=find_packages(),
    include_package_data=True,
    install_requires=["pygame", "python3-albow"]
)
