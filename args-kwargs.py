# def addition(*args):
#     s = 0
#     for i in args:
#         s = s+i
#     return s
# print(addition(12,33,11))

# def info(**kwargs):
#     return kwargs

# print(info(name = "Bipro",age = 24, profession = "AI Eng"))


def extragreeting(func):
    def wrapper(*args,**kwargs):
        print("Hello from Bangladesh")
        func(*args,**kwargs)
        
        print("Thank You Visit Again")
    return wrapper

@extragreeting
def addition(a,b,c):
    print(a+b+c)

addition(12,12,12)