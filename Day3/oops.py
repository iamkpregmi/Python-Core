# #class and object
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def __str__(self):
#         return f"Hello {self.name} your age is {self.age}"
    

#     def __del__(self):
#         print('this is distructor')


# p1 = Person("krishna",23)
# print(p1)
# print(p1.name)
# print(p1.age)

# # del p1.name

# #Single Inheritance
# class Animal:
#     def __init__(self, name):
#         self.name = name

#     def speak(self):
#         return "Generic animal sound"
    

# class Dog(Animal):
#     def __init__(self, name, breed):
#         super().__init__(name)
#         self.breed = breed

#     def speak(self):
#         return f"{self.name} speak Woof!"


# # a1 = Animal('Tom')
# # print(a1.speak())

# bob = Dog('Bob', 'lebra')
# print(bob.speak())



# # Multiple inheritance
# class A:
#     def __init__(self):
#         print('this is the class A')

# class B:
#     def __init__(self):
#         print('this is the class B')


# class C(A,B):
#     def __init__(self):
#         print('this is the class C')
#         B.__init__(self) #Inherit B class
#         A.__init__(self) #Inherit A class


# myObj = C()


# #Polymorphism Example
# class Animal:
#     def speak(self):
#         return "Generic animal sound"
    
# class Dog(Animal):
#     def speak(self):
#         return "Woof!"
    
# class Cat(Animal):
#     def speak(self):
#         return "Meow!"
    

# def animal_sound(animal):
#     return animal.speak()


# dog = Dog()
# cat = Cat()

# print(animal_sound(dog))
# print(animal_sound(cat))


# # Implemented encapsulation
# class BankAccount:
#     def __init__(self,balance):
#         self.__balance = balance


#     def deposit(self, amount):
#         if amount > 0:
#             self.__balance += amount

    
#     def withdraw(self,amount):
#         if amount > 0 and amount <= self.__balance:
#             self.__balance -= amount
#         else:
#             print("Insufficient balance")
#             exit()
    
#     def get_balance(self):
#         return self.__balance
    

# account = BankAccount(1000)
# account.deposit(500)
# account.withdraw(1300)
# print(account.get_balance())



# # Abstraction Example
# from abc import ABC, abstractmethod
# import math as m
# class Shape(ABC):
#     @abstractmethod
#     def area(self):
#         pass

    
#     @abstractmethod
#     def perimeter(self):
#         pass



# class Circle(Shape):
#     def __init__(self, radius):
#         self.radius = radius

#     def area(self):
#         return m.pi * self.radius ** 2
    
#     def perimeter(self):
#         return 2 * m.pi * self.radius
    

# class Rectangle(Shape):
#     def __init__(self, length, width):
#         self.length = length
#         self.width = width
    
#     def area(self):
#         return self.length * self.width
    
#     def perimeter(self):
#         return 2 * (self.length * self.width)
    


# circle = Circle(5)
# rectangle = Rectangle(4,6)

# print(f"Circle Area: {circle.area():.2f}")
# print(f"Circle Perimeter: {circle.perimeter():.2f}")
# print(f"Rectange Perimeter: {rectangle.area()}")
# print(f"Rectange Perimeter: {rectangle.perimeter()}")



#Operator Overloading [Want to compare age]
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __gt__(self,other):
        return True if self.age > other.age else False


roger = Dog('Roger',8)
syd = Dog('Syd', 12)

print(roger > syd) #False