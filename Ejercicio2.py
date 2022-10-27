cadena = "zeréP nauJ,01"

def nombre_nota(cadena):
  ordenar=cadena[::-1].split(',')
  return ordenar[1]+' ha sacado un '+ ordenar[0]+' de nota'

print(nombre_nota(cadena))