class check:
    def oddeven(self,value1):
        if(value1%2==0):
            print(f"{value1} is even")
        else:
            print(f"{value1} is odd")
a=check()
b=int(input("Enter the integer to check the even odd: "))
a.oddeven(b)
print(dir(check))
