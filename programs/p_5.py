
num_to_words = {1: 'One', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five',
             6: 'Six', 7: 'Seven', 8: 'Eight', 9: 'Nine', 10: 'Ten', 
            11: 'Eleven', 12: 'Twelve', 13: 'Thirteen', 14: 'Fourteen', 
            15: 'Fifteen', 16: 'Sixteen', 17: 'Seventeen', 18: 'Eighteen', 
            19: 'Nineteen', 20: 'Twenty', 30: 'Thirty', 40: 'Forty', 
            50: 'Fifty', 60: 'Sixty', 70: 'Seventy', 80: 'Eighty', 
            90: 'Ninety', 0: 'Zero'}


n = int(input("enter number: "))

lst = []
l = 0

while n != 0:

    if n >= 10:
        l = n%10
        s = n - l

        lst.append(num_to_words[s])

    else:
        lst.append(num_to_words[l])

    
    n = n//10

print(' '.join(lst))
