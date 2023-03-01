lenguajes = ['Python', 'kotlin','Java','Javascrip']
print(lenguajes)

#los array (list) comienzan en la posicion 0
print(lenguajes[0])

#ordenar los elementos
lenguajes.sort()
print(lenguajes)

#ordenar los elementos
lenguajes.sort()
print(lenguajes)

#acceder a un elenmento dentro de un texto
aprendiendo = f'Estoy aprendiendo {lenguajes[3]}'
print(aprendiendo)

#modificando valores de un arreglo
lenguajes[2] = 'PHP'
print(lenguajes)

#agregar elementos a un arreglo (list)
lenguajes.append('Ruby')
print(lenguajes)

#Eliminar de un arreglo (list)
del lenguajes[1]
print(lenguajes)

#eliminar con pop una posicion en especifico
lenguajes.pop(0)
print(lenguajes)

#eleminar por nombre
lenguajes.remover('PHP')
print(lenguajes)
