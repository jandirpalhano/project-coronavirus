listaIdEstados = ["do Acre", "de Alagoas", "do Amazonas", "do Amapá", "da Bahia", "do Ceára", "do Distrito Federal", "do Espírito Santo", "de Góias", "do Maranhão", "de Minas Gerais", "do Mato Grosso do Sul", "do Mato Grosso", "do Pará", "da Paraíba", "de Pernambuco", " do Piauí", "do Paraná", "do Rio de Janeiro", "do Rio Grande do Norte", "do Rio Grande do Sul", "de Rondônia", "de Roraima", "de Santa Catarina", "de Sergipe", "de São Paulo", "de Tocantins"]

multiplicador = int(input("Calcular a taxa por 100 habitantes, 500 mil habitantes ou 1 milhão de habitantes?"))

listaPerEstados = ["Número de óbitos no Estado do Acre? ","Número de óbitos no Estado de Alagoas? ", "Número de óbitos no Estado do Amazonas? ","Número de óbitos no Estado da Amapá? ", "Número de óbitos no Estado da Bahia? ", "Número de óbitos no Estado do Ceára? ", "Número de óbitos no Distrito Federal? ","Número de óbitos no Estado do Espírito Santo? ","Número de óbitos no Estado de Góias? ","Número de óbitos no Estado do Maranhão? ","Número de óbitos no Estado de Minas Gerais? ","Número de óbitos no Estado do Mato Grosso do Sul? ","Número de óbitos no Estado do Mato Grosso? ","Número de óbitos no Estado do Pará? ","Número de óbitos no Estado da Paraíba? ","Número de óbitos no Estado de Pernambuco? ","Número de óbitos no Estado do Piauí? ","Número de óbitos no Estado do Paraná? ","Número de óbitos no Estado do Rio de Janeiro? ","Número de óbitos no Estado do Rio Grande do Norte? ","Número de óbitos no Estado de Rio Grande do Sul? ","Número de óbitos no Estado de Rondônia? ","Número de óbitos no Estado de Roraima? ","Número de óbitos no Estado de Santa Catarina? ","Número de óbitos no Estado de Sergipe? ","Número de óbitos no Estado de São Paulo? ","Número de óbitos no Estado do Tocantins? "]

ac = int(input(listaPerEstados[0])); #al = int(input(listaPerEstados[1])); am = int(input(listaPerEstados[2])); ap = int(input(listaPerEstados[3])); ba = int(input(listaPerEstados[4])); ce = int(input(listaPerEstados[5])); df = int(input(listaPerEstados[6])); es = int(input(listaPerEstados[7])); go = int(input(listaPerEstados[8])); ma = int(input(listaPerEstados[9])); mg = int(input(listaPerEstados[10])); ms = int(input(listaPerEstados[11])); mt = int(input(listaPerEstados[12])); pa = int(input(listaPerEstados[13])); pb = int(input(listaPerEstados[14])); pe = int(input(listaPerEstados[15])); pi = int(input(listaPerEstados[16])); pr = int(input(listaPerEstados[17])); rj = int(input(listaPerEstados[18])); rn = int(input(listaPerEstados[19])); rs = int(input(listaPerEstados[20])); ro = int(input(listaPerEstados[21])); rr = int(input(listaPerEstados[22])); sc = int(input(listaPerEstados[23])); se = int(input(listaPerEstados[24])); sp = int(input(listaPerEstados[25])); to = int(input(listaPerEstados[26]));


#lista[pop_ac = 881935, pop_al = 3337357, pop_am = 4144597,pop_ap = 845731, pop_ba = 14873064, pop_ba = 14873064, pop_ce = 9132078, pop_df = 3015268, pop_es = 4018650, pop_go = 7018354, pop_ma = 7075181, pop_mg = 21168791, pop_ms = 2778986, pop_mt = 3484466, pop_pa = 8602865, pop_pb = 4018127, pop_pe = 9557071, pop_pi = 3273227, pop_pr = 11433957, pop_rj = 17264943, pop_rn = 3506853, pop_rs = 11377239, pop_ro = 1777225, pop_rr = 605761, pop_sc = 7164788, pop_se = 2298696, pop_sp = 45919049, pop_to = 1572866];

#listaIdPopEstados: [pop_ac,pop_al,pop_am,pop_ap,pop_ba,pop_ce,pop_df,pop_es,pop_go,pop_ma,pop_mg,pop_ms,pop_mt,pop_pa,pop_pb,pop_pe,pop_pi,pop_pr,pop_rj, pop_rn,pop_rs,pop_ro,pop_rr,pop_sc,pop_se,pop_sp,pop_to];

listaObitosEstados = [ac]# al, am, ap, ba, ce, df, es, go, ma, mg, ms, mt, pa, pb, pe, pi, pr, rj, rn, rs, ro, rr, sc, se, sp, to]

listaPopEstados = [881935,3337357,4144597,845731,14873064,9132078,3015268,4018650,7018354,7075181,21168791,2778986,3484466,8602865,4018127,9557071, 3273227,11433957,17264943,3506853,11377239,1777225,605761,7164788,2298696,45919049,1572866]

import math

def txPorHab (x, y, z):
	return (x / y) * z

txPorHabAc = txPorHab(listaObitosEstados[0], listaPopEstados[0], multiplicador)
#txPorHabAl = txPorHab(listaObitosEstados[1], listaPopEstados[1], multiplicador)
#txPorHabAm = txPorHab(listaObitosEstados[2], listaPopEstados[2], multiplicador) 
#txPorHabAp = txPorHab(listaObitosEstados[3], listaPopEstados[3], multiplicador) 
#txPorHabBa = txPorHab(listaObitosEstados[4], listaPopEstados[4], multiplicador) 
#txPorHabCe = txPorHab(listaObitosEstados[5], listaPopEstados[5], multiplicador) 
#txPorHabDf = txPorHab(listaObitosEstados[6], listaPopEstados[6], multiplicador) 
#txPorHabEs = txPorHab(listaObitosEstados[7], listaPopEstados[7], multiplicador) 
#txPorHabGo = txPorHab(listaObitosEstados[8], listaPopEstados[8], multiplicador) 
#txPorHabMa = txPorHab(listaObitosEstados[9], listaPopEstados[9], multiplicador) 
#txPorHabMg = txPorHab(listaObitosEstados[10], listaPopEstados[10], multiplicador) 
#txPorHabMs = txPorHab(listaObitosEstados[11], listaPopEstados[11], multiplicador) 
#txPorHabMt = txPorHab(listaObitosEstados[12], listaPopEstados[12], multiplicador) 
#txPorHabPa = txPorHab(listaObitosEstados[13], listaPopEstados[13], multiplicador) 
#txPorHabPb = txPorHab(listaObitosEstados[14], listaPopEstados[14], multiplicador) 
#txPorHabPe = txPorHab(listaObitosEstados[15], listaPopEstados[15], multiplicador) 
#txPorHabPi = txPorHab(listaObitosEstados[16], listaPopEstados[16], multiplicador) 
#txPorHabPr = txPorHab(listaObitosEstados[17], listaPopEstados[17], multiplicador) 
#txPorHabRj = txPorHab(listaObitosEstados[18], listaPopEstados[18], multiplicador) 
#txPorHabRn = txPorHab(listaObitosEstados[19], listaPopEstados[19], multiplicador) 
#txPorHabRs = txPorHab(listaObitosEstados[20], listaPopEstados[20], multiplicador) 
#txPorHabRo = txPorHab(listaObitosEstados[21], listaPopEstados[21], multiplicador) 
#txPorHabRr = txPorHab(listaObitosEstados[22], listaPopEstados[22], multiplicador)
#txPorHabSc = txPorHab(listaObitosEstados[23], listaPopEstados[23], multiplicador) 
#txPorHabSe = txPorHab(listaObitosEstados[24], listaPopEstados[24], multiplicador) 
#txPorHabSp = txPorHab(listaObitosEstados[25], listaPopEstados[25], multiplicador) 
#txPorHabTo = txPorHab(listaObitosEstados[26], listaPopEstados[26], multiplicador) 


if (multiplicador == 100000):
	texto_padrao = "A taxa por 100 mil habitantes no Estado"
elif (multiplicador == 500000):
	texto_padrao = "A taxa por 500 mil habitantes no Estado"
else:
	texto_padrao = "A taxa por 1 milhão de habitantes no Estado"

print(texto_padrao,listaIdEstados[0],txPorHabAc)
#print(texto_padrao,txPorHabAl)
#print(texto_padrao,txPorHabAm)
#print(texto_padrao,txPorHabAp)
#print(texto_padrao,txPorHabBa)
#print(texto_padrao,txPorHabCe)
#print(texto_padrao,txPorHabDf)
#print(texto_padrao,txPorHabEs)
#print(texto_padrao,txPorHabGo)
#print(texto_padrao,txPorHabMa)
#print(texto_padrao,txPorHabMg)
#print(texto_padrao,txPorHabMs)
#print(texto_padrao,txPorHabMt)
#print(texto_padrao,txPorHabPa)
#print(texto_padrao,txPorHabPb)
#print(texto_padrao,txPorHabPe)
#print(texto_padrao,txPorHabPi)
#print(texto_padrao,txPorHabPr)
#print(texto_padrao,txPorHabRj)
#print(texto_padrao,txPorHabRn)
#print(texto_padrao,txPorHabRs)
#print(texto_padrao,txPorHabRo)
#print(texto_padrao,txPorHabRr)
#print(texto_padrao,txPorHabSc)
#print(texto_padrao,txPorHabSe)
#print(texto_padrao,txPorHabSp)
#print(texto_padrao,txPorHabTo)