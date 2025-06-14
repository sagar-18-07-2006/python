            #   if elif ladder 
    
a=int(input("Enter your age: "))
if(a>18):
    print("you are above age of consent")# it will work if if condition is true it will work and rest is ignore otherwise 
elif (a>0): # it will be checked if if false  if true remaining ignorrre 
    print("you are not above age of consent")
else:
    print("age cannot be negitive or zero")
    
if(a>=18):
    print ("yes")