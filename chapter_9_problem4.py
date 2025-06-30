word = "donkey"
with open ("donkey.txt" ,"r") as f:
    content =f.read()
contentNew=content.replace("donkey","####")
print(contentNew)
with open ("donkey.txt" ,"w") as f:
    f.write(contentNew)