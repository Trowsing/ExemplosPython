"""
Given an array of numbers and a 'target', finds
which indexes addition equals target.
Using linear search algorithm
"""

list = [1, 7, 1, 15]
target = 9
i = 0
j = len(list) - 1

while i < j:
    if list[i] + list[j] == target:
        print(i, j)
        break
    elif list[i] + list[j] < target:
        i += 1
    elif list[i] + list[j] > target:
        j -= 1
