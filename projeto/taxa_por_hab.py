import requests
from Class import EstadoObitos
from func import mensagem_inicial, definicao_obito_ou_caso, definicao_taxa, calculo_por_habitantes


"""mensagem_inicial()
multiplicador = definicao_taxa()
definicao = definicao_obito_ou_caso()
print(definicao)
print(multiplicador)"""

definicao = "Óbitos"
multiplicador = 100000

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

print(lista_dados.values())
print(pop_estados.values())
lista_calculo_por_habitantes = []
#calculo_por_habitantes()
"""for dados_estados in lista_estados:
    i = 0
    lista_calculo_por_habitantes.append(calculo_por_habitantes(lista_dados[i], pop_estados[i], multiplicador))
    i += 1

print(lista_calculo_por_habitantes)
print(lista_dados)"""





"""dados_estados = requests.get("https://covid19-brazil-api.now.sh/api/report/v1/brazil/uf/sp")
print(dados_estados.text)
print(dados_estados.json()['uf'],[state])
#print(dados_estados.json()["uf", "State", "cases", "deaths", "suspects"])
#["""