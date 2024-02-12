s1 = input("enter string 1: ")
s2 = input("enter string 2: ")

n = int(input("enter the amount of characters you'd like to swap: "))

s1_lst = list(s1)
s2_lst = list(s2)

for i in range(0,n):
    s1_lst[i],s2_lst[i] = s2_lst[i],s1_lst[i]

print("modified strings:", 's1:',''.join(s1_lst))
print('s2:',''.join(s2_lst))
