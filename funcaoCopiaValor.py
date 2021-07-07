from typing import List


def dobro(lista: List[int]) -> List[int]:
    numerosDobrados = []
    for i in range(len(lista)):
        numerosDobrados.append(lista[i] * 2)

    return numerosDobrados


numeros = [1, 2, 3, 4]
numeros = dobro(numeros)
resultado = dobro(numeros)

print(f"Numeros - valor {numeros}, tipo {type(numeros)}")
print(f"Dobro - valor {resultado}, tipo {type(resultado)}")
