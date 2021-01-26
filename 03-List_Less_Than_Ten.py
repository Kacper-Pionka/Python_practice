# -*- coding: utf-8 -*-
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

for i in range(len(a)):
    if a[i] < 5:
        print(a[i])
        
#different solution

print([aa for aa in a if aa < 5])
