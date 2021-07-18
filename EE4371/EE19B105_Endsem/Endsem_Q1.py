#Endsem Qs 1)
#Birthday Problem : Probability that 2 birthdays coincide for randomly chosen n people
#Probability for n people is 1 - (365 permute n divided by 365^n) using complementation 
#method for finding probability since 365 permute n divided by 365^n is probability for all distinct birthdays

import random

def recursive(n):                                   #Recursion for 365 permutate n divided by 365^n
    if n==1:
        return 1
    else:
        return ((366-n)/365)*recursive(n-1)
    
def theoretical_probability(n):                     #Theoretical probability that 2 birthdays coincide                
    return 1-recursive(n)   

def experimental_probability(n,max_iter):    
    
    s=0                                             #Expermintal probability variable       
    c=0                                             #Count variable        
    for x in range(max_iter): 	   #Running the experiment 'iteration' number of times
        date_count = {}            #Initalsing a empty dictionary for storing dates as key and the number of people having birthday as that date as value
        for y in range(n): 	       #Calculating birthday for each person
            rand_num = random.randint(1,365) 	#Creating a random birthday
            if rand_num in date_count:      #If new date is in the dictionary, increase count by 1 and break
                c += 1
                break
            else: 						        #Else add the date in the dictionary with key = date and value = 1 which signifies that the date is in the dictionary
                date_count[rand_num]=1
	
    s+=c                                            #sum of c's for each trial     
    p=s/max_iter                                              #Experimental probability is sum of trials divided by number of trials                                                         
    return p

file = open("Bday_100000.txt","w")
max_iter = 10000
for x in range(5,201,5): 	#Iterating the values of n
    file.write("%d %lf\n"%(x,(float(experimental_probability(x,max_iter))-float(theoretical_probability(x))))) 
    #writing theoritical and experimental probability for each n to the file "Bday_100000.txt"
    #will plot the data in this file by setting max_iter to 100 first then to 10000 
    #Have attached both the plots in the document which is : [experimental_probability(n,max_iter)-theoretical_probability(n)] vs n for each n
