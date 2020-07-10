import requests
from Class import EstadoObitos
from funcion import mensagem_inicial, definicao_obito_ou_caso, definicao_taxa, calculo_por_habitantes

mensagem_inicial()
multiplicador = definicao_taxa()
definicao = definicao_obito_ou_caso()

lista_estados = ["ac", "al", "am", "ap", "ba", "ce", "df", "es", "go", "ma", "mg", "ms", "mt", "pa", "pb", "pe",
                         "pi", "pr", "rj", "rn", "rs", "ro", "rr", "sc", "se", "sp", "to"]

lista_dados = []
for estado in lista_estados:
    EstadoObitos(estado, definicao)
    lista_dados.append(EstadoObitos.chama_dados_api_obitos(EstadoObitos, estado))

lista_dados = dict(lista_dados)

pop_estados = {"pop_ac": 881935, "pop_al": 3337357, "pop_am": 4144597,"pop_ap": 845731, "pop_ba": 14873064,
               "pop_ce": 9132078, "pop_df": 3015268, "pop_es": 4018650, "pop_go": 7018354,
               "pop_ma": 7075181, "pop_mg": 21168791, "pop_ms": 2778986, "pop_mt": 3484466, "pop_pa": 8602865,
               "pop_pb": 4018127, "pop_pe": 9557071, "pop_pi": 3273227, "pop_pr": 11433957, "pop_rj": 17264943,
               "pop_rn": 3506853, "pop_rs": 11377239, "pop_ro": 1777225, "pop_rr": 605761, "pop_sc": 7164788,
               "pop_se": 2298696, "pop_sp": 45919049, "pop_to": 1572866}

lista_calculo_por_habitantes = []
for uf in lista_estados:
    lista_calculo_por_habitantes.append(calculo_por_habitantes(lista_dados.get(f"{uf.upper()}"), pop_estados.get(f"pop_{uf}"), multiplicador))

values = lista_calculo_por_habitantes
keys = lista_estados
dict_calculo_por_habitantes = dict(zip(keys, values))
reverse_dict_calculo_por_habitantes = dict(zip(values, keys))
sorted_reverse_dict_calculo_por_habitantes = (sorted(reverse_dict_calculo_por_habitantes, reverse=True))

barra_vertical = "|"
barra_horizontal = "-"

for i in range(len(sorted_reverse_dict_calculo_por_habitantes)):
    print(reverse_dict_calculo_por_habitantes[float(f"{sorted_reverse_dict_calculo_por_habitantes[i]}")].upper(), sorted_reverse_dict_calculo_por_habitantes[i])

