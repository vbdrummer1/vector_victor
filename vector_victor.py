import math


class ShapeError(Exception):
    pass


m = [3, 4]
n = [5, 0]

v = [1, 3, 0]
w = [0, 2, 4]
u = [1, 1, 1]
y = [10, 20, 30]
z = [0, 0, 0, 1]


def vector_shape(vector):
    return (len(vector), )


def vector_add(v1, v2):
    if vector_shape(v1) == vector_shape(v2):
        return [sum(x) for x in zip(v1, v2)]
    else:
        raise ShapeError


def vector_sub(v1, v2):
    if vector_shape(v1) == vector_shape(v2):
        return [v1 - v2 for v1, v2 in zip(v1, v2)]
    else:
        raise ShapeError


def vector_sum(*args):
    new_list = [len(arg) == len(args[0]) for arg in args]
    if sum(new_list) != len(args):
        raise ShapeError
    return [sum(x) for x in zip(*args)]


def dot(*args):
    new_list = [len(arg) == len(args[0]) for arg in args]
    if sum(new_list) != len(args):
        raise ShapeError
    return sum([(a * b) for (a, b) in zip(*args)])


def vector_multiply(vector, multiplier):
    return[(x * multiplier) for x in vector]


def vector_mean(*args):
    new_list = [len(arg) == len(args[0]) for arg in args]
    if sum(new_list) != len(args):
        raise ShapeError
    return [sum(x)/len(x) for x in zip(*args)]


def magnitude(vector):
    return math.sqrt(sum(x**2 for x in vector))






# print(vector_shape(m))
# print(vector_add(v, w))
# print(vector_sub(v, w))
#print(vector_sum(w, v, u, y, z))
