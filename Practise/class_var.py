#! Python3

#import random

#class Hat_Sort():

 #   houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]

  #  @classmethod
   # def Sort(cls, name):
    #    print(f"{name} is in {random.choice(cls.houses)}.")

#Hat_Sort.Sort("Harry")

#! Python3 
#Object Oriented Programming

class Student:

    #self corresponds to the current object that has been created.
    def __init__(self, name, house, patronus):
        #Here we adding instance variables to the objects.
        self.name = name
        self.house = house #It will also call the setter method
        self.patronus = patronus

    #Specaial method inside a class which python calls automatically 
    def __str__(self):
        return f"{self.name} is from {self.house}. \nExpecto Patronum! {self.patronus}."
    
    @classmethod
    def get(cls):
        name = input("What's your name?  ")
        house = input("What's your house?  ")
        patronus = input("What's your patronus? ")
        return cls(name, house, patronus)
 

def main():
    student = Student.get()
    print(student) 
    
if __name__ == "__main__":
    main()

