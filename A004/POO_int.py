import datetime
import math

class Pessoa:
    def __init__(self, nome: str, sobrenome: str, data_de_nascimento: datetime.date):
        self.nome = nome
        self.sobrenome = sobrenome
        self.data_de_nascimento = data_de_nascimento

    @property
    def idade(self) -> int:
        return math.floor((datetime.date.today() - self.data_de_nascimento).days / 365.2425)

    def __str__(self) -> str:
        return f"{self.nome} {self.sobrenome} tem {self.idade} anos."

#criando a pessoa
joao = Pessoa(nome='João Vitor', sobrenome='Lima', data_de_nascimento=datetime.date(1994,2,12))

print(joao)
print(joao.nome)
print(joao.sobrenome)
print(joao.data_de_nascimento)