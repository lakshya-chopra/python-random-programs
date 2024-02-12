#program which takes an integer input, form a new number which has the same number of digits at the 10's place and the digit at the
#unit's place is equal to the unit digit at the integer input.
from random import shuffle

def q1():
    a = int(input("Enter a number: "))

    n_digits = 0

    unit_dig = a % 10

    while a != 0:

        n_digits += 1
        a = a//10

    new_number = n_digits*10 + unit_dig
    print(new_number)

# program to print all the 3 combinations of a number:    
def q2():
    
    n_list = list(map(int, input(" Enter numbers : ").split()))


    n_combs = 6
    b = []
    
    while True:

        if len(b) == 6:
            break
        
        else:
            a = n_list.copy()
            
            shuffle(a)
            
            if a in b:

                continue
            else:

                b.append(a)

    for x in b:
        print(x)

##q2()
            
def gen_prime():


    i = 2
    while True:

        for j in range(2,i):

            if i %j == 0:
                break
        else:
            yield i

        i += 1

##gen = gen_prime()
##for i in range(10):
##    a = next(gen)
##    print(a)


def gcd(a,b):

    if b < a:
        sm = b
    else:
        sm = a

    g = 1

    for i in range(1,sm+1):

        if a%i == 0 and b%i == 0:
            g = i
    return f"GCD of {a},{b} is, {g}"

##print(gcd(24,120))

def gcd_recursive(a,b):

    #euclid's algorithm
    
    if b == 0:
        return a
    else:
        gcd(a-b,a%b)


def unsigned_bin_to_dec(a):

    #recursive
    
    if a%10 == 0:
        return a
    else:

        re 

        


        
