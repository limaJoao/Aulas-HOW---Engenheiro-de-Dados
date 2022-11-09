import datetime
import math
from typing import List

# class Pessoa:
#     def __init__(self, nome: str, sobrenome: str, data_de_nascimento: datetime.date):
#         self.nome = nome
#         self.sobrenome = sobrenome
#         self.data_de_nascimento = data_de_nascimento

#     @property
#     def idade(self) -> int:
#         return math.floor((datetime.date.today() - self.data_de_nascimento).days / 365.2425)

#     def __str__(self) -> str:
#         return f"{self.nome} {self.sobrenome} tem {self.idade} anos."

# joao = Pessoa('João Vitor', 'Lima', datetime.date(1994,2,12))

# print(joao)

# class Curriculo:
#     def __init__(self, pessoa: Pessoa, experiencias: List[str]):
#         self.experiencias = experiencias
#         self.pessoa = pessoa

#     @property
#     def quantidade_de_experiencias(self) -> int:
#         return len(self.experiencias)

#     @property
#     def empresa_atual(self) -> str:
#         return self.experiencias[-1]

#     def adiciona_experiencia(self, experiencia: str) -> str:
#         self.experiencias.append(experiencia)

#     def __str__(self):
#         return f"""{self.pessoa.nome} {self.pessoa.sobrenome} tem {self.pessoa.idade} anos e já trabalhou em {self.quantidade_de_experiencias} empresas. Atualmente trabalha na empresa {self.empresa_atual}"""


# # Definindo pessoa e o seu currículo
# curriculo_jv = Curriculo(
#     pessoa=joao, 
#     experiencias=['Correios','Candido Gás', 'Brasil Center', 'CECON', 'Mondelez']
#     )

# # Printando curriculo

# print(curriculo_jv)

# curriculo_jv.adiciona_experiencia('Dadosfera')

# print(curriculo_jv)

## criando classe vivente

class Vivente:
    def __init__(self, nome: str, data_de_nascimento:datetime.date) -> None:
        self.nome = nome
        self.data_de_nascimento = data_de_nascimento

    @property
    def idade(self) -> int:
        return math.floor((datetime.date.today() - self.data_de_nascimento).days / 365.2425)

    def emite_ruido(self, ruido: str):
        print(f"{self.nome} fez ruido: {ruido}")

class Pessoa(Vivente):
    def __str__(self) -> str:
        return f"{self.nome} tem {self.idade} anos."

    def fala(self, frase):
        return self.emite_ruido(frase)

class Cachorro(Vivente):
    def __init__(self, nome: str, data_de_nascimento: datetime.date, raca:str):
        super().__init__(nome, data_de_nascimento)
        self.raca = raca

    def __str__(self):
        return f"{self.nome} é da raça {self.raca} e tem {self.idade} anos."

    def late(self):
        return self.emite_ruido("Au! Au!")

joao = Pessoa('João Vitor', datetime.date(1994,2,12))

print(joao)

maya = Cachorro('Maya', datetime.date(2014,11,10), 'Vira-lata')

print(maya)

maya.late()
maya.late()
joao.fala('Cala a boca Maya!')
maya.late()
maya.late()