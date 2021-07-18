#Assignment 1) 5)

def arithmetical_ops(a,b,c):
    if a+b==c:
        out1 = " a+b=c is True "                            #Since more than one of the given operations maybe true, we will assign a variable output for each case and give output as concatnation of all
    else:
        out1 = ""                                                               
    if a-b==c:
        out2 =  " a-b=c is True "
    else:
        out2 = ""
    if a*b==c:
        out3 = " a*b=c is True "
    else:
        out3 = ""
    if out1+out2+out3 != "":                                #If any operation is true, the return will have its output as a part and will print it                                        
        return out1+out2+out3
    else:                                                   #If none of the operation is true, we will return that no operations are true
        return "None of the given arithmetical operations are True"    
    
a = int(input("Enter an integer a:"))                       #Taking inputs from user
b = int(input("Enter an integer b:"))
c = int(input("Enter an integer c:"))
out = arithmetical_ops(a,b,c)        
print(out)            
