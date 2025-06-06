def square(n):
  
   return n**2
def main():
    a=int(input("enter a number"))
    print(square(a))
    print((lambda x : x**2)(a))
if __name__ == "__main__":
    main()