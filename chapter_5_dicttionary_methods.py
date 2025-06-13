# d={} empty dictionary
marks ={
    "harry" : 100,
    "sagar": 100,
    "darshita":100,
    "hardik" :100,
    "kartavya" : 14}
# print(marks.items())

# print(marks.keys())
# print(marks.values())
marks.update({"harry": 0})
print(marks)
print(marks.get("sagar"))
print(marks)
marks.pop("darshita")
print(marks)
print(len(marks))