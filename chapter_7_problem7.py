n=int(input("Enter the number: "))
for i in range(1,n+1):
    if(i==1 or i==n):
        for i in range(1,n+1):
            print("*",end=" ")
    else :
        
             for i in range(1,n+1):
                 if(i!=1 and i!=n):
                    print(" ",end=" ")
                 else:
                     print("*",end=" ")
            
    print()    