# -*- coding: utf-8 -*-
text1 = 'type number the programme will check if its even or odd: '
num = int(input(text1))

if num%4 == 0:
    print('Number is devidable by 4')
elif num%2 == 0:
    print('Number is devidable by 2')
else:
    print('Number is odd')

#Additional part

text2 = 'type number the programme will check if it\'s devidable by another given number: '
num = int(input(text2))
text3 = 'type number that will be devider: '
dev = int(input(text3))

if num%dev == 0:
    print('number', num, 'is devidable by', dev)
else:
    print('number', num, 'is not devidable by', dev)
