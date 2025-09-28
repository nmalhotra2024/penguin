#activity 1
class Vehicle:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage
        
class Bus(Vehicle):
    pass

School_bus = Bus("School Volvo", 180, 12)
print("Vehicle Name:", School_bus.name, "Speed:", 
School_bus.max_speed, "Mileage:", School_bus.mileage)

#activity 2  
class Person(object):
    
    def __init__(self, name, idnumber):
        self.name = name
        self.idnumber = idnumber
    def display(self):
        print(self.name)
        print(self.idnumber)  
        
class Employee(Person):
    def __init__(self, name, idnumber, salary, post):
        self.salary = salary
        self.post = post
        
        Person.__init__(self, name, idnumber)
        
a = Employee('Rahul', 886012, 200000, "Intern")

a.display()

#activity 3

class Bird:
    
    def __init__(self):
        print("Bird is ready")
        
    def whoisThis(self):
        print("Bird")
        
    def swim(self):
        print("swim faster")
        
class Penguin(Bird):
    
    def __init__(self):
        super().__init__()
        print("Penguin is ready")
        
    def whoisThis(self):
        print("penguin")
        
    def run(self):
        print("Run faster")
        
peggy = Penguin()
peggy.whoisThis()
peggy.swim()
peggy.run()
        