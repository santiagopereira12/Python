
myString = "hola mundo"

# print(dir(myString))

print(myString.upper()) #mayusculas
print(myString.lower()) #minusculas
print(myString.swapcase()) #mayus
print(myString.capitalize()) #coloca la letra inicial en mayuscula
print(myString.replace('hola', 'adios').upper()) #remplaza la palabra seleccionada por la dada
print(myString.count('o')) #cuenta cuantos caracteres posee
print(myString.startswith("perra")) #verifica el inicio del texto
print(myString.endswith('mundo')) #verifica el final del texto
print(myString.split()) #separa en caracteres
print(myString.find('u')) #cuenta la posicion del caracter especificados
print(len(myString)) #muestra la cantidad de caracteres
print(myString.index('a')) #muestra el indice del valor
print(myString.isnumeric()) #muestra si la variable es numerica
print(myString.isalpha()) #muestra si la variable es alfa numerica
print(myString[5]) #imprime en caracter de la ubicación dada

#concatenacion
print("the program is " + myString)
print(f"the program is {myString}")
print("the program is {0}".format(myString))

#mi propia prueba personal
a = "abcd abcdef abcdefgh efgh"

print(a)
print(a.count('abcd'))
print(a.count('efgh'))
print(a.startswith("prueba"))
print(a.swapcase())
print(a.split())
