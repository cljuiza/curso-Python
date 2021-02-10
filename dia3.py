# def gracias(donacion):
#   if donacion>=10000 and donacion<=50000:
#     print("Gracias, por danar 10mil")
#   elif donacion>=5000:
#     print("gracias por donar 5mil")
#   elif donacion>=1000:
#     print("gracias por donar mil")
#   else:
#     print("gracias por no donar")

# gracias(0)

# Escribe una función llamada en_rango que reciba tres parámetros: num, inferior, superior. La función debe retornar True si num es mayor o igual a inferior y menor a superior. De lo contrario debe retornar False.

# escribe la función en_rango acá
def en_rango(num,inferior,superior):
  if num>=inferior and num<superior:
    return True
  else:
    return False
# código de prueba
print(en_rango(5, 1, 10)) # True
print(en_rango(5, 6, 10)) # False
print(en_rango(1, 1, 10)) # True
print(en_rango(10, 1, 10)) # False

# Escribe una función llamada calificar_pelicula que reciba un parámetro rating (un número). Si el rating es menor a o igual a 5 la función debe retornar la cadena "Terrible!". Si el rating está entre 5 y 9 debe retornar la cadena "Interesante". Si el rating es 9 o más debe retornar la cadena "Increíble!".

# escribe la función calificar_pelicula acá
def calificar_pelicula(rating):
  if rating<=5:
    return "Terrible!"
  elif rating>5 and rating<9:
    return"Interesante"
  else:
    return"Increíble!"

# código de prueba
print(calificar_pelicula(5)) # "Terrible!"
print(calificar_pelicula(8)) # "Interesante"
print(calificar_pelicula(9)) # "Increíble!"

# Escribe una función llamada mas_del_doble que reciba dos parámetros: num1 y num2. La función debe retornar True si num1 es más del doble de num2. De lo contrario debe retornar False.

# escribe la función mas_del_doble acá
def mas_del_doble(num1,num2):
  doble_num2=2*num2
  if num1>doble_num2:
    return True
  else:
    return False
# código de prueba
print(mas_del_doble(11, 5)) # True
print(mas_del_doble(5, 10)) # False

# Escribe una función llamada gran_exponente que reciba dos parámetros: base y exponente. Si base elevado a exponente es más de 5000 debe retornar True. De lo contrario debe retornar False.

# escribe la función gran_exponente acá
def gran_exponente(base,exponente):
  if base**exponente>5000:
    return True
  else:
    return False
# código de prueba
print(gran_exponente(2, 8)) # False
print(gran_exponente(5, 1000)) # False
print(gran_exponente(6, 900)) # True

# Escribe una función llamada divisible_por_10 que reciba un parámetro num que retorne True si num es divisible por 10 y False de lo contrario.

# escribe la función divisible_por_10 acá
def divisible_por_10(num):
  if num%10==0: return True
  else: return False
# código de prueba
print(divisible_por_10(100)) # True
print(divisible_por_10(1980)) # True
print(divisible_por_10(38)) # False

# Escribe una función llamada bing_bong que reciba un número como parámetro:

# Si el número es múltiplo de 3 debe retornar "bing".
# Si el número es múltiplo de 5 debe retornar "bong".
# Si el número es múltiplo tanto de 3 como de 5 debe retornar "bingbong".
# Si no cumple ninguna de las condiciones anteriores debe retornar el mismo número.
# escribe la función bing_bong acá
def bing_bong(num):
  if num%3==0 and num%5==0: return "bingbong"
  elif num%3==0: return "bing"
  elif num%5==0: return "bong"
  else: return num
# código de prueba
print(bing_bong(3)) # "bing"
print(bing_bong(5)) # "bong"
print(bing_bong(30)) # "bingbong"
print(bing_bong(8)) # 8