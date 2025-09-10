# Creating a set
my_set = {1, 2, 3, 4, 5}
print(my_set)   # {1, 2, 3, 4, 5}

# Using set() constructor
another_set = set([1, 2, 2, 3, 4])
print(another_set)   # {1, 2, 3, 4}

# Empty set
empty_set = set()
print(type(empty_set))   # <class 'set'>
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

# Union
print(A | B)     # {1, 2, 3, 4, 5, 6}
print(A.union(B))  

# Intersection
print(A & B)     # {3, 4}
print(A.intersection(B))

# Difference
print(A - B)     # {1, 2}
print(B - A)     # {5, 6}

# Symmetric Difference
print(A ^ B)     # {1, 2, 5, 6} (A-b) U (B-A)
print(A.symmetric_difference(B))
s = {1, 2, 3}

s.add(4)                  # Add element
print(s)                  # {1, 2, 3, 4}

s.update([5, 6])          # Add multiple elements
print(s)                  # {1, 2, 3, 4, 5, 6}

s.remove(3)               # Remove element (error if not found)
s.discard(10)             # Remove element (no error if not found)
print(s)                  # {1, 2, 4, 5, 6}

s.pop()                   # Removes random element
print(s)

s.clear()                 # Empty the set
print(s)                  # set()

frozen = frozenset([1, 2, 3, 4])
print(frozen)          # frozenset({1, 2, 3, 4})
# frozen.add(5)        # ❌ Error (cannot add to frozenset)
    

students = {"Alice", "Bob", "Charlie"}
new_students = {"David", "Alice", "Eve"}

# Union
print("All students:", students | new_students)

# Intersection
print("Common students:", students & new_students)

# Difference
print("Only old students:", students - new_students)

