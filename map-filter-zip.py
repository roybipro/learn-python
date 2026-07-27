# a = ["Bipro","Dipto","Rifat","Sakib"]

# lengths = map(len, a)
# print(list(lengths))

temp_cel = [0, 10, 20, 34.5]

# def converter(a):
#     farenheit =(9/5)*a + 32
#     return farenheit


print(list(map(lambda x : (9/5)*x + 32, temp_cel)))

# print(list(map(converter, temp_cel)))