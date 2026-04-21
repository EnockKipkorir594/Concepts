'''Abstract class --> A class that can't be instantiated on its own;Meant to be subclassed
                    contain abstract methods, which are declared but have no implementation
                    Abstract classes benefits:
                    1.Prevents instantiation of the class itself
                    2.Requires subclasses to use inheritd abstract methods
                    '''
from abc import ABC, abstractmethod

class Vehicle(ABC):
    
    @abstractmethod
    def go(self):
        pass
    @abstractmethod
    def stop(self):
        pass

class Car(Vehicle):
    def go(self):
        print("ACCELERATE")
        
    def stop(self):
        print("STOP")
        
car = Car()
car.go()


'''Aggregation --> Represents a relationship where one object(the whole) '''
                
class Library:
    def __init__(self,name):
        self.name = name
        self.books = []

    def add_book(self, book):
        self.books.append(book)
    def display_books(self):
        return [f"{book.title} by {book.author}" for book in self.books]
    
        
class Book:
    def __init__(self,title,author):
        self.title = title 
        self.author = author 
        
lib = Library("One piece Library")
b1 = Book("Road to Kubernetes", "Justin Mitchell")
b2 = Book("Atomic habits", "Michael Carnigie")
b3 = Book("Be the man", "David Goggins")

lib.add_book(b1)
lib.add_book(b2)
lib.add_book(b3)

print(lib.display_books())


'''Composition --> the composed object directly owns its components, which cannot '''
                 
class Engine:
    def __init__(self, horse_power):
        self.horse_power = horse_power

class Wheel:
    def __init__(self,size):
        self.size = size

class Car:
    def __init__(self, make, model, horse_power, wheel_size):
        self.make = make 
        self.model = model 
        self.engine = Engine(horse_power)
        self.wheels = [Wheel(wheel_size) for wheel in range(4)]
        
    def display_car(self):
        return f"{self.make} {self.model} {self.engine.horse_power}HP {self.wheels[0].size}inches"

car0 = Car(make="BMW",model="G80 M3",horse_power=700,wheel_size=19)
print(car0.display_car())

'''Nested classes'''
class Company:
    class Employees:
        def __init__(self,name,position):
            self.name = name 
            self.position = position
            
        def get_details(self):
            return f"{self.name} {self.position}"
        
    def __init__(self,company_name):
        self.company_name = company_name
        self.employees = []
        
    def add_employee(self,name,position):
        new_emp = self.Employees(name,position)
        self.employees.append(new_emp)
        
    def list_employees(self):
        return [employee.get_details() for employee in self.employees]
    
comp = Company("Cloudspinx")
comp.add_employee('Pedro','Vice President')
comp.add_employee("Cisco", "Manager")
comp.add_employee("Kate", "Department head ")
comp.add_employee("Samantha", "Secretary")
print(comp.list_employees())


                 
    
    