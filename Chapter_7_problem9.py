n=int(input("Enter siae of triangle: "))
for i in range(n):
    j=n-i-1
    while j>0:
        print(end=" ")
        j-=1
        

    for i in range (((i)*2)+1):
        print("*",end="")
    print()