#to check if a number 'n' is prime, to generate prime numbers until n and to generate first n prime nums:

n = int(input("enter a number: "))

def check_prime(n:int):

    for i in range(2,n):

        if n % i == 0:

            return False
    else:
        return True

def gen_prime():

    i = 2
    while i:

        if check_prime(i):
            yield i
        i += 1

        

def n_primes(n):

    first_n_primes = list()
    gen = gen_prime()
    
    i = 1
    while len(first_n_primes) < n:

        num = next(gen)
        first_n_primes.append(num)

    return first_n_primes
            
            
    

print("is the number entered prime:",check_prime(n))

prime_nos_until_n = [x for x in range(2,n) if check_prime(x)]

print(f"primes_until_n : {prime_nos_until_n}")
print(n_primes(n))
    

        
