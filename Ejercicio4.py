
#Elimina el último elemento de la lista modificada en el paso anterior.
#Crea una nueva lista con la repetición de los elemento de la lista guardada en el paso anterior.
import sys
lista=['string', 1, 3.14, 3>1]

def salto(lista):
  lista_final=[]
  lista_alreves=lista[::-1]
  lista_final.append(lista_alreves[0])
  lista_final.append(lista_alreves[2])
  return lista_final
  
print(salto(lista))

def eliminar():
  lista1=salto(lista)
  lista1.remove[1]
  return lista1

print(eliminar())

  
      
      



