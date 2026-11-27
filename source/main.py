# source/main.py
from producto import Producto

p1= Producto(1,"producto 1", 50)
p2= Producto(2,"producto 2", 150)
p3= Producto(3,"producto 3", 20)
print(p1)
print(p2)
print(p3)

print (p3.calcular_total(5))

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b
