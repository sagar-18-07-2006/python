#all triangles pattern

w=int(input("enter height"))
i=1
for i in range(1,w+1):
    j=0
    for j in range(0,i):
        print("*",end=' ')
        j+=1
    print()
    i+=1
w=int(input("enter height"))
i=1
for i in range(1,w+1):
    j=0
    for j in range(0,w-i+1):
        print(" ",end=' ')
        j+=1
    for j in range(0,i):
        print("*",end=' ')
        j+=1
    print()
    i+=1
m=int(input("enter height"))
i=1
for i in range(1,m+1):
    j=0
    k=0
    for j in range(1,i):
        print(" ",end=' ')
        j+=1
    for k in range(0,m+1-i):
        print("*",end=' ')
        k+=1
    print()
    i+=1
l=int(input("enter height"))
i=1
for i in range(1,l+1):
    j=0
    k=0
    for j in range(1,i):
        print(end=' ')
        j+=1
    for k in range(0,l+1-i):
        print("*",end=' ')
        k+=1
    print()
    i+=1
n=int(input("enter height"))
i=1
for i in range(1,n+1):
 
    k=0
 
    for k in range(0,n+1-i):
        print("*",end=' ')
        k+=1
    print()
    i+=1