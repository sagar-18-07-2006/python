found = False

with open("python.txt", "r") as f:
    for i, line in enumerate(f, start=1):
        if "python" in line.lower():
            print(f"'python' is in line {i}")
            found = True

if not found:
    print("python is not present")
