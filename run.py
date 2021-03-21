#!/usr/bin/python3
# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
from random import *
import math


def get_random_coordinates():
    return random(), random()


def draw_circle():
    center = (0, 0)
    radius = 1

    circle = plt.Circle(center, radius, fill=False, ec='b')

    a = plt.axes(xlim=(-1.2, 1.2), ylim=(-1.2, 1.2))
    a.add_patch(circle)
    a.set_aspect('equal')

    plt.grid(True)


def main():
    data = []
    gen_cnt = 100000
    inside_cnt = 0

    for i in range(gen_cnt):
        x, y = get_random_coordinates()
        data.append((x, y))

        xy_pow_sum = math.pow(x, 2) + math.pow(y, 2)
        if xy_pow_sum <= 1:
            inside_cnt += 1

    xs, ys = zip(*data)

    draw_circle()
    plt.scatter(xs, ys)

    plt.grid(True)
    plt.show()

    print("Div: {} (Expected: {})".format(str(inside_cnt/gen_cnt), math.pi/4))


if __name__ == '__main__':
    main()

