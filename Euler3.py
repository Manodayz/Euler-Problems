import math

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

primes = []
numrunner = 2  # Start with the first prime number

while numrunner <= 600851475143:
    if is_prime(numrunner):
        primes.append(numrunner)
    numrunner += 1
    
last_prime = primes[-1]
print("The last prime is :")
print(last_prime)