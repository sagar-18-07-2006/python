print('''
s for snake 
g for gun 
w for water''')
computer =-1
you = (input("enter your option "))
youDict = {"s" : 1 ,"g" : 0,"w":-1}
youNum=youDict[you]
if computer==-1:
    if youNum==1:
        print(" you Won")
    if youNum==0:
        print(" you lost")
    if youNum==-1:
        print(" Draw")
if computer==0:
    if youNum==-1:
        print(" you Won")
    if youNum==1:
        print(" you lost")
    if youNum==0:
        print(" Draw")
if computer==1:
    if youNum==-1:
        print(" you Won")
    if youNum==0:
        print(" you lost")
    if youNum==1:
        print(" Draw")