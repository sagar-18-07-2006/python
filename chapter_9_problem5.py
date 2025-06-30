words = ["donkey","pagal","bawle"]
with open ("donkey.txt" ,"r") as f:
    content =f.read()
for i in words:
    content=content.replace(i,"*"*len(i))
print(content)
with open ("donkey.txt" ,"w") as f:
    f.write(content)