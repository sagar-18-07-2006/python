# class is bluepriint (placeholder) 
class Employee:
    name=""
    language ="py" #this is class attribute
    salary =120000#this is class attribute
    def __init__(self,a,b,c): #dunder method is called when object is created 
        print('i am creating object')
        self.name =a
        self.language=b
        self.salary=int(c)
    def getinfo(self):
        print(f"The language is {self.language}. The salary is {self.salary}")
    @staticmethod
    def greet():
        print("you are learning")
sagar =Employee("Sagar" ,"CPP",1024500)# This is an instance attribute
sagar.language ="CPP"
sagar.getinfo()
sagar.greet()
# sagar.getinfo() =Employee.getinfo(sagar)
print(sagar.language,sagar.salary)
