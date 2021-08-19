
x = 85

if x < 60:
    print(f"60 is higher that {x}")
else:
    print(f"60 is less that {x}")

color = "rojo"

if color == "azul":
    print("el color es azul")
elif color == "rojo":
    print("el color es rojo")
else:
    print(f"el color es {color}")

name = "Emmanuel"
last_name = "Pereira"

a = input("digite su nombre : ")
b = input("digite su apellido : ")
if a == "Emmanuel":
    if b == "Pereira":
        print("usted es una perra hijueputa que no valora una monda")
    else:
        print("a bueno pa saber")
else:
    print("a bueno pa re saber")

y = input("digite el numero : ")
x = int(y)
if x > 2 and x < 10:
    print("el dato ingresado es un asco")
if x > 2 or x <= 20:
    print("ya esta un poquito mejor")
if(not(x == a)):
    print("bueno ya es aceptable")
