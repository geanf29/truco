class Jogador:
    def __init__(self, nome):
        self.nome = nome
        self.mao = []
    def __str__(self):
        return f"Jogador: {self.nome}"
    def mostrar_nome(self):
        return f'{self.nome}'
    def mostrar_mao(self):
        return ', '.join(str(carta) for carta in self.mao)
    def receber_carta(self, carta):
        self.mao.append(carta)
    def jogar_carta(self, indice):
        return self.mao.pop(indice)
    
