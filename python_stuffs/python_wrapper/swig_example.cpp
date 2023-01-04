/*
Simple cpp function to do square of a vector
*/
#include "swig_example.h"
#include <iostream>

vector<double> square(vector<double>vec)
{
    for (int i=0; i<vec.size(); i++)
    {
        vec[i] = vec[i]*vec[i];
    }
    return vec;
}