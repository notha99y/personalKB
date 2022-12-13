# Repo to write python wrapper over other languages
## Marshalling
Marshalling is what the Python bindings are doing when they prepare data to move it from Python to other languages or vice versa.

This is neccesarry as Python and the other languages store data in different ways. Python stores everything as an Object

## Understanding Mutable and Immutable Values
Python objects can be either Mutable or immutables. 

C has a similar concept with function parameters when talking about pass-by-value or pas-by-reference. 

In C, all parameters are pass-by-value. If you want to allow a function to change a variable in the caller, then you need to pass a pointer to that variable.

## Managing Memory
Python has a garbabe collector while other languages may or may not have this. 

You'll need to be aware of where the memory of each object is allocated and ensure that it's only freed on the same side of the language barrier.

e.g. a Python object is created when you set `x=3`. The memory for this is allocated on the Python side and needs to be garbage collected. Fortunately for Python, it is quite difficult to do anything else. 

But for C, where you directly allocate a block of memory:
```c
int* iPtr = (int*)malloc(sizeof(int));
```
When you do this, you need to ensure that this pointer is freed in C. This may mean manually adding code to your Python bindings to do this.

