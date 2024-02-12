#pyramid:

def pyramid(n:int):

    spaces = n

    for i in range(1,n+1): #for rows

        print(" "*spaces,end='') #first print the spaces

        for j in range(0,i): #then for each rows, iterate to print the * one by one
            print("* ",end='')

        spaces -=1 #finally decrease the num of spaces and print a new line.
        print()

pyramid(10)

def rev_pyramid(n):

    spaces = 0

    for i in range(n,0,-1):

        print(" "*spaces,end='')

        for j in range(0,i):

            print("* ",end = '')

        spaces += 1
        print()

rev_pyramid(10)

        
            
