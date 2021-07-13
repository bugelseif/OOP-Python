class Pessoa:
    idInc = 0

    @classmethod
    def novoId(cls):
        cls.idInc += 1
        return cls.idInc

    def __init__(self, nome, sobrenome, idade):
        if not self.validaNome(nome):
            raise ValueError('Nome invalido')

        self.id = self.novoId()
        self.nome = nome
        self.sobrenome = sobrenome
        self.idade = idade

    def nomeCompleto(self):
        return f"{self.nome} {self.sobrenome}"

    def trocarSobrenome(self, sobrenome):
        self.sobrenome = sobrenome

    def aniversario(self):
        self.idade += 1

    def retornaIdade(self):
        return self.idade

    @staticmethod
    def validaNome(nome):
        return len(nome) >= 3 and ' ' not in nome


print(Pessoa.validaNome('Bruna'))
