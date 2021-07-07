valoresInplace = [21, 78, 6, 4]
print(f"originais: {valoresInplace}")
valoresInplace.sort()
print(f"ordenados: {valoresInplace}")
valoresInplace.reverse()
print(f"reversa: {valoresInplace}")


valoresCopia = [45, 7, 20, 2]
novoValores = list(reversed(sorted(valoresCopia)))

print(f"original: {valoresCopia}")
print(f"copia: {novoValores}")

valoresHibrido = [1, 8, 24, 12]
novoHibrido = sorted(valoresHibrido)
novoHibrido.reverse()

print(f"original: {valoresHibrido}")
print(f"copia: {novoHibrido}")

