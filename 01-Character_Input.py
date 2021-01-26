# -*- coding: utf-8 -*-
name = input('What\'s your name traveller?\n')
text1 = 'Ah, what a fine name that is \'' + name.capitalize() + '\' it just sounds great!'
print(text1)

text2 = 'And what is your age?\n'
age = input(text2)

print('Well it seems that in ', 100 - int(age), 'years youll be 100 years old!')
multip = int(input('how many times '))
print('gugu gaga\n' * multip)
