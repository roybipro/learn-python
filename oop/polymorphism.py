# class Animal:
#     def speak(self):
#         print("Animal Dont speak")
        
        
# class Humans:
#     def speak(self):
#         print("Humans can speak")
        
        
# obj = Animal()
# obj2 = Humans()

# obj.speak()
# obj2.speak()


# Method overriding (we need inheritance)

# class Animal:
    
#     a = 12
#     def __init__(self,name):
#         self.name = name
        
#     def details(self):
#         print(f"Your Name is {self.name}")
        
        
# class Humans(Animal):
    
#     b =13
#     def __init__(self, name,id):
#         super().__init__(name)
#         self.id = id
        
#     def details(self):
#         super().details()
#         print(f"Your Name is {self.name} your id is {self.id}")
        

# obj = Humans("Dube", 1)
# obj2 = Animal("Bipro")

# print(obj.a)
# obj2.details()
# obj.details()

# when we doing inheritance and parent and chaild class 
#have same method name so the child class method wll override your parent class method


##method overloading
class Hello:
    def speak(self,a):
        print("Hello from Hello class")
    
    def speak(self,a,b):
        print("Hello from Hello class with two arguments")
