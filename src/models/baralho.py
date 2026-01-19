import random 
from src.models.carta import Carta

class Baralho:
    def __init__(self):
        self.cartas = [Carta(face, naipe) for naipe in Carta.NAIPES for face in Carta.FACES]

    def __str__(self):
        return f"Baralho com {len(self.cartas)} cartas"

    def embaralhar(self):
        random.shuffle(self.cartas)
    def cortar(self, quantidade):
        self.cartas = self.cartas[:-quantidade]
    def definir_vira(self):
        self.carta_vira = self.cartas.pop()
        return self.carta_vira

    def dar_carta(self):
        if len(self.cartas) > 0:
            return self.cartas.pop()

        return None