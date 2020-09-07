from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="helloworld-notha99y",
    version="0.0.1",
    description="Say Hello!",
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: GNU General Public License v2 or later (GPLv2+)",
        "Operating System :: OS Independent",
    ],
    url="https://github.com/notha99y/personalKB/tree/master/python_stuffs/publishing_python_packages/hello_world",
    author="Tan Ren Jie",
    author_email="renjie.tan91@gmail.com",
    py_modules=["helloworld"],
    package_dir={"": "src"},

    install_requires = [
        "blessings ~= 1.7",
    ],

    extras_require = {
        "dev": [
            "pytest >= 3.7",
            "check-manifest",
            "twine",
        ],
    },
)
