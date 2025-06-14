p1="Make a lot of Money"
p2 ="buy now"
p3 ="Subscribr this"
p4 ="click this"
message =input("enter your message")
if(p1 in message)or (p2 in message) or (p3 in message) or (p4 in message):
    print("It is a Spam ")
else:
    print("it is not a spam")