from typing import List


def dobro(lista: List[int]) -> None:
    for i in range(len(lista)):
        lista[i] = 2 * lista[i]


entrada = [1, 2, 3, 4]
resultado = dobro(entrada)

print(f"lista de numeros: tipo {type(entrada)} valor{entrada}")
print(f"resultado tipo {type(resultado)} valor {resultado}")
