#Assignment 1) 4)
#Since no string is given I will generate a random string of a random length

import string
import random

def vowel_counter(rand_str=""):                                                           #If string argument is given it will check for that string else generate string in next couple lines            
    if rand_str=="":
        n = random.randint(7,15)
        letters = string.ascii_letters
        rand_str = ''.join(random.choice(letters) for i in range(n))
    print(rand_str)
    count=0                                                                               #Setting counter variable to 0
    for letter in rand_str:
        if letter.upper() in {"A","E","I","O","U"}:
            count += 1
    return count        

rand_str = str(input("Enter a string to check vowel, if no input will test on randomly generated string"))      #To take specific string input from user to check for vowels
count = vowel_counter(rand_str)                                                                             
print("The number of vowels in the given string are :",count)            
