import requests

def obter_dados_brutos_clima(cidade: str, api_key: str):
    """
    Consome a API do OpenWeatherMap utilizando a biblioteca requests
    e exibe a resposta JSON completa obtida.
    """
    url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': cidade,
        'appid': api_key,
        'units': 'metric',
        'lang': 'pt_br'
    }
    
    print(f"Fazendo requisição para a API do OpenWeatherMap ({cidade})...\n")
    response = requests.get(url, params=params)
    
    # Exibe o status code e o JSON completo da resposta
    print(f"Status Code: {response.status_code}")
    print("Dados brutos (JSON):")
    print(response.json())

if __name__ == "__main__":
    # Substitua 'SUA_API_KEY_AQUI' pela sua chave da OpenWeatherMap
    API_KEY = "SUA_API_KEY_AQUI"
    CIDADE = "São Paulo"
    
    obter_dados_brutos_clima(CIDADE, API_KEY)