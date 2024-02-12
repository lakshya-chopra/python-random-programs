#program to find roots of a quadratic eqn
from math import sqrt

a,b,c = map(int,input("enter the coefficients of the quadratic ax^2 + bx + c, separated by a space: ").split())
print(f"The equation is {a}x^2 + {b}x + {c}")


disc = b**2 - 4*a*c

try:
    roots = lambda x : (-b - sqrt(disc))/2*a if x == 1 else (-b + sqrt(disc))/2*a

    root_lst = [roots(0),roots(1)]
    print("The roots are", root_lst)

except Exception as e:
    print("Imaginary roots", e)
