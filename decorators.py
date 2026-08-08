
def extragreeting(func):
    def wrapper():
        print("Hello from Bangladesh")
        func()
        
        print("Thank You Visit Again")
    return wrapper

@extragreeting
def greetings():
    print("Good morning")
    
greetings()



