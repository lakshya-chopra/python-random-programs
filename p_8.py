s1 = input("enter first string: ")
s2 = input("enter second string: ")

l_1 = len(s1)
l_2 = len(s2)

if l_2 > l_1: print("s2 must be smaller than s1")

i = 0
c = 0

while i <= (l_1 - l_2):

    if s1[i:i+l_2] == s2:
        c += 1
    i += 1

print("number of occurences: ",c)
