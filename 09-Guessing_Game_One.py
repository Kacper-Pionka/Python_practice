# -*- coding: utf-8 -*-

import random

rando = random.randint(0, 9)

num = -rando

guess = 1

ask = 'nay'

while ask != 'ende':
    while num != rando:

        num = int(input('Type in number '))
    
        if num > rando:
            print('number is too big, try again: ')
        if num < rando:
            print('number is too small, try again: ')
        if num == rando:
            print('Yay! You guessed it random number is:', rando)
            print('It took you', guess, 'guesses to win')
            ask = input('To end type in \'ende\'\n')

        guess += 1
