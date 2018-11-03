"""
This snippet multiplies all the 3 digit numbres to get
all the possible palindromes to return the biggest one
and some other interesting information.
"""
list = []
total = 0
for i in range(99, 999, +1):
    for j in range(99, 999, +1):
        string = j*i
        total += 1
        #print(j, i, string)
        if str(string) == str(string)[::-1]:
            #print(string)
            list.append(string)
            list.sort()
print("Biggest palindrome is: ", list[-1])
print("Total palindromes are: ", len(list))
print("Total possible products: ", total)
