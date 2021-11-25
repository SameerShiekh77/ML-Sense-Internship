'''
You are given a string .
 contains alphanumeric characters only.
Your task is to sort the string  in the following manner:

All sorted lowercase letters are ahead of uppercase letters.
All sorted uppercase letters are ahead of digits.
All sorted odd digits are ahead of sorted even digits.

'''


# Take Input from user
validation = True
string = input("Enter any String: ")
while validation:
    try:
        if string == '':
            print("Please Write Something....")
            string = input("Enter any String: ")
        elif len(string) > 0 and len(string) < 1000:
            validation = False
    except:
        print("Please enter valid string")


# now sorted all characters and create list of each
lowerCharacters = sorted(filter(lambda x: x.islower(),string))
upperCharacters = sorted(filter(lambda x: x.isupper() ,string))
oddNumbers = sorted(filter(lambda x: x.isnumeric() and int(x)%2 ==1 ,string))
evenNumbers = sorted(filter(lambda x: x.isnumeric() and int(x)%2 == 0 ,string))

# join all letters by .join method
sortedString = "".join(lowerCharacters + upperCharacters + oddNumbers + evenNumbers)

# print the sorted result
print("\nSorted String: " + sortedString)