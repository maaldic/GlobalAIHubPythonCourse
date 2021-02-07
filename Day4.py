number_of_primes = 0

def primeFinder(x):
    if x >= 2:
        for y in range(2, x):
            if not (x % y): #If the statement is true it returns false.
                return False
    else:
        return False
    return True

for i in range(1,100):
    if primeFinder(i): #calling the function.
        number_of_primes += 1
        print (i)

print (str(number_of_primes) + " prime numbers.")







