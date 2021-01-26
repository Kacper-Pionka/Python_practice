# -*- coding: utf-8 -*-
'''def invert():
    str = input('type in string: ')
    str = str.split()
    for i in range(1, len(str) + 1):
        print(str[-i], end = ' ')

def ask():
    YeOrNay = input('Do you want to invert string? (ye/nay)')
    if YeOrNay == 'ye':
        invert()
    elif YeOrNay == 'nay':
        print('ok')
    else:
        print('What?')'''

def ask():
    dtr = input('type in somthing pls ')
    dtr = ' '.join(dtr.split()[::-1])
    print(dtr)

ask()

