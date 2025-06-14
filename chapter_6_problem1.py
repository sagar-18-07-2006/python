a=int(input("Enter 1st number: "))
b=int(input("Enter 2st number: "))
c=int(input("Enter 3st number: "))
d=int(input("Enter 4st number: "))

if(a>b and a>c and a>d):
    print(f"{a} is a greatest in {a} ,{b} ,{c} ,{d}")
elif(b>c and b>d):
    print(f"{b} is b greatest in {a} ,{b} ,{c} ,{d}")
elif(c>d):
    print(f"{c} is c greatest in {a} ,{b} ,{c} ,{d}")
else:
    print(f"{d} is d greatest in {a} ,{b} ,{c} ,{d}")