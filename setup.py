import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

# can't use toml in setup.py and there's only one dependency right now
package_list = [
    "euclid3"
]

setuptools.setup(
    name="polyskel",
    version="0.0.0",
    author="https://github.com/Botffy",
    author_email="",
    description="A pip-installable version of Bottfy's polyskel.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    install_requires=package_list,
    url="https://github.com/1build/polyskel",
    packages=setuptools.find_packages("polyskel", exclude=["tests"]),
    classifiers=[
        "Programming Language :: Python :: 3"
    ],
    python_requires='>=3.7',
)