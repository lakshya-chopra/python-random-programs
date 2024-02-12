#program: 1) find the frequency of a char in a string, replace char by another char, remove all occurences or remove the first occurence

def freq_char(string):

    c = input("enter the character whose frequency you'd like to find: ")
    freq = 0

    for i in string:

        if i == c:
            freq += 1

    print(f'The character {c} occurs {freq} times in "{string}"')

def rep_first_occurence(ch_old,ch_new,lst):
    
        for i , e in enumerate(lst):

            if e == ch_old:
                lst[i] = ch_new
                return lst
    

def rep_char(string):

    lst = list(string)

    ch_old, ch_new = input("Enter the character you want to replace and the character that replaces it (separated by a space): ").split()

    replace_all = True if input("Replace all (y/n): ").lower() == 'y' else False

    if replace_all:
        for i , e in enumerate(lst):

            if e == ch_old:
                lst[i] = ch_new
            else:
                continue

    else:

        lst = rep_first_occurence(ch_old,ch_new,lst)
        
    return ''.join(lst) #returns the string to the global namespace



if __name__ == "__main__":
    
    s = input("enter the string: ")
    
    freq_char(s)

    print("Modified string: ",rep_char(s))



    



    
