number_range = 1000
primes = []
num = 0
while num < number_range:
    num += 1
    isprime = True
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                isprime = False
                break
        if isprime == True:
            primes.append(num)
print(primes)
print(len(primes))
