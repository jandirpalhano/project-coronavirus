
print("********************************************************************************************")
print("**Bem vinda a ferramenta para cálculo da taxa de covid por habitantes no Estados do Brasil**")
print("********************************************************************************************")

opcao_multiplicador = int(input("""\n	(1) 100 mil habitantes 
	(2) 500 mil habitantes 
	(3) 1 milhão de habitantes
	Selecione a taxa que será ultilizada: """))
taxa_por_extenso = ["100 mil habitantes", "500 mil habitantes", "1 milhão de habitantes"]
while (opcao_multiplicador < 1 or opcao_multiplicador > 3):
	opcao_multiplicador = int(input("	Digite 1, 2 ou 3 "))
print("\n A taxa escolhida é de: {}\n".format(taxa_por_extenso[opcao_multiplicador - 1]))
if (opcao_multiplicador == 1):
	multiplicador = 100000
elif (opcao_multiplicador == 2):
	multiplicador = 500000
elif (opcao_multiplicador == 3):
	multiplicador = 1000000

lista_estados = {"ac": "Acre ", "al": "Alagoas ", "am": "Amazonas ", "ap": "Amapá ", "ba": "Bahia ", "ce": "Ceára ", "df": "Distrito Federal ", "es": "Espírito Santo ", "go": "Góias ", "ma": "Maranhão ", "mg": "Minas Gerais ", "ms": "Mato Grosso do Sul ","mt": "Mato Grosso ","pa": "Pará ","pb": "Paraíba ","pe": "Pernambuco ","pi": "Piauí ","pr": "Paraná ","rj": "Rio de Janeiro ", "rn": "Rio Grande do Norte ", "rs": "Rio Grande do Sul ", "ro": "Rondônia ", "rr": "Roraima ", "sc": "Santa Catarina ", "se": "Sergipe ", "sp": "São Paulo ", "to": "Tocantins "}

print("Número de óbitos no Estado/DF: \n")
ac = int(input(lista_estados["ac"])); al = int(input(lista_estados["al"])); am = int(input(lista_estados["am"])); ap = int(input(lista_estados["ap"])); ba = int(input(lista_estados["ba"])); ce = int(input(lista_estados["ce"])); df = int(input(lista_estados["df"])); es = int(input(lista_estados["es"])); go = int(input(lista_estados["go"])); ma = int(input(lista_estados["ma"])); mg = int(input(lista_estados["mg"])); ms = int(input(lista_estados["ms"])); mt = int(input(lista_estados["mt"])); pa = int(input(lista_estados["pa"])); pb = int(input(lista_estados["pb"])); pe = int(input(lista_estados["pe"])); pi = int(input(lista_estados["pi"])); pr = int(input(lista_estados["pr"])); rj = int(input(lista_estados["rj"])); rn = int(input(lista_estados["rn"])); rs = int(input(lista_estados["rs"])); ro = int(input(lista_estados["ro"])); rr = int(input(lista_estados["rr"])); sc = int(input(lista_estados["sc"])); se = int(input(lista_estados["se"])); sp = int(input(lista_estados["sp"])); to = int(input(lista_estados["to"]));

pop_estados = {"pop_ac": 881935, "pop_al": 3337357, "pop_am": 4144597,"pop_ap": 845731, "pop_ba": 14873064, "pop_ba": 14873064, "pop_ce": 9132078, "pop_df": 3015268, "pop_es": 4018650, "pop_go": 7018354, "pop_ma": 7075181, "pop_mg": 21168791, "pop_ms": 2778986, "pop_mt": 3484466, "pop_pa": 8602865, "pop_pb": 4018127, "pop_pe": 9557071, "pop_pi": 3273227, "pop_pr": 11433957, "pop_rj": 17264943, "pop_rn": 3506853, "pop_rs": 11377239, "pop_ro": 1777225, "pop_rr": 605761, "pop_sc": 7164788, "pop_se": 2298696, "pop_sp": 45919049, "pop_to": 1572866}

obitos_estados = {"obitos_ac": ac, "obitos_al": al, "obitos_am": am, "obitos_ap": ap, "obitos_ba": ba, "obitos_ce": ce, "obitos_df": df, "obitos_es": es, "obitos_go": go, "obitos_ma": ma, "obitos_mg": mg, "obitos_ms": ms, "obitos_mt": mt, "obitos_pa": pa, "obitos_pb": pb, "obitos_pe": pe, "obitos_pi": pi, "obitos_pr": pr, "obitos_rj": rj, "obitos_rn": rn, "obitos_rs": rs, "obitos_ro": ro, "obitos_rr": rr, "obitos_sc": sc, "obitos_se": se, "obitos_sp": sp, "obitos_to": to}

import math
from decimal import *
getcontext()
getcontext().prec = 2

def tx_por_hab (obitos, pop, multiplicador):
	return (obitos / pop) * multiplicador

obitos_por_pop_ac = tx_por_hab(obitos_estados["obitos_ac"], pop_estados["pop_ac"], multiplicador); obitos_por_pop_al = tx_por_hab(obitos_estados["obitos_al"], pop_estados["pop_al"], multiplicador); obitos_por_pop_am = tx_por_hab(obitos_estados["obitos_am"], pop_estados["pop_am"], multiplicador); obitos_por_pop_ap = tx_por_hab(obitos_estados["obitos_ap"], pop_estados["pop_ap"], multiplicador); obitos_por_pop_ba = tx_por_hab(obitos_estados["obitos_ba"], pop_estados["pop_ba"], multiplicador); obitos_por_pop_ce = tx_por_hab(obitos_estados["obitos_ce"], pop_estados["pop_ce"], multiplicador); obitos_por_pop_df = tx_por_hab(obitos_estados["obitos_df"], pop_estados["pop_df"], multiplicador); obitos_por_pop_es = tx_por_hab(obitos_estados["obitos_es"], pop_estados["pop_es"], multiplicador); obitos_por_pop_go = tx_por_hab(obitos_estados["obitos_go"], pop_estados["pop_go"], multiplicador); obitos_por_pop_ma = tx_por_hab(obitos_estados["obitos_ma"], pop_estados["pop_ma"], multiplicador); obitos_por_pop_mg = tx_por_hab(obitos_estados["obitos_mg"], pop_estados["pop_mg"], multiplicador); obitos_por_pop_ms = tx_por_hab(obitos_estados["obitos_ms"], pop_estados["pop_ms"], multiplicador); obitos_por_pop_mt = tx_por_hab(obitos_estados["obitos_mt"], pop_estados["pop_mt"], multiplicador); obitos_por_pop_pa = tx_por_hab(obitos_estados["obitos_pa"], pop_estados["pop_pa"], multiplicador); obitos_por_pop_pb = tx_por_hab(obitos_estados["obitos_pb"], pop_estados["pop_pb"], multiplicador); obitos_por_pop_pe = tx_por_hab(obitos_estados["obitos_pe"], pop_estados["pop_pe"], multiplicador); obitos_por_pop_pi = tx_por_hab(obitos_estados["obitos_pi"], pop_estados["pop_pi"], multiplicador); obitos_por_pop_pr = tx_por_hab(obitos_estados["obitos_pr"], pop_estados["pop_pr"], multiplicador); obitos_por_pop_rj = tx_por_hab(obitos_estados["obitos_rj"], pop_estados["pop_rj"], multiplicador); obitos_por_pop_rn = tx_por_hab(obitos_estados["obitos_rn"], pop_estados["pop_rn"], multiplicador); obitos_por_pop_rs = tx_por_hab(obitos_estados["obitos_rs"], pop_estados["pop_rs"], multiplicador); obitos_por_pop_ro = tx_por_hab(obitos_estados["obitos_ro"], pop_estados["pop_ro"], multiplicador); obitos_por_pop_rr = tx_por_hab(obitos_estados["obitos_rr"], pop_estados["pop_rr"], multiplicador); obitos_por_pop_sc = tx_por_hab(obitos_estados["obitos_sc"], pop_estados["pop_sc"], multiplicador); obitos_por_pop_se = tx_por_hab(obitos_estados["obitos_se"], pop_estados["pop_se"], multiplicador); obitos_por_pop_sp = tx_por_hab(obitos_estados["obitos_sp"], pop_estados["pop_sp"], multiplicador); obitos_por_pop_to = tx_por_hab(obitos_estados["obitos_to"], pop_estados["pop_to"], multiplicador);

arredondamento = 1
lista_obitos_por_pop_estados = {"ac": round(obitos_por_pop_ac,arredondamento), "al": round(obitos_por_pop_al,arredondamento), "am": round(obitos_por_pop_am,arredondamento), "ap": round(obitos_por_pop_ap,arredondamento), "ba": round(obitos_por_pop_ba,arredondamento), "ce": round(obitos_por_pop_ce,arredondamento), "df": round(obitos_por_pop_df,arredondamento), "es": round(obitos_por_pop_es,arredondamento), "go": round(obitos_por_pop_go,arredondamento), "ma": round(obitos_por_pop_ma,arredondamento), "mg": round(obitos_por_pop_mg,arredondamento), "ms": round(obitos_por_pop_ms,arredondamento), "mt": round(obitos_por_pop_mt,arredondamento), "pa": round(obitos_por_pop_pa,arredondamento), "pb": round(obitos_por_pop_pb,arredondamento), "pe": round(obitos_por_pop_pe,arredondamento), "pi": round(obitos_por_pop_pi,arredondamento), "pr": round(obitos_por_pop_pr,arredondamento), "rj": round(obitos_por_pop_rj,arredondamento), "rn": round(obitos_por_pop_rn,arredondamento), "rs": round(obitos_por_pop_rs,arredondamento), "ro": round(obitos_por_pop_ro,arredondamento), "rr": round(obitos_por_pop_rr,arredondamento), "sc": round(obitos_por_pop_sc,arredondamento), "se": round(obitos_por_pop_se,arredondamento), "sp": round(obitos_por_pop_sp,arredondamento), "to": round(obitos_por_pop_to,arredondamento)}

sorted(lista_obitos_por_pop_estados)

if (multiplicador == 100000):
	texto_padrao = "taxa por 100 mil habitantes"
elif (multiplicador == 500000):
	texto_padrao = "taxa por 500 mil habitantes"
else:
	texto_padrao = "taxa por 1 milhão de habitantes"

listaIdEstados = ["do Acre", "de Alagoas", "do Amazonas", "do Amapá", "da Bahia", "do Ceára", "do Distrito Federal", "do Espírito Santo", "de Góias", "do Maranhão", "de Minas Gerais", "do Mato Grosso do Sul", "do Mato Grosso", "do Pará", "da Paraíba", "de Pernambuco", "do Piauí", "do Paraná", "do Rio de Janeiro", "do Rio Grande do Norte", "do Rio Grande do Sul", "de Rondônia", "de Roraima", "de Santa Catarina", "de Sergipe", "de São Paulo", "de Tocantins"]

print("\nSegue a lista dos Estados e o DF com a {}:".format(texto_padrao))
print("\n",lista_estados["ac"],lista_obitos_por_pop_estados["ac"],"\n",lista_estados["al"],lista_obitos_por_pop_estados["al"],"\n",lista_estados["am"],lista_obitos_por_pop_estados["am"],"\n",lista_estados["ap"],lista_obitos_por_pop_estados["ap"],"\n",lista_estados["ba"],lista_obitos_por_pop_estados["ba"],"\n",lista_estados["ce"],lista_obitos_por_pop_estados["ce"],"\n",lista_estados["df"],lista_obitos_por_pop_estados["df"],"\n",lista_estados["es"],lista_obitos_por_pop_estados["es"],"\n",lista_estados["go"],lista_obitos_por_pop_estados["go"],"\n",lista_estados["ma"],lista_obitos_por_pop_estados["ma"],"\n",lista_estados["mg"],lista_obitos_por_pop_estados["mg"],"\n",lista_estados["ms"],lista_obitos_por_pop_estados["ms"],"\n",lista_estados["mt"],lista_obitos_por_pop_estados["mt"],"\n",lista_estados["pa"],lista_obitos_por_pop_estados["pa"],"\n",lista_estados["pb"],lista_obitos_por_pop_estados["pb"],"\n",lista_estados["pe"],lista_obitos_por_pop_estados["pe"],"\n",lista_estados["pi"],lista_obitos_por_pop_estados["pi"],"\n",lista_estados["pr"],lista_obitos_por_pop_estados["pr"],"\n",lista_estados["rj"],lista_obitos_por_pop_estados["rj"],"\n",lista_estados["rn"],lista_obitos_por_pop_estados["rn"],"\n",lista_estados["rs"],lista_obitos_por_pop_estados["rs"],"\n",lista_estados["ro"],lista_obitos_por_pop_estados["ro"],"\n",lista_estados["rr"],lista_obitos_por_pop_estados["rr"],"\n",lista_estados["sc"],lista_obitos_por_pop_estados["sc"],"\n",lista_estados["se"],lista_obitos_por_pop_estados["se"],"\n",lista_estados["sp"],lista_obitos_por_pop_estados["sp"],"\n",lista_estados["to"],lista_obitos_por_pop_estados["to"])
