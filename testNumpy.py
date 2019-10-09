#!/usr/bin/python
# coding:utf-8

import numpy as np

x = np.array([1.0, 2.0, 3.0])
y = np.array([2.0, 4.0, 6.0])
print("x type is:", type(x))
print("x = ", x)
print("y = ", y)
print("x+y = ", x+y)
print("x-y = ", x-y)
print("x*y = ", x*y)
print("x/y = ", x/y)
print("x/2 = ", x/2)


A = np.array([[1, 2], [3, 4]])
B = np.array([[3, 0], [0, 6]])
print("A=", A)
print("A.shape=", A.shape)
print("A.dtype=", A.dtype)
print("B=", B)
print("A+B = ", A+B)
print("A*B = ", A*B)
print("A*10 = ", A*10)
