import pessoa

p1 = pessoa.novaPessoa('Bruna', 'Ferreira', 30)
p2 = pessoa.novaPessoa('Camila', 'Lira', 20)

print(pessoa.nomeCompleto(p2))

pessoa.trocarSobrenome(p1, 'Elseif')
print(pessoa.nomeCompleto(p1))

pessoa.aniversario(p2)
print(pessoa.idade(p2))
