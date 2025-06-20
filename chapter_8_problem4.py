def star_triangle_up_to_down(n):
    a=int(n)
    if(n==1):
       print("*")
    if(n>1):
        for i in range(0,n):
            print("*",sep="",end="")
        print()
        star_triangle_up_to_down(n-1)
star_triangle_up_to_down(3)