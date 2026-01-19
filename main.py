from src.models import Baralho, Jogador, Carta
jogador = Jogador(input("Digite o nome do jogador: "))

meu_baralho = Baralho()
while True:
    try:
        tam_corte = int(input("Quantas cartas deseja cortar do baralho? "))

        
        if tam_corte > 0 and tam_corte < 27:
            break 
        else:
            raise ValueError("Valor inválido para corte. Deve ser entre 1 e 26.")

    except ValueError as e:
        print(e)
meu_baralho.embaralhar()
meu_baralho.cortar(tam_corte)
print(f"o vira é {meu_baralho.definir_vira()}")
for _ in range(3):
    jogador.receber_carta(meu_baralho.dar_carta())

print(meu_baralho)
print(f'Mão do {jogador} é: {jogador.mostrar_mao()}')
print("--- TESTE DE MANILHA ---")
vira_fake = Carta('3', 'Ouros') # O último da lista
minha_carta = Carta('4', 'Paus') # O primeiro da lista (deve ser manilha)

if minha_carta.ismanilha(vira_fake):
    print(f"Sucesso! Com vira {vira_fake.face}, a manilha é {minha_carta.face}")
else:
    print("Erro na matemática circular!")
print("------------------------")
