#importação de biblioteca utilizada
import requests

#def(): para poder puxar para o frontend
def obter_dados_meteorologicos():
    url = "http://127.0.0.1:8000/v1/forecast"
    params = {
        "latitude": -26.4851,
        "longitude": -49.0713,
    }

    resposta = requests.get(url, params=params)

    #converte em estruturas Python
    if resposta.status_code == 200:
        dados = resposta.json()
        print(dados)
    else:
        print("Erro:", resposta.status_code, resposta.text)

    longitude = dados["longitude"]
    latitude = dados["latitude"]
    return{"longitude":longitude,
           "latitude":latitude}