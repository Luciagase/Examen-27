#*Realiza una función llamda funcion3 para pedir al usuario que introduzca su edad, y después imprimir en la pantalla si es meyor de edad o no

var_1 = "Módulo 1 de Python "

print(var_1.lower())
print(var_1.upper())

print('La longitud de la variable es',len(var_1))
division=len(var_1)/7
print(round(division,4))

def funcion1():
  operacion = 12 - (4 * 2) - (2 + 2)
  return operacion

print(funcion1())

def funcion2():
  operacion = 12 - 4 * (2 - 2) + 2
  return operacion

print(funcion2())

def funcion3():
  edad=int(input('Introduce tu edad: '))
  if 0 < edad < 18:
    return 'Eres menor de edad'
  elif edad >=18:
    return 'Eres mayor de edad'
  else:
    return 'No es válido'

print(funcion3())