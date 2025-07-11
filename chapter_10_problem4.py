import random
class Train:
    def __init__(self,trainNo):
        self.trainNo =trainNo
    
    def book(self ,From,To):
        print(f"your ticket is booked in {self.trainNo} from {From} to {To}")
        # pass
    def getStatus(self):
        print(f"the train {self.trainNo} is running Succsesfully     ")
    def getFare(self,From,To):
        print(f"your ticket fare for {self.trainNo} from {From} to {To} is {random.randint(555,3999)}")
T = Train(12356)
T.getFare("jaipur","Raichur")
T.book("jaipur","Raichur")
T.getStatus()