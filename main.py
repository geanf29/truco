from src.models import Baralho, Jogador, Carta, Duplas
jogador1 = Jogador(input("Digite o nome do jogador: "))
jogador2 = Jogador(input("Digite o nome do jogador: "))
dupla1 = Duplas(jogador1, jogador2)
jogador3 = Jogador(input("Digite o nome do jogador: "))
jogador4 = Jogador(input("Digite o nome do jogador: "))
dupla2 = Duplas(jogador3, jogador4)
print(dupla1, dupla2)
meu_baralho = Baralho()
while True:
    try:
        corte = int(input("Quantas cartas deseja cortar do baralho? "))
        if corte > 0 and corte < 27:
            break 
        else:
            raise ValueError("Valor inválido para corte. Deve ser entre 1 e 26.")

    except ValueError as e:
        print(e)
meu_baralho.embaralhar()
meu_baralho.cortar(corte)
print(f"o vira é {meu_baralho.definir_vira()}")
for _ in range(3):
    jogador.receber_carta(meu_baralho.dar_carta())

print(meu_baralho)
print(f'Mão do {jogador} é: {jogador.mostrar_mao()}')
