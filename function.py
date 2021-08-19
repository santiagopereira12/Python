
def hola(name = "People."):
    print("hola " + name)

hola("Santiago")
hola("Cristian")
hola("Arturo")
hola()

def add(numberOne, numberTwo):
    return numberOne + numberTwo

print(add(50, 90))
print(add(60, 84))

edd = lambda numeroUno, numeroDos: numeroUno + numeroDos
print(edd(84, 97))