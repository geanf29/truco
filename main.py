from src.models.jogador import Jogador
from src.models.duplas import Duplas
from src.models.mesa import Mesa

def main():
    print("\n=== ♠️ ♥️  TRUCO PYTHONICO  ♣️ ♦️ ===\n")

    # 1. CRIANDO A GALERA (Instanciando Objetos)
    print("--- 1. Criando Jogadores e Duplas ---")
    j1 = Jogador("Arnaldo")
    j2 = Jogador("Bernaldo")
    j3 = Jogador("Ceraldo")
    j4 = Jogador("Deraldo")

    # Criando as Duplas (Composição)
    # Dupla 1: Arnaldo e Bernaldo
    dupla_nos = Duplas(j1, j2)
    # Dupla 2: Ceraldo e Deraldo
    dupla_eles = Duplas(j3, j4)

    print(f"Dupla Nós: {dupla_nos}")
    print(f"Dupla Eles: {dupla_eles}")

    # 2. MONTANDO A MESA (O Juiz)
    mesa = Mesa(dupla_nos, dupla_eles)
    
    # ---------------------------------------------------------
    
    # 3. INTERFACE COM USUÁRIO (Simulando a escolha)
    print("\n--- 2. Hora do Corte ---")
    print("Quem vai cortar o baralho?")
    print(f"1 - {j1.nome}")
    print(f"2 - {j2.nome}")
    print(f"3 - {j3.nome}")
    print(f"4 - {j4.nome}")
    
    opcao = int(input("Escolha o número do jogador (1-4): "))
    
    # Lógica para transformar número em Objeto Jogador
    quem_corta = None
    if opcao == 1: quem_corta = j1
    elif opcao == 2: quem_corta = j2
    elif opcao == 3: quem_corta = j3
    elif opcao == 4: quem_corta = j4
    else:
        print("Opção inválida, o Arnaldo vai cortar por padrão.")
        quem_corta = j1

    # Input do tamanho do corte
    try:
        tamanho_corte = int(input(f"{quem_corta.nome}, quantas cartas tirar do topo? (1-20): "))
    except ValueError:
        tamanho_corte = 5 # Valor padrão se der erro

    # ---------------------------------------------------------

    # 4. A MÁGICA ACONTECE (O Motor)
    print("\n--- 3. Iniciando a Mão ---")
    # Aqui a Mesa faz tudo: embaralha, corta, vira e distribui
    mesa.iniciar_mao(quem_corta, tamanho_corte)

    # ---------------------------------------------------------

    # 5. VERIFICAÇÃO (O Teste Final)
    print("\n--- 4. Resultado da Distribuição ---")
    print(f"O Vira da rodada é: {mesa.vira}")
    
    print("\nCartas nas mãos:")
    print(f"{j1.nome}: {j1.mostrar_mao()}")
    print(f"{j2.nome}: {j2.mostrar_mao()}")
    print(f"{j3.nome}: {j3.mostrar_mao()}")
    print(f"{j4.nome}: {j4.mostrar_mao()}")

if __name__ == "__main__":
    main()