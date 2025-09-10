a = [1, 2, 3]
b = a         # b refers to the same object as a
c = [1, 2, 3] # c is a new object with the same values

print(a == b)   # True  (values are equal)
print(a  is b)   # True  (same object in memory)

print(a == c)   # True  (values are equal)
print(a is c)   # False (different objects in memory)
print(a is a)
b.pop()
print(a  is b)   # True  (same object in memory)
print(b)
print(a)