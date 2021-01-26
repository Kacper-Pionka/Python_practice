# -*- coding: utf-8 -*-

list_1 = [1, 5, 6, 12, 16]
list_2 = [1, 1, 1, 12, 15]

def OkFunction():

    return [i for i in list_1 if i not in list_2]

print(OkFunction())
