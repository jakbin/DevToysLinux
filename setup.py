from setuptools import setup
from devtoys.cli import __version__

with open("README.md", "r") as readme_file:
    readme = readme_file.read()

setup(
    name="devtoys",
    version=__version__,
    author="Jak Bin",
    author_email="jakbin4747@gmail.com",
    description="DevToys for Linux",
    long_description=readme,
    long_description_content_type="text/markdown",
    license="MIT License",
    url="https://github.com/jakbin/DevToysLinux",
    python_requires=">=3",
    install_requires=[""],
    classifiers=[
        "Programming Language :: Python :: 3.6",
        "Natural Language :: English",
        "Operating System :: OS Independent",
    ],
    keywords='devtoys, linux, devloper-tools',
    packages=["devtoys"],
    entry_points={
        'console_scripts': (
            'devtoys=devtoys.cli:main'
            )
        },
    zip_safe=False,
)
