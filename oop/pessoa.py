def novaPessoa(nome, sobrenome, idade):
    return{
        'nome': nome,
        'sobrenome': sobrenome,
        'idade': idade,
    }


def nomeCompleto(pessoa):
    return f"{pessoa['nome']} {pessoa['sobrenome']} "


def trocarSobrenome(pessoa, sobrenome):
    pessoa['sobrenome'] = sobrenome


def aniversario(pessoa):
    pessoa['idade'] += 1


def idade(pessoa):
    return pessoa['idade']
