a=int(input("enter a number         "))
b=int(input("enter a number         "))
if(a>b):
    temp=a
    a=b
    b=temp
while(a<=b):
    if(a%2==0):
        print(a ," is even ")
    a+=1
