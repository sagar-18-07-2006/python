a = input("enter a string")
count = 0
for i in a:
    if(i == " "):
        count+=1

if count == 2:
    print(" it contain 2 white spaces")
else :
    print(" it dosen't contain exactly 2 white spaces")
# second way
if(a.count(" ")==2):
    print(" it contain 2 white spaces")
else :
    print(" it dosen't contain exactly 2 white spaces")
# does your string has double whitespace
a=a.replace("  "," ")
if(a.find("  ")!=-1):
    print("it contain double space")
else :
    print("it does not contain double space")
#replace double spaces in a with 3spaces
