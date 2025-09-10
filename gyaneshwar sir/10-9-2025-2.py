class vehicle:
    def __init__(self,milege,max_speed):
        self.max_speed=max_speed
        self.milege=milege
    def display(self):
        print(f"{self.milege} is the milege and have max speed of {self.max_speed}")
car=vehicle(16,160)
car.display()
        