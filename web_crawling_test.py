import requests
from bs4 import BeautifulSoup
import json
import time
import concurrent.futures

def extrair_proxies(numero_pagina):
    url = f"http://www.freeproxylists.net/?page={numero_pagina}"
    resposta = requests.get(url)
    soup = BeautifulSoup(resposta.content, "html.parser")
    
    proxies = []
    tabela = soup.find("table", attrs={"class": "DataGrid"})
    
    if tabela is not None:
        linhas = tabela.find_all("tr")

        for linha in linhas[1:]:
            colunas = linha.find_all("td")
            ip = colunas[0].text.strip()
            porta = colunas[1].text.strip()
            protocolo = colunas[2].text.strip()
            pais = colunas[3].text.strip()
            uptime = colunas[8].text.strip()

            proxy = {
                "ip": ip,
                "porta": porta,
                "protocolo": protocolo,
                "pais": pais,
                "uptime": uptime
            }
            proxies.append(proxy)
    
    return proxies

def salvar_proxies_em_json(proxies):
    with open("proxies.json", "w") as arquivo:
        json.dump(proxies, arquivo, indent=4)

def main():
    tempo_inicio = time.time()
    proxies = []
    
    with concurrent.futures.ThreadPoolExecutor() as executor:
        futuros = [executor.submit(extrair_proxies, numero_pagina) for numero_pagina in range(1, 8)]
        concurrent.futures.wait(futuros)
        
        for futuro in futuros:
            proxies += futuro.result()
    
    salvar_proxies_em_json(proxies)
    
    tempo_execucao = time.time() - tempo_inicio
    
    print(f"Total de proxies capturados: {len(proxies)}")
    print(f"Tempo de execução: {tempo_execucao} segundos")

if __name__ == "__main__":
    main()