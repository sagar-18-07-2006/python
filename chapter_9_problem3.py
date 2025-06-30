def multiplytable(n):
   
    with open(f"tabels/maths_table_{n}.txt","a") as f:
        f.write((f"Table of {n} ==>"))
        for i in range (1,11):
            f.write(f"\n{n} X {i} ={n*i}\n")
    print("")
for i in range(2,21):
    multiplytable(i)