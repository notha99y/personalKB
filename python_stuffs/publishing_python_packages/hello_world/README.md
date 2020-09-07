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