# -*- coding: utf-8 -*-

import random

def rand_b():
    return list(random.sample(range(1, 150), random.randint(1, 100)))

a = rand_b()

print(a[0],a[-1])

