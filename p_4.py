n = input("enter a character (digit, letter, special character) : ")

num_flag = False

try:

    if float(n): num_flag = True
    print("We have have a DIGIT")

except Exception as e:
    
    if ord(n) in list(range(65,91)) or ord(n) in list(range(97,123)):
        print("the data entered is in alphabet form")

    else:
        print("Special character bro")
        
