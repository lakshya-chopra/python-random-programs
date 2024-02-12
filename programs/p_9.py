inp_lst = input('enter the inputs (separated by a space): ').split()

cube_sum = 0

for i in inp_lst:
    
    if i.isdigit():

        if eval(i)%2 == 0: cube_sum += int(i)**3 #first eval to account for all numeric values (float or int) and if %2 == 0 then the value is int.

    else:
        continue


print("cubic sum: ",cube_sum)

#or

even_ints = [int(x)**3 for x in inp_lst if x.isdigit() and eval(x)%2 == 0]
print("cube_sum through list comprehension", sum(even_ints))
