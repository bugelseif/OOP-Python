def init(pessoa, nome, sobrenome, idade):
    pessoa['nome'] = nome
    pessoa['sobrenome'] = sobrenome
    pessoa['idade'] = idade


def novaPessoa(nome, sobrenome, idade):
    pessoa = {}
    init(pessoa, nome, sobrenome, idade)
    return pessoa


def nomeCompleto(pessoa):
    return f"{pessoa['nome']} {pessoa['sobrenome']} "


def trocarSobrenome(pessoa, sobrenome):
    pessoa['sobrenome'] = sobrenome


def aniversario(pessoa):
    pessoa['idade'] += 1


def idade(pessoa):
    return pessoa['idade']
