#ciclps python
razas=["beagle","golden","bulldog","labrador","pug"]
# for<variable temporal> in <lista>:

for i in razas:
  print(i);

print(list(range(9)))

# rango de veces que se repetira
for i in range(3):
  print("Warning!")

mis_numeros=[4,3,5,6,2,4,5,3]
# agregar valor
# mis_numeros.append(1)
# for number in mis_numeros:
#   print(mis_numeros.append(1))

#break
razas=["beagle","golden","bulldog","labrador","pug"]
for i in razas:
  if i=="bulldog":
    print("se encontro el bulldog")
    break
  print(i)

## continue
lista_numeros=[1,-2,3,-4,5,-6,7]
for i in lista_numeros:
  if i<0:
    continue
  print(i)

# indices
for i in range(len(lista_numeros)):
  print("indices",i)

##ciclos concatenados o nesteados(nested)
equipos=[["Laura","Lina"],["Angie","Helen"],["Lady","Maria"]]
for equipo in equipos:
  for i in equipo:
    print(i)

print("--------------")
##ciclo while se utiliza cuando hay un condicional hasta cuando se busca que itere
razas=["beagle","golden","bulldog","labrador","pug"]

#inicializador en 0
inicializador=0
while inicializador<len(razas):
  print(razas[inicializador])
  inicializador+=1

n=10
sum=10
i=1
while i<=n:
  sum+=i
  print("contador",i)
  print("sumatoria",sum)
  i+=1

##list comprehensions (compresiones de listas)
##ciclo for dentro de una lista, para obtener como resultado otra lista
razas=["beagle","golden","bulldog","labrador","pug"]

bulldog=[]
for raza in razas:
  if raza=="bulldog":
    bulldog.append("bulldog "*3)
print(bulldog)
#beagles=["bulldog","bulldog","bulldog"]

##list comprehensions mas abreviado de lo anterior
beagles=[raza for raza in razas if raza=="pug"]
print(beagles)

#2 ejemplo
palabras=["@ana","@no-filter","@diego","#fff","@dfmp"]
usernames=[u for u in palabras if u[0]=="@"]
print(usernames)

#3 ejemplo
mensajes=[usuario+"por favor sigueme!" for usuario in usernames]
print(mensajes)

#4ejemplo
mis_votos=[23,45,25,1,17,24]
votos_actualizados=[voto+10 for voto in mis_votos]
print(votos_actualizados)