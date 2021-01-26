# -*- coding: utf-8 -*-
import random
import string

ask = []
ask_a = ['n', 'N', 'no', 'No', 'NO', 'nO', 'nay']

ter = int(input('type lenght of password (max lengt is 62): '))

while ask not in ask_a:
    print(''.join(random.sample(string.ascii_letters + string.digits, ter)))
    ask = input('do you want to generate password again?(n/y)')
