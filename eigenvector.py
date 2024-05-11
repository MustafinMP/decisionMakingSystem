import numpy as np
from math import sqrt


def product(vector: list[float]) -> float:
    p = 1
    for i in vector:
        p *= i
    return p


def estimation_of_the_eigenvector(table):
    vector = []
    for row in range(len(table)):
        vector.append(product(table[row]) ** 0.25)
    return vector


def normalize(vector: list[float]) -> list[float]:
    s = sum(vector)
    for i in range(len(vector)):
        vector[i] /= s
    return vector

