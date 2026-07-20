# class Animal:  # parent class
#     a = 2
#     def __init__(self,name):
#         self.name = name
        
#     def details(self):
#         print("An animal is a multicellular, eukaryotic organism that belongs to the biological kingdom Animalia")

# class Humans(Animal):  #Child class
#     pass

# obj = Animal("Lion")
# obj2 = Humans("John")
# obj2.details()

# your child object has all the powers to access the attributes and methodes of parent calss

class BagFactory:
    def __init__ (self,material,zips,pockets):
        self.material = material
        self.zips = zips
        self.pockets = pockets
    
    def details(self):
        print("Your bag details are")
        print(self.material)
        print(self.zips)
        print(self.pockets)
        
class Reebok(BagFactory):
    def __init__(self, material, zips, pockets,color):
        super().__init__(material, zips, pockets)
        self.color = color
    
    def details(self):
        print(self.color)
        return super().details()
      
        
urbanland = BagFactory("Lather",3,4)

bag2 = Reebok("Polyster",3,3)