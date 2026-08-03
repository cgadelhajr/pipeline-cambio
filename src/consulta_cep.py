import requests

url = "https://viacep.com.br/ws/52041065/json/"

resposta = requests.get(url, timeout = 10)
print("Status:", resposta.status_code)
print("json:", resposta.json())

def consultar_cep(cep: str) -> dict | None:
    """Consulta um CEP no ViaCEP. Devolve dict, ou None se falhar"""
    url = f"https://viacep.com.br/ws/{cep}/json/"
    try:
        resposta = requests.get(url, timeout=10)
        resposta.raise_for_status()
    except requests.exceptions.Timeout:
        print(f"[erro] ViaCEP demorou demais (cep={cep})")
        return None
    except requests.exceptions.ConnectionError:
        print("[erro] Sem conexão ou servidor fora do ar")
        return None
    except requests.exceptions.HTTPError:
        print(f"[erro] HTTP {resposta.status_code}: {erro}")
        return None