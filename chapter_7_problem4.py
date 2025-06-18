n =int(input("Enter a number: "))
if (n>2):
     for i in range(2,n):
         if (n%i == 0):
           print(i)
           print("number is not a prime ")
           break