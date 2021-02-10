
# base=input("Ingrese la base en cm del rectángulo: ")
# altura=input("Ingrese la altura en cm del rectángulo :")
# area=int(base)*int(altura)
# print("El área del rectángulo es " + str(area) +" cm^2")

# def saludar():
#   print("Estamos dentro de la funcion ")
#   print("segunto print")
#   print("tercer print")

# saludar()

# def oferta(camisa,saco="koaj"):
#   print("la camisa que esta en promocion es de " + camisa+ "y saco " +saco)
# oferta("avengers","veles")

# articulo_especial="gorra";
# def crear_string(articulo_especial):
#   return "Nuestro articulo especial es "+ articulo_especial+"."

# print("no me gusta el articulo " + articulo_especial)
# print(crear_string("jeans"))
# print("no me gusta el articulo " + articulo_especial)

# # escribe la función suma acá
# def suma(num1,num2):
#   return num1+num2
# # código de prueba, verifica que aparezcan los valores correctos en la consola
# print(suma(1, 2)) # 3
# print(suma(0, 0)) # 0
# print(suma(245, 923)) # 1168

# # escribe la función hola acá
# def hola(nombre):
#   return f"Hola {nombre} !"
# # código de prueba
# print(hola("Pedro")) # "Hola Pedro!"
# print(hola("Juan")) # "Hola Juan!"
# print(hola("")) # "Hola !"

# escribe la función raiz_cuadrada acá
# def raiz_cuadrada(num):
#   return num**0.5
# # código de prueba
# print("Escriba un numero que quiera obtener la raiz cuadrada ")
# num_raiz=int(input())
# print(raiz_cuadrada(num_raiz))
# print(raiz_cuadrada(25)) # 5.0
# print(raiz_cuadrada(5476)) # 74.0
# print(raiz_cuadrada(2)) # 1.4142135623730951


# def propina(total,porentaje):
#   return total*(porentaje/100)

# num1=input("Digite el total de la compra ")
# num2=input("Digite el porcentaje de propina ")
# print(propina(int(num1),int(num2)))

# print(propina(100, 50)) # 50
# print(propina(200, 10)) # 20
# print(propina(5000, 90)) # 4500

# # escribe la función porcentaje_de_victorias acá
# def porcentaje_de_victorias(victorias,derrotas):
#   return (victorias*100)/(victorias + derrotas)

# # código de prueba

# print(porcentaje_de_victorias(5, 5)) # 50
# print(porcentaje_de_victorias(7, 0)) # 100
# print(porcentaje_de_victorias(6000, 4000)) # 60

# Dicen que un año en un humano es equivalente a 7 años de vida de los perros. Escribe una función llamada edad_perruna que reciba dos parámetros: nombre y edad. La función debe calcular la edad en años perrunos y retornar la siguiente cadena de texto (string): ", tienes en años perrunos!".

def edad_perruna(nombre,edad):
  edad*=7
  return f"{nombre} tienes en edad perruna {edad} años"
nombre=input("Ingrese su nombre: ")
edad=int(input("Dijite su edad: "))
print(str(edad_perruna(nombre,edad)))