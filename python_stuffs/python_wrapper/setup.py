from distutils.core import setup, Extension

example_module = Extension(
    '_example', sources = ['swig_example_wrap.cxx', 'swig_example.cpp']
)

setup (
    name = 'example',
    version = '0.1',
    author = 'SWIG Docs',
    description='simple swig example from docs',
    ext_modules=[example_module],
    py_modules=["example"],
)