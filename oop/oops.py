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
class Bags :
    name = "Roys"
    
    def details(self):
        print("This is the company who create bags")
        

rebook = Bags()
campus = Bags()

print(rebook.name)
print(campus.name)

rebook.details()