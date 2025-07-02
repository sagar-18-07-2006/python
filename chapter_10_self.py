# class is bluepriint (placeholder) 
class Employee:
    
    language ="py" #this is class attribute
    salary =120000#this is class attribute
    def getinfo(self):
        print(f"The language is {self.language}. The salary is {self.salary}")
    @staticmethod
    def greet():
        print("you are learning")
sagar =Employee()# This is an instance attribute
sagar.language ="CPP"
sagar.getinfo()
sagar.greet()
# sagar.getinfo() =Employee.getinfo(sagar)
print(sagar.language,sagar.salary)
