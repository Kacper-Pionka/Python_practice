# -*- coding: utf-8 -*-

import random

def rand_a():
    return list(random.sample(range(1,30),7))

def rand_b():
    return list(random.sample(range(1,30),12))

a = rand_a()
b = rand_b()

print(str(a) + '\n' + str(b))

list_boi = set([x for x in a for z in b if x == z])

print(list_boi)
