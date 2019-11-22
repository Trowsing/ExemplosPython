# print all the even Fibonacci numbers up to n
# and add each even number found to the sum.

a, b, suma = 1, 2, 0
n = input("Max limit to sum: ")

while a <= n:
    if a % 2 == 0:
        print(a)
        suma += a
    a, b = b, a + b
print("The total is: ", suma)
