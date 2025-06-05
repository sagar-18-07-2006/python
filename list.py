# l=[46,989684,66,6,66,42,644]
# m=list()
# print(type(m))

# print(type(l))
# # iterabklke
# for i in m:
#     print(i)
#     print ("hi")
# for i in l:
#     print(i)
# #acccsesing
# l1=[1,2,3,4,5,6,7,8,9,10]

# print(l1[0])
# print(l1[-1])
# print(l1[-(len(l1))])

# #mutubaility
# print(id(l1))
# l1[0]=22
# print(l1[0])
# print(id(l1))

# #list slicing
# print(len(l1))
# for i in l1[0:3]:
#     print (i)
# # inbuilt methods
# budget =[100,200,150,100]  #million dollar
# print(budget.count(100))
# print(budget.index(100))
# name1=["sagar","hardik","yashpalsinngh","darshita "]
# for i in  name1:
#     print(i)
# print()
# heart=name1.pop()
# for i in  name1:
#     print(i)
# print()
# print(heart)
budget =[100,200,150,100]  #million dollar
budget.sort()
for i in budget:
    print(i)
name=["dgb656,",244,True,False,174786,"ss"]
# # name.sort()
# # for i in name:
# #     print(i)  
# #it eill give typo error
name = ["dgb656,", 244, True, False, 174786, "ss"]

strings = sorted([x for x in name if isinstance(x, str)])
numbers = sorted([x for x in name if isinstance(x, (int, float, bool))])

# Combine or print separately
for i in strings + numbers:
    print(i)
    1
s=["sagar","radhe"]
s.insert(1,"ram")
for i in s:
    print(i)
s.append("darshita")
for i in s:
    print(i)
s.append(name)
for i in s:
    print(i)
print()
s.extend(name)
for i in s:
    print(i)



    l1=[1,2,3]
l2=[4,5,6]
l3=[7,8,9]
l =[l1,l2,l3]
for i in l:
    print(i)
#indexing
"""
for l1 it will be zero
for l2 it will be 1
for l3 it will be 2"""
print(l[0][0])
for i in l:
    for j in i:
        print(j)
    print()

q=[]
# i=0
for i in range(100):
    q.append(i)
    # i+=1
i=0
for i in q:
    print(i)
    i+=1

#list compherseion
s=[(i ** 100) for i in range (10)]
for i in s:
    print(i)
s=[(i ** 100) for i in range (10)]
for i in s:
    print(i)
