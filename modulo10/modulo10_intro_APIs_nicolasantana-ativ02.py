import requests

API_KEY = "731aba53421e296ce01d6b5648ea30ea"
CIDADE = "São Paulo"
URL = f"http://api.openweathermap.org/data/2.5/weather?q={CIDADE}&appid={API_KEY}&units=metric&lang=pt_br"

resposta = requests.get(URL)
dados = resposta.json()

# Filtrando dados específicos do JSON retornado
nome_cidade = dados.get("name")
temperatura = dados["main"]["temp"]
sensacao_termica = dados["main"]["feels_like"]
umidade = dados["main"]["humidity"]
descricao_clima = dados["weather"][0]["description"].capitalize()

# Exibindo os dados organizados
print("=" * 35)
print(f" PREVISÃO DO TEMPO: {nome_cidade.upper()} ")
print("=" * 35)
print(f" Clima: {descricao_clima}")
print(f" Temperatura: {temperatura}°C")
print(f" Sensação Térmica: {sensacao_termica}°C")
print(f" Umidade do Ar: {umidade}%")
print("=" * 35)