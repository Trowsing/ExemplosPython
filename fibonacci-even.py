# Fibonacci even sum to given range

ran = int(input("Sum even in range: "))
a, b, suma = 1, 2, 0

while a <= ran:
    if a % 2 == 0:
        print(a)
        suma += a
    a, b = b, a + b
print(suma)
