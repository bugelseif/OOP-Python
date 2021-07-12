from Pessoa import Pessoa

p1 = Pessoa('Bruna', 'Ferreira', 30)
p2 = Pessoa('Camila', 'Lira', 20)

print(Pessoa.nomeCompleto(p1))

Pessoa.trocarSobrenome(p1, 'Elseif')
print(Pessoa.nomeCompleto(p1))

Pessoa.aniversario(p2)
print(Pessoa.idade(p2))
