class Employee :
    name="default"
    salary=00000
    codingLanguage="c"
    def __init__(self,name ,salary,codingLanguage):
        self.codingLanguage=codingLanguage
        self.salary=salary
        self.name=name
    def getinfo(self):
        print(self.name)
        print(self.salary)
        print(self.codingLanguage)
em =[s:=Employee("Sagar",10000000,"cpp"),b:=Employee("bagar",1,"c")]
for i in em:
    i.getinfo()