import time
import requests
from sqlalchemy import URL

URL = "https://servicodados.ibge.gov.br/api/v3/noticias/"

def coletar_noticias(paginas: int = 3, por_pagina: int = 10) -> list[dict]:
    """Percorre paginas da API de noticias e acumula os itens."""
    todas = []
    for page in range(1, paginas + 1):
        params = {"qtd": por_pagina, "page": page}
        resposta = requests.get(URL, params=params, timeout=10)
        resposta.raise_for_status()
        itens = resposta.json()["items"]
        todas.extend(itens)
        print(f"pagina {page}: +{len(itens)} (total {len(todas)})")
        time.sleep(1) # educacao com o servidor
    return todas

#chamada a função
noticias = coletar_noticias(paginas=3, por_pagina=10)
print(f"Total de notícias coletadas: {len(noticias)}")
