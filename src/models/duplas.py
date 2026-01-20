class Duplas:
    def __init__(self, jogador1, jogador2):
        self.jogador1 = jogador1
        self.jogador2 = jogador2
        self.pontos
    def __str__(self):
        return f'Dupla: {self.jogador1.nome} e {self.jogador2.nome}'
    def somar_pontos(self, pontos):
        self.pontos += pontos
        return self.pontos
