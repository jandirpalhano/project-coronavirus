def mensagem_inicial():
    print("****************************************************************************************")
    print("Bem vinda a ferramenta para cálculo da taxa de covid por habitantes no Estados do Brasil")
    print("****************************************************************************************")

def definicao_multiplicador():
    print("Selecione a taxa que será utilizada:")
    opcao_multiplicador = int(input("(1) 100 mil habitantes (2) 500 mil habitantes (3) 1 milhão de habitantes?"))
    multiplicardor = 0
    while (multiplicador = 0):
        if opcao_multiplicador == 1:
            multiplicador = 100000
        elif opcao_multiplicador == 2:
            multiplicador = 500000
        elif multiplicador == 3:
            multiplicador = 1000000
        else:
            multiplicador = 0

    return multiplicador