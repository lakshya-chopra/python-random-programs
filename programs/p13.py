cond = True

while cond:

    name = input("Name: ")

    for i in name:
        if not(i.isalpha()):
            print("enter a valid name")
            break
    else:
        cond = False  #if doesn't break then else executes => name is valid!
