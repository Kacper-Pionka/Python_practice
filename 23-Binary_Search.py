# -*- coding: utf-8 -*-
import random

x = int(input('give me a number I\'ll check if it\'s in array\n'))

lst = [-8,1,3]

def boi(x,lst):
    low_val = 0
    high_val = len(lst) - 1
    
    while low_val <= high_val:
        middle = (low_val + high_val) // 2
        guess = lst[middle]

        if guess == x:
            return guess
        if guess > x:
            high_val = middle - 1
        else:
            low_val = middle + 1

    return None

def middle_val(x,lst):
    low_val = 0
    high_val = len(lst) - 1
    
    while low_val <= high_val:
        middle = (low_val + high_val) // 2
        guess = lst[middle]

        if guess == x:
            return guess
        if guess > x:
            high_val = middle - 1
        else:
            low_val = middle + 1

    return middle
    
    

def inhailed_boi(guess,lst,middle):
    if lst[middle] > x:
        middle = middle - 1
    if guess != x:
        question_1 = input('value is not in array, do you want to add value to the array? Y/N')
        if question_1=='Y' or question_1 =='y':
            lst.insert(middle+1,x)
            return lst
        else:
            return lst
    else:
        return lst
        
print(inhailed_boi(boi(x,lst),lst,middle_val(x,lst)))
        
