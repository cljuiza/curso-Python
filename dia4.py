alturas =[1.9, 1.7, 1.5, 1.2, 1.3]
nombre=["leo", "lina", ""]
mix=[12,"juan",True]
print(mix)
print(alturas)

list_lista=[["ana",23],["juan",20],["andrea",23]]

##listas vacias
lista_vacia=[]

##llenar lista vacias o con valores 
##.append() solo puede agregar un elemento a la lista_vacia
print(lista_vacia)
lista_vacia.append(1) #solo puede agregar un valor
print(lista_vacia)

# 2. signo operador + para agregar mas elementos a la lista 
lista_vacia =lista_vacia + [2, 3, "ana"]
lista_vacia =lista_vacia + [4]
lista_con_valores=[5, 6, 7]
lista_vacia=lista_vacia+lista_con_valores
lista_vacia+=lista_con_valores
print(lista_vacia)

#indices de las listas
alturas =[1.9, 1.7, 1.5, 1.2, 1.3]
#posicion  0    1    2    3    4

#seleccion de un elemento basado en su indice
print(alturas[0])
#editar valor de lista #mutables
alturas[1]=2
print(alturas)
## Fuera de rango
#alturas[6]=6
print(alturas)
##ver si exite el elemento con in
print(1.9 in alturas)

if 1.9 in alturas:
  print("el valor esta en la lista")
else:
    print("el valor no esta en la lista")

print(len(alturas)) # saber la longitud de la lista

##inset() añadir un valor en la posicion deseada
alturas =[1.9, 1.7, 1.5, 1.2, 1.3]
print(alturas)
alturas.insert(2, 3)
alturas.insert(2, "altura") #primer elemento posicion, 2da el valor a cambiar
print(alturas)

#eliminar pop()
alturas.pop(0)
print(alturas)

#eliminar lista por compile
#del alturas 

#limpiar lista
alturas.clear()
print(alturas)

##
alturas =[1.9, 1.7, 1.5, 1.2, 1.3]
print(alturas[-1])
print(alturas[-3])

## Slicing list seleccionar trozos de items en lista
letras=['a', 'b', 'c', 'd', 'e', 'f', 'g']
##letras[inicio:fin]
#fin posicion +1
print(letras)
sub_lista=letras[1:6]
print(sub_lista)
print(letras[2:-1])
print(letras[:3])
print(letras[3:])
print(letras[-3:])
print(letras[:-3])

## Tipo de dato Range en Python es diferente a las listas pero se conbina
#bien con listas
mi_rango=range(10)#genera una lista iniciando desde 0 hasta el numero-1

print(type(mi_rango)) #type ver tipo de dato
#conversion de tipos de datos de range a list
mi_rango_list=list(mi_rango)
print(mi_rango_list)
print(len(mi_rango_list))

mi_rango2=range(2,10)#desde 2 hasta 9
mi_rango3=range(2,10,2)#desde 2 hasta 9 y salta de dos en dos
print(list(mi_rango3))

#
ejemplos=["azul","verde","rojo","amarillo"]
print(len(ejemplos))

for color in range(len(ejemplos)):
  print(color) #imprime sus indices 
  print(ejemplos[color])

#zip emparejar dos listas deben tener la misma cantidad de elemetos
alturas =[1.9, 1.7, 1.5, 1.2, 1.3]
nombres=["leo", "lina", "juan", "daniela","luz"]
print(list(zip(alturas, nombres)))






