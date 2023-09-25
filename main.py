# Тестовый файл


from random import randrange
from test import power

# f = open("temp.txt", "w")
# f.write("hello")
# f.close()

f = open('temp.txt', "r")
print(f.read())
f.close()

x: object = power(2, 2)
print(x)

y = randrange(1, 100)
print(y)
