import struct


def bin_to_float(b):
    """ Convert binary string to a float. """
    bf = int_to_bytes(int(b, 2), 8)  # 8 bytes needed for IEEE 754 binary64
    return struct.unpack('>d', bf)[0]


def int_to_bytes(n, minlen=0):  # helper function
    """ Int/long to byte string. """
    nbits = n.bit_length() + (1 if n < 0 else 0)  # plus one for any sign bit
    nbytes = (nbits + 7) // 8  # number of whole bytes
    b = bytearray()
    for _ in range(nbytes):
        b.append(n & 0xff)
        n >>= 8
    if minlen and len(b) < minlen:  # zero pad?
        b.extend([0] * (minlen - len(b)))
    return bytearray(reversed(b))  # high bytes first


def float_to_bin(f):
    """ Convert a float into a binary string. """
    ba = struct.pack('>d', f)
    # ba = bytearray(ba)  # convert string to bytearray - not needed in py3
    s = ''.join('{:08b}'.format(b) for b in ba)
    return s


import random as rnd
import math

left_x = -1000
left_y = None
right_x = 1000
right_y = None
n = 5
length = 100
mutate_coeff = 95
hem_const = 4
iterations_num = 200000


def func(x):
    return rosenbrock(x)


def booth_func(x):
    left_x = -10
    left_y = -10
    right_x = 10
    right_y = 10
    return (x[0] + 2 * x[1] - 7) * (x[0] + 2 * x[1] - 7) + (2 * x[0] + x[1] - 5) * (2 * x[0] + x[1] - 5)


def rosenbrock(x):
    # left_x=float('-inf')
    # right_x=float('inf')
    # left_y=None
    # right_y=None
    res = 0
    for i in range(n - 1):
        res = res + 100 * (x[i + 1] - x[i] * x[i]) * (x[i + 1] - x[i] * x[i]) + (1 - x[i]) * (1 - x[i])
    return res


def init():
    values = []
    for i in range(length):
        point = []
        if (left_y == None):
            for i in range(n):
                point.append(rnd.uniform(left_x, right_x))
        else:
            point.append(rnd.uniform(left_x, right_x))
            point.append(rnd.uniform(left_y, right_y))
        values.append(point)
    return values


def cross(point1, point2):
    print(point1)
    print(point2)
    bin_point1 = ''.join([float_to_bin(gen) for gen in point1])
    bin_point2 = ''.join([float_to_bin(gen) for gen in point2])
    first=""
    second=""
    for i in range (bin_point1.__len__()):
        if (i%2==0):
            first = first + bin_point1[i]
            second = second + bin_point2[i]
        else:
            first=first+bin_point2[i]
            second=second+bin_point1[i]
    gen_nums = int(bin_point1.__len__() / 64)
    f = []
    s = []
    for index in range(gen_nums):
        f.append(bin_to_float(first[index * 64:(index + 1) * 64]))
        s.append(bin_to_float(second[index * 64:(index + 1) * 64]))
    print(s)
    print(f)
    return [s, f]


def check_hemming(point1, point2):
    bin_point1 = ''.join([float_to_bin(gen) for gen in point1])
    bin_point2 = ''.join([float_to_bin(gen) for gen in point2])
    hem_calc = 0
    for i in range(bin_point1.__len__()):
        if (bin_point1[i] != bin_point2[i]):
            hem_calc = hem_calc + 1
    if (hem_calc > hem_const):
        return True
    return False


def selection(values):
    values.sort(key=lambda x: func(x))
    new_arr = values[0:length]
    return new_arr


def mutate(values):
    new_values = []
    for q in range(length):
        bin_point = "".join([float_to_bin(gen) for gen in values[q]])
        for k in range(bin_point.__len__()):
            if rnd.randint(0, 100) > mutate_coeff:
                if bin_point[k] == "0":
                    tmp = list(bin_point)
                    tmp[k] = "1"
                    bin_point = "".join(tmp)
                else:
                    tmp = list(bin_point)
                    tmp[k] = "0"
                    bin_point = "".join(tmp)

        gen_nums = int(bin_point.__len__() / 64)
        point = []
        for index in range(gen_nums):
            point.append(bin_to_float(bin_point[index * 64:(index + 1) * 64]))
        new_values.append(point)
    return new_values


values = init()
for j in range(iterations_num):
    values = mutate(values)
    for i in range(length - 1):
        if (check_hemming(values[i], values[i + 1])):
            children = cross(values[i], values[i + 1])
            values.append(children[0])
            values.append(children[1])
    values = selection(values)
    print(str(j) + " "+str(func(values[0]))+" " + str(values[0]))
#    print(func(values[0]))
print(values[0])
