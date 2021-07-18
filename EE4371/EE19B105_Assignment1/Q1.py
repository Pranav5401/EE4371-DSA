#Assignment 1) 1a) 

def sum_squares():
    n = int(input("Enter the positive integer n for sum of squares < n"))           #Take input 
    s=0
    for i in range(0,n):
        s += i*i                                        #for loop to add all squares till n
    return s    

a1 = sum_squares()
print("The sum of squares till n is ",a1)              


#Assignment 1) 1b)
    
def sum_odd_squares():
    n = int(input("Enter the positive integer n for sum of odd squares < n"))       #Take input
    s=0
    for i in range(1,n,2):
        s += i*i                                        #for loop to add odd squares till n
    return s       

a2 = sum_odd_squares()
print("The sum of odd squares till n is ",a2)          



                                    
    
            
