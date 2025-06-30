with open("python.txt","r") as f :
    if ("python" in f.read().lower()):
        print(" Python is in this file")
    else:
        print(" Python is not in this file")
        