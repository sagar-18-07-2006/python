# class ClassSchedule:
#    def __init__(self, course, instructor):
#        self.course = course
#        self.instructor = instructor
  
#    def display_course(self):
#        print(f'Course: {self.course}, Instructor: {self.instructor}')
# sched = ClassSchedule('Chemistry', 'Mr. Doe') # initializing
 
# sched.display_course() # prints Course: Chemistry, Instructor: Mr. Doe
# sched.course # prints 'Chemistry
class ClassSchedule:
   def __init__(self, course, instructor):
       self.__course = course # private
       self.__instructor = instructor # private
 
   def display_course(self):
       # public
 
       print(f'Course: {self.__course}, Instructor: {self.__instructor}')
 
sched = ClassSchedule('Biology', 'Ms. Smith')

# the following will throw an Attribute Error because we're trying to access a private member
#sched.__course 
 

# this line won't throw an Attribute Error because this method is publi
sched.display_course() 