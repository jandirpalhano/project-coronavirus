#from Class from

def mensagem_inicial():
    caracteres = 90
    print("=" * caracteres)
    print(" Bem vinda a ferramenta para cálculo da taxa de covid por habitantes no Estados do Brasil ")
    print("#" * caracteres)

def definicao_taxa():
    global multiplicador
    opcao_multiplicador = input("""
    (1) 100 mil habitantes
    (2) 500 mil habitantes
    (3) 1 milhão de habitantes
    Selecione a taxa a ser utilizada: """)
    taxa_por_extenso = ("100 mil habitantes", "500 mil habitantes", "1 milhão de habitantes")
    lista_opcao_multiplicador = (1, 2, 3)
    lista_opcao_multiplicador = str(lista_opcao_multiplicador)
    while not opcao_multiplicador in lista_opcao_multiplicador:
        opcao_multiplicador = input("   Digite 1, 2 ou 3: ")
    print(f"\nA taxa escolhida é de: {taxa_por_extenso[int(opcao_multiplicador) - 1]}\n")
    if (opcao_multiplicador == "1"):
        multiplicador = 100000
    elif (opcao_multiplicador == "2"):
        multiplicador = 500000
    elif (opcao_multiplicador == "3"):
        multiplicador = 1000000
    return multiplicador


def definicao_obito_ou_caso():
    print("#" * 90)
    opcao_escolhida = input("""    
    (1) Óbitos
    (2) Casos
    Selecione a opção a ser utilizada: """)
    texto_por_extenso = ("Óbitos", "Casos")
    lista_opcao_disponiveis = (1, 2)
    lista_opcao_disponiveis = str(lista_opcao_disponiveis)
    while not opcao_escolhida in lista_opcao_disponiveis :
        opcao_escolhida = input("    Digite 1 ou 2 ")
    print(f"\nA opção escolhida é: {texto_por_extenso[int(opcao_escolhida) - 1]}\n")
    definicao = 0
    if (opcao_escolhida == "1"):
        definicao = "Óbitos"
    elif (opcao_escolhida == "2"):
        definicao = "Casos"
    return definicao

def calculo_por_habitantes (dados, pop, multiplicador):
    return (dados / pop) * multiplicador

