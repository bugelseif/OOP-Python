from typing import List


def dobro(lista: List[int]) -> List[int]:
    for i in range(len(lista)):
        lista[i] = lista[i] * 2

    return lista


numeros = [1, 2, 3, 4]
resultado = dobro(numeros)


print(f"lista de numeros: tipo {type(numeros)} valor{numeros}")
print(f"resultado tipo {type(resultado)} valor {resultado}")
