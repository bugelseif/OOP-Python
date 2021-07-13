from Pessoa import Pessoa

p1 = Pessoa('Bruna', 'Ferreira', 30)
p2 = Pessoa('Camila', 'Lira', 20)

print(p1.nomeCompleto())

p1.trocarSobrenome('Elseif')
print(p1.nomeCompleto())

p1.aniversario()
print(p2.idade())
