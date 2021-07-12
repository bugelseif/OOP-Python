class Pessoa:
    def __init__(self, nome, sobrenome, idade):
        self.nome = nome
        self.sobrenome = sobrenome
        self.idade = idade

    def nomeCompleto(self):
        return f"{self.nome} {self.sobrenome}"

    def trocarSobrenome(self, sobrenome):
        self.sobrenome = sobrenome

    def aniversario(self):
        self.idade += 1

    def idade(self):
        return self.idade
