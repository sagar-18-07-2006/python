def factorial(n):
    n=int(n)
    if(n<0):
        print("factorial of 0 or >0 exist")
    elif(n==0):
        return 1
    else:
        return n*factorial(n-1)
def main():
    l=input("enter an number: ")
    print(factorial(l))
if __name__ == "__main__":
    main()