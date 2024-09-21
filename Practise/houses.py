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
    
    @property 
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if not name:
            raise ValueError("Missing Name")
        self._name = name
        
    #getter
    @property
    def house(self):
        return self._house
    
    @house.setter
    def house(self, house):
        if house not in ["Gryffindor", "Slytherin", "Hufflepuff", "Ravenclaw"]:
            raise ValueError("Invalid House")
        self._house = house
 

def main():
    student = get_student()
    print(student)

       
def get_student():
    name = input("What's your name?  ")
    house = input("What's your house?  ")
    patronus = input("What's your patronus? ")
    return Student(name, house, patronus) #An object is created and the value is initialised when python calls the __init__().
    
    
if __name__ == "__main__":
    main()


#An object is created or an instance of the class is created when Student(name, house) is executed.
#Objects are the members of the class which gives it some characteristcs. Name and house are the attributes of the class.
