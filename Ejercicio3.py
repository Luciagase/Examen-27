#Realiza un programa llamado multiplicador.py que cumpla el siguiente algoritmo utilizando siempre que sea posible operadores en asignación:

#Guarda en una variable numero_magico el valor 12345679 (sin el 8)
#Lee por pantalla otro numero_usuario, especifica que sea entre 1 y 9
#Multiplica el numero_usuario por 9 en sí mismo
#Multiplica el numero_magico por el numero_usuario en sí mismo
#Finalmente muestra el valor final del numero_magico por pantalla

numero_magico = 12345679

def operacion(numero_magico):
  numero_usuario = int(input('Escribe un número entre 1 y 9: '))
  numero_usuario*= 9
  numero_magico*= numero_usuario
  return numero_magico

print(operacion(numero_magico))