from .baralho import Baralho
from .duplas import Duplas
from .carta import Carta
import random
class Mesa:
    def __init__(self, dupla1, dupla2):
        self.dupla1 = dupla1
        self.dupla2 = dupla2
        self.baralho = Baralho()
        self.vira = None
        self.cartas_jogadas = []
        self.manilha_rodada = None
    def iniciar_mao(self, jogador_cortador, tam_corte):
        self.baralho.embaralhar()
        self.baralho.cortar(tam_corte)
        self.vira = self.baralho.definir_vira()
        print(f"o vira é {self.vira}")
        self.distribuir_cartas(jogador_cortador)
    def encontrar_parceiro(self, jogador):
        if jogador == self.dupla1.jogador1: return self.dupla1.jogador2
        if jogador == self.dupla1.jogador2: return self.dupla1.jogador1

        if jogador == self.dupla2.jogador1: return self.dupla2.jogador2
        if jogador == self.dupla2.jogador2: return self.dupla2.jogador1
        
        return None

    def distribuir_cartas(self, jogador_cortador):
        
        parceiro = self.encontrar_parceiro(jogador_cortador)
        
        print(f"O corte foi de {jogador_cortador.nome}. Primeira carta vai para {parceiro.nome}!")
        
        carta_vip = self.baralho.dar_carta()
        parceiro.receber_carta(carta_vip)

        todos_jogadores = [
            self.dupla1.jogador1, self.dupla1.jogador2,
            self.dupla2.jogador1, self.dupla2.jogador2
        ]

        while any(len(j.mao) < 3 for j in todos_jogadores):
            
            random.shuffle(todos_jogadores) 
            
            for jogador in todos_jogadores:
                if len(jogador.mao) < 3:
                    carta = self.baralho.dar_carta()
                    if carta:
                        jogador.receber_carta(carta)
    
