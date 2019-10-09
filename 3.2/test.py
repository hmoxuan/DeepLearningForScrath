#!/usr/bin/python
# coding:utf-8

import numpy as np
import matplotlib.pyplot as plt


def step_function(x):
    return np.array(x > 0, dtype=np.int)


def sigmoid(x):
    return 1 / (1 + np.exp(-x))


plt.title("Step function")
plt.xlabel("x axis")
plt.ylabel("y axis")
plt.ylim(-0.1, 1.1)

x = np.arange(-5.0, 5.0, 0.1)
y = step_function(x)
plt.plot(x, y)

y = sigmoid(x)
plt.plot(x, y)

plt.show()
