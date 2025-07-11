class calculator:
    n=0
    def __init__(self,N):
        self.n=N
    def squareOfN(self,n=0):
        return self.n**2
    def CubeOfN(self,n=0):
        return self.n**3
    def squareRootN(self,n=0):
        return self.n**(1/2)
    @staticmethod
    def greet(a="user"):
        print(f"hello {a}!!!")

number = calculator(10)
print(f"{number.CubeOfN()} {number.squareRootN()} {number.squareOfN()}")
number.greet("Welcome")