def mensagem_inicial():
    caracteres = 90
    print("=" * caracteres)
    print(" Bem vinda a ferramenta para cálculo da taxa de covid por habitantes no Estados do Brasil ")
    print("#" * caracteres)

def definicao_taxa(): #Definição da taxa por habitantes a ser utilizada
	opcao_multiplicador = int(input("""\n	(1) 100 mil habitantes 
	(2) 500 mil habitantes 
	(3) 1 milhão de habitantes
	Selecione a taxa que será ultilizada: """))
	taxa_por_extenso = ["100 mil habitantes", "500 mil habitantes", "1 milhão de habitantes"]
	while (opcao_multiplicador < 1 or opcao_multiplicador > 3):
		opcao_multiplicador = int(input("	Digite 1, 2 ou 3 "))
	print("\nA taxa escolhida é de: {}\n".format(taxa_por_extenso[opcao_multiplicador - 1]))
	if (opcao_multiplicador == 1):
	    multiplicador = 100000
	elif (opcao_multiplicador == 2):
		multiplicador = 500000
	elif (opcao_multiplicador == 3):
		multiplicador = 1000000
	return multiplicador

def calculo_por_hab (obitos, pop, multiplicador):
	return (obitos / pop) * multiplicador

def espaco_estado(estado): #função para contar os caracteres e dar espaço para poder inserir a barra vertical alinhada
    caracteres_antes_barra = 20
    carac_estado = len(estado)
    carac_espaco = caracteres_antes_barra - carac_estado
    return ' ' * carac_espaco

def espaco_resultado(resultado): #funçao para imprimir os caraceres em branco após a bbara vertical
    caracteres_apos_barra = 6
    resultado = str(round(resultado))
    carac_resultado = len(resultado)
    carac_espaco = caracteres_apos_barra - carac_resultado
    return ' ' * carac_espaco

def definicao_texto_taxa(multiplicador):
    if (multiplicador == 100000):
        texto_padrao = "taxa por 100 mil habitantes"
    elif (multiplicador == 500000):
        texto_padrao = "taxa por 500 mil habitantes"
    else:
        texto_padrao = "taxa por 1 milhão de habitantes"
    return texto_padrao
