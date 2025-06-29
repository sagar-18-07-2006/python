with open ("poem.txt", "r") as f:
    poem = f.read()
    if "Twinkle, twinkle, little star" in poem:
        print("it is Twinkle twinkle poem.")