#Assignment 1) 3)
#sequence can be taken as input from user but it will be time taking so generating random sequence
#Since our job is to only check if there exist 2 numbers in the sequence whose product is odd we just need to check if 2 distinct odd numbers are there in the sequence

import random                                           


def odd_product(sequence=[]):                                       #While calling if user wants he can give sequence if not it will be generated    
    if sequence == []:
        n = random.randint(8,20)                               #randomly decide length of sequence to be taken since not mentioned
        sequence = list()
        for i in range(0,n):
            sequence.append(random.randint(0,100))              #randomly put values from 0 to 99 in the sequence
    print(sequence)
    c=0                                                     #counter for odd number appearances
    for i in sequence:
        if i%2==1:
            c=c+1
        if c>=2:
            return "2 such numbers found"
            break                                           #If already it has occured then to save computation time we will break from the loop
    if c<2:
        return "No such numbers found"        
inp = input("Enter a list of integers with spaces to check if 2 numbers with odd product exist or not, if not will test on randomly generated sequence")        #Take list input
seq = inp.split()                                                   #Input is in form of string, so we will split to form list                 
sequence=list()
for i in seq:                                                       #Entries of list seq are strings, we need integer entries to check so we will form new list "sequence" with in entries        
     sequence.append(int(i))
s = odd_product(sequence)                                           #If however sequence entered by user is empty will check on randomly generated sequence
print(s)    

