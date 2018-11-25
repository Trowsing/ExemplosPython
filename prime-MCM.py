# Prints primes and MCM's on a given range.

end = input("Display primes and MCM's  to: ")
for n in range(1, end+1):
     for x in range(2, n):
         if n % x == 0:
             print(n, 'equals', x, '*', n//x)
             break
     else:
        print(n, 'is a prime number')