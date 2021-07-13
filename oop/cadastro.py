from Pessoa import Pessoa

p1 = Pessoa('Bruna', 'Ferreira', 30)
p2 = Pessoa('Camila', 'Lira', 20)

print(p1.nomeCompleto())

p1.trocarSobrenome('Elseif')
print(p1.nomeCompleto())

p1.aniversario()
print(p2.retornaIdade())

print(p2.validaNome(p2.nome))

p3 = Pessoa('buuu', 'sem sobrenome', 25)

print(p2.id)
print(Pessoa.idInc)
