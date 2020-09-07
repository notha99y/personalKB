# Publishing (Perfect) Python Packages on PyPI
[source](https://github.com/judy2k/publishing_python_packages_talk)

## Install package in the current directory
### Build the package
```bash
python setup.py bdist_wheel
```
### Installing locally
```bash
pip install -e .
```

## Write Documentation
### ReStructured Text
- Pythonic
- Powerful
- Can use Sphinx
### Markdown
- More widespread
- Simpler
- Can use MkDocs

## Testing
### Pytest
#### Declare Development Dependencies
```python
# setup.py
setup(
    ...
    extras_require = {
        'dev': [
            'pytest>=3.7',
        ],
    },
)
```
To install the helloworld package along with the tools you need to develop and run tests, run the following
```bash
pip install -e .[dev]
```
#### Install vs Extras
- install_requires
    - is for production dependencies (Flask, Click, Numpy, Pandas)
    - version should be as relaxed as possible (>3.0, <4.0)
- extras_require
    - is for optional requirements: (Pytest, Mock, Coverage.py)
    - versions should be as specific as possible

### Tox
#### tox.ini
```
[tox]
envlist = py36, py37

[testenv]
deps = pytest
commands = pytest
```
#### Testing with tox
```bash
pip install tox
tox
```

### Travis
For trying it on a clean computer
#### .travis.yml
```
language: python
sudo: false

python:
    - "3.6"
    - "3.7-dev"

install:
    - pip install tox
script:
    - tox -v -e py
```

## Extra Credit
### Badges!
- Code Coverage (Coveralls, codecov.io)
- Quality Metrics (Code Climate, Landscape.io)

### Manage versions
- bumpversion

### Test on different OS
- MacOS
- Windows

### More Documentations
- Contributors Section
- Code of Conduct

# Use Cookiecutter
```bash
pip install cookiecutter

cookiecutter gh:ionelmc/cookiecutter-pylibrary
```

# Installing packages not through PyPI
## Installing packages via Git
It’s quite common to want to pip install a version of a package that hasn’t been released to PyPI, but is available on its Git repository host, such as GitHub. If the package is pure Python or has a relatively simple build process integrated with setup.py, it can be installed from source.

Here are the supported forms:
```bash
[-e] git+http://git.example.com/MyProject#egg=MyProject
[-e] git+https://git.example.com/MyProject#egg=MyProject
[-e] git+ssh://git.example.com/MyProject#egg=MyProject
[-e] git+file:///home/user/projects/MyProject#egg=MyProject
```

Passing a branch name, a commit hash, a tag name or a git ref is possible like so:
```bash
[-e] git+https://git.example.com/MyProject.git@master#egg=MyProject
[-e] git+https://git.example.com/MyProject.git@v1.0#egg=MyProject
[-e] git+https://git.example.com/MyProject.git@da39a3ee5e6b4b0d3255bfef95601890afd80709#egg=MyProject
[-e] git+https://git.example.com/MyProject.git@refs/pull/123/head#egg=MyProject
```


## Installing via tarballs


### Why use python -m pip install instead of pip install
In brief, the main problem:

Most Python developers install more than one Python version. This is either due to their OS including an old Python by default, working on projects that use different versions, or simple experimentation.

Running the `pip` executable with more than one Python version can be unpredictable. When you upgrade pip on one version, it can replace the executable from the other. So running pip install at one moment might use Python 2.7, then later it could use Python 3.7.

It’s not hard to see how this can lead to problems understanding what’s installed where and when.

When you use `python -m pip`, the `pip` package is executed explicitly with the version of Python that python points to. If you have other interpreters, you can use them precisely and predictably, e.g. `python3.6 -m pip`.