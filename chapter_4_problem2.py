marks =[]
for i in range (0,7):
    a=int(input(f"Enter marks of {i+1} student: "))
    marks.append(a)
marks.sort()
print (marks)
