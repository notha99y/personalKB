# Python wrapper over c/cpp

## Setting up
You would need the following setup in your environment
- C++ library installed
- Python development tools
- Python 3.6 and greater
- The `invoke` toll

To create your own conda environment, run the following
```bash
conda env create -f env.yml
```

## Invoke
Build project
```bash
invoke build-cmult
```
See which tasks are available
```bash
invoke --list
```
Runs the build and test tasks for all tools
```bash
invoke all
```
removes any generated files
```bash
invoke clean
```

## ctypes
ctypes is a standard library in Python and it is used to for creating python bindings. It provides a low-level toolset for loading shared libraries and marshalling data between Python an C

### Calling the function
All of the code to load C library and call the function will be in your Python program, no extra steps is needed. 

To create your Python bindings in ctypes, you need to these:
1. Load your library
1. Wrap some of your input parameters
1. Tell ctypes the return type of your function


## SWIG

# Reference
- https://realpython.com/python-bindings-overview/

