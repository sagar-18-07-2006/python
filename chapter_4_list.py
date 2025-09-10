friends =["apple","orange",True,2,2.36,False ,"sagar","hardik"]
print(friends[0])
# print(friends[0][0])
friends[0]="grapes"
print(friends[0])
#list slicing
# same as string
#methods
friends.append("sagarrr")
print(friends[len(friends)-1])
l1=[1,2,3,8,9,10,4,5,6,7]
l1.sort()
for i in l1:
    print (i)
l1.reverse()
for i in l1:
    print (i)
l1.pop()
print(l1) 
value = l1.pop(3 )
print(l1)  
print(value)
l1.remove(8)
print(value)
l1.remove(989)
print(value)