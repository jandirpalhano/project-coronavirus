import requests


class EstadoObitos():
    def __init__(self, uf, definicao):
        lista_estados = ["ac", "al", "am", "ap", "ba", "ce", "df", "es", "go", "ma", "mg", "ms", "mt", "pa", "pb", "pe",
                         "pi", "pr", "rj", "rn", "rs", "ro", "rr", "sc", "se", "sp", "to"]
        if uf in lista_estados and "Óbitos" in definicao:
            self.chama_dados_api_obitos(uf)
        elif uf in lista_estados and "Casos" in definicao:
            self.chama_dados_api_casos(uf)
        else:
            raise ValueError ("UF não disponível na lista de Estados")

    def __str__(self):
        return self.chama_dados_api_obitos()

    def chama_dados_api_obitos(self, uf):
        url = requests.get(f"https://covid19-brazil-api.now.sh/api/report/v1/brazil/uf/{uf}")
        dados_estados = url.json()
        return [
            dados_estados["uf"],
            dados_estados["deaths"]
        ]

    def chama_dados_api_casos(self, uf):
        url = requests.get(f"https://covid19-brazil-api.now.sh/api/report/v1/brazil/uf/{uf}")
        dados_estados = url.json()
        return [
            dados_estados["uf"],
            dados_estados["cases"]
        ]


