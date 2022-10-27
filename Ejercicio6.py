def pares_impares(lista):
    pares = []
    impares = []

    for i in lista:
        if i%2 == 0:
            pares.append(i)
        else:
            impares.append(i)
    pares.sort()
    impares.sort()
    return pares, impares

