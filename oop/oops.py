#imperative programming
# a = 12
# b = 13

# print(a + b)


#functional programming
# def add(a , b):
#     print(a+b)
    
# add(12, 13)
# add(100, 200)


#object oriented programming


# class
# class Car:
#     a = 12 # inside class variabe call attribute

#     def hello():    # functions inside class is call method
#         print("how are you")  
        

# #We can  access attributes and methodes after accessing the class    
# print(Car.a) #accessing attributes 

# Car.hello() #accessing methodes



# objects
# class Bags :
#     name = "Roys"
    
#     def details(self):
#         print("This is the company who create bags")     

# rebook = Bags()
# campus = Bags()

# print(rebook.name)
# print(campus.name)

# rebook.details()



#constructors
# class Bags:
#     def __init__(self,material,zips,pockets):  #self hold the location of object
#         self.material = material
#         self.zips = zips
#         self.pockets = pockets
        
    
    
# rebook = Bags("leather",3,2)
# campus = Bags("polyster",2,4)

# print(rebook.material)
# print(campus.material)



# Types of Attributes and methodes

class Animal:
    a = 12
    
    def __init__(self,name):
        self.name = name #object/instance attributes
    
    def hello(self): #object/instance method   capture the location of object
        print(f"Hello, How are you? My name is {self.name}")
        
    @classmethod    
    def details(cls):  #class method .  capture the location of class
        print(f"how are you my name is {cls.a}") 
        
    @staticmethod
    def speak(): #this is astatic method and it will not target any location
        print("Hello how are you I am a static mehod")
        
obj = Animal("lion")

obj.details()