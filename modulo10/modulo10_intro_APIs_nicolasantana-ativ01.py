import requests

# Definição das credenciais e parâmetro de busca
API_KEY = "731aba53421e296ce01d6b5648ea30ea"
CIDADE = "São Paulo"
URL = f"http://api.openweathermap.org/data/2.5/weather?q={CIDADE}&appid={API_KEY}&units=metric&lang=pt_br"

# Requisição GET para a API
resposta = requests.get(URL)

# Exibição do status da resposta e dos dados brutos em formato JSON
print(f"Status Code: {resposta.status_code}")
print("Dados brutos recebidos da API:")
print(resposta.json())