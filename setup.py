from setuptools import setup
import pathlib

# The directory containing this file
HERE = pathlib.Path(__file__).resolve().parent

# The text of the README file
README = (HERE / "README.md").read_text()

setup(
    name="clashapi",
    packages=["clashapi"],
	include_package_data=True,
    version="1.4",
    description="Update IP address of Clash of Clans and/or Clash Royale API keys with token fetching",
    long_description=README,
    long_description_content_type="text/markdown",
    author="Roshan Dash",
    author_email="roshan1337d@gmail.com",
    url="https://github.com/roshan1337d/clashapi",
	license="MIT",
    keywords=["coc", "cr", "clash of clans",
              "clash royale", "clash", "royale", "clan", "api"],
    install_requires=["requests"]
)
