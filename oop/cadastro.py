from Pessoa import Japones, Pessoa, PessoaAutenticavel

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


p4 = PessoaAutenticavel('Supimpa', 'Caverna', 55, 'supimpa', '1234')

print(p4.autenticar('supimpa', '12345'))
print(p4.nomeCompleto())


p5 = Japones('Kenshin', 'Himura', 45)
print(p5.nomeCompleto())
