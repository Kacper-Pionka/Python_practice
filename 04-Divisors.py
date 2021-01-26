# -*- coding: utf-8 -*-
num = int(input('Type number, program will print out it devisors: '))
print([i for i in range(1, num) if num%i == 0])
