# Divides a large number in groups of 3 or 2, similar to phone numbers.

import numpy as np

number = str(input("Wich number do you want to split? "))

number = list(number)

#s = [1, 2, 3, 4, 5, 6, 7, 8]

if len(number)%3 != 0:
    n = len(number)//3+1

arr = [number[i:i+3] for i in range(0,len(number),3)]

final = '-'.join(str(x) for x in arr)

print(final)
