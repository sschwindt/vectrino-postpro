from setuptools import setup, find_packages
from pathlib import Path


lines = Path(".").joinpath("__init__.py")
version = "1.1.8"
for line in lines.read_text().split("\n"):
    if line.startswith("__version__ ="):
        version = line.split(" = ")[-1].strip('"')
        break


setup(
    name="vectrino-postpro",
    version=version,
    python_requires=">=3.7",
    author="Sebastian Schwindt",
    author_email="sebastian.schwindt@iws.uni-stuttgart.de",
    url="https://github.com/sschwindt/vectrino-postpro",
    project_urls={
        "Documentation": "https://vectrino-postpro.readthedocs.io/",
        "Funding": "https://hydro-informatics.com/",
        "Source": "https://github.com/sschwindt/vectrino-postpro",
    },
    # this should be a whitespace separated string of keywords, not a list
    keywords="fluvial geospatial data processing numerical model validation",
    description="Post-process Vectrino II",
    license="BSD License",
    long_description=Path("./README.md").read_text(),
    long_description_content_type="text/markdown",
    packages=find_packages(),
    install_requires=[
        "pyyaml",
        "docutils>=0.15",
        "sphinx",
        "click",
        "pydata-sphinx-theme",
        "beautifulsoup4",
        'importlib-resources~=3.0.0; python_version < "3.7"',
    ],
    # dependency_links=[
    #     "git+https://github.com/sschwindt/flusstools-pckg#egg=flusstools-pckg"
    # ],
    include_package_data=True,
    extras_require={
        "code_style": ["pre-commit~=2.7.0"],
        "sphinx": [
            "numpy",
            "pandas",
            "nbclient",
            "myst-nb",
            "sphinx-togglebutton>=0.2.1",
            "sphinx-copybutton",
            "sphinxcontrib-bibtex",
            "ablog~=0.10.11",
        ],
        "testing": [
            "myst_nb",
            "coverage",
            "pytest~=6.0.1",
            "pytest-cov",
            "pytest-regressions~=2.0.1",
        ],
        "live-dev": ["sphinx-autobuild", "web-compile~=0.2.1"],
    },
    entry_points={
        "sphinx.html_themes": ["sphinx_book_theme = sphinx_book_theme"],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Development Status :: 4 - Beta",
    ],
)
