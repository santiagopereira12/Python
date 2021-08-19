
beta_list = [4, 'hola', True, [7, 8, 9]]

color = ['amarillo', 'azul', 'rojo', 'negro', 'negro']

number_list = list((1, 2, 3, 4, 5))

print(number_list)
print(type(number_list))

b = list(range(1, 51))
print(b)
print(len(beta_list))
print(color[2])
print('azul' in color)
print(color)
color[0] = 'negro'
print(color)

color.append('blanco') #agrega una nueva descripcion a la lista 
print(color)
color.extend(['gris', 'morado'])
print(color)
color.insert(4,  'rosado')
print(color)
# color.pop() #elimina el ultimo valor de la lista
# print(color)
# color.remove('rojo') #elimina el valor ingresado de la lista
# print(color)
# color.pop(3) #elimina segun el indice indicado
# print(color)
# color.clear() #limpia la lista dejandoja sin elementos guardadoss
# print(color)
color.sort() #ordena la lista alfabeticamente
print(color)
color.sort(reverse=True) #ordena la lista en forma reversiva
print(color)
print(color.index('negro'))
print(color.count('negro'))
