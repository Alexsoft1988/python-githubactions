# source/main.py
import sys
from pathlib import Path

# Agrega la carpeta padre (la raíz) a las rutas de búsqueda de Python
sys.path.append(str(Path(__file__).resolve().parent.parent))

from producto import Producto

p1= Producto(1,"producto 1", 50)
p2= Producto(2,"producto 2", 150)
p3= Producto(3,"producto 3", 20)
print(p1)
print(p2)
print(p3)

print (p3.calcular_total(5))

def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b
