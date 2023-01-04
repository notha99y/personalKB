%module example

%{
#include "swig_example.h"
%}

%include "std_vector.i";
using namespace std;
%template(DoubleVector) vector<double>;

%include swig_example.h
