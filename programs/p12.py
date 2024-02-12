t1 = (1,2,5,7,9,2,4,6,8,10)

for i in range(len(t1)):

    if len(t1)/(i+1) == 2:
        print(t1[i])
        print()

    else:
        print(t1[i],end=' ')
        
t2 = (11,13,15)

t2 = list(t2)
t1 = list(t1)

t1.extend(t2)

t1 = tuple(t1)

print()
print(t1)



tup_new = ()
for i in t1:
    if i%2 == 0:
        tup_new += (i,)

print('even values of t1: ',tup_new)

max_val = min_val = t1[0]


for i in t1:

    if i > max_val:
        max_val = i

    if i < min_val:
        min_val = i

print("The min val from t1:",min_val)
print("The max val from t1:",max_val)
