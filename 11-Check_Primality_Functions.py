# -*- coding: utf-8 -*-

def input_uno():
    return int(input('Type number, program will check if it\'s prime: '))

#for num in range(1, 1000):
num = input_uno()

a = [i for i in range(1, num) if num%i == 0]

if len(a)<2: print('Number', num, 'is prime')
else: print('Number', num, 'is not prime, in fact it\'s devisors are: ', a)
