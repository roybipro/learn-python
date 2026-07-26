# class Factory:
#     a = 12
#     name = "kia" #private class Attributes 
#     def __init__(self,type,tyre,color):
#         self.type = type #Public object attribute
#         self.__tyre = tyre #private
#         self.color = color
        
#     def __detail(self): #private
#         print("hello")
        
# obj = Factory("Sedan","MRF","Black")

# obj.name ="Maruti"

# print(obj.__name)


class Hello:
   __a = 12
   
   
   @classmethod
   def info(cls):
       print(cls.__a)
       
obj = hello()

obj.info()