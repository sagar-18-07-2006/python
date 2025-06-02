a=int(input("enter a number         "))
b=int(input("enter a number         "))
if(a>b):
    temp=a
    a=b
    b=temp
sum=0
while(a<=b):
    sum+=a
    a+=1
print(sum)