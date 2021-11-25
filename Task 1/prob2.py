'''
You are given a string . Suppose a character 'c' occurs consecutively X times in the string.
Replace these consecutive occurrences of the character 'c' with (X,c) in the string.

For a better understanding of the problem, check the explanation.
'''
import itertools

# use validation to check the user enter a digit or string
validation = True
while validation:
    # take input from user
    str = input("Enter numbers to check how many times consecutive occurrences of the character: ")
    try:
        # convert into list for iteration
        strList = list(str)
        for i,j in itertools.groupby(map(int,strList)):
            # now the value of list was store in 'i' by iteration and no of times occurrences is store in j as a object
            # so we convert object into list and then find its length
            no_of_times = len(list(j))
            print(tuple([no_of_times, i]) ,end = " ")
            validation = False
    except:
        print("Please enter integer")
