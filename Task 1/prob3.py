"""
You and Fredrick are good friends. Yesterday, Fredrick received  credit cards from ABCD Bank.
He wants to verify whether his credit card numbers are valid or not. You happen to be great at regex so
he is asking for your help!

A valid credit card from ABCD Bank has the following characteristics:

► It must start with a ,  or .
► It must contain exactly  digits.
► It must only consist of digits (-).
► It may have digits in groups of , separated by one hyphen "-".
► It must NOT use any other separator like ' ' , '_', etc.
► It must NOT have  or more consecutive repeated digits.

"""

import re
TESTER = re.compile(
    r"^"
    r"(?!.*(\d)(-?\1){3})"
    r"[456]"
    r"\d{3}"
    r"(?:-?\d{4}){3}"
    r"$")
 # take input from user
cards = int(input("How many cards you have?\n"))
for i in range(cards):
    # take input from user about credit card number
    creditCardNumber = input(f"Enter Credit Card {i+1} number: ")
    # checking
    if TESTER.search(creditCardNumber):
        print("Valid")
    else:
        print("Invalid")
