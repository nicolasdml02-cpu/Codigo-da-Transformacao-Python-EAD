import requests

def consultar_clima_filtrado(cidade: str, api_key: str):
    """
    Consome a API do OpenWeatherMap e filtra apenas as informações 
    relevantes, como temperatura e condições climáticas.
    """
    url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': cidade,
        'appid': api_key,
        'units': 'metric',
        'lang': 'pt_br'
    }
    
    response = requests.get(url, params=params)
    dados = response.json()
    
    if response.status_code == 200:
        # Filtrando informações específicas do JSON
        nome_cidade = dados.get('name')
        pais = dados.get('sys', {}).get('country')
        temp = dados.get('main', {}).get('temp')
        sensacao = dados.get('main', {}).get('feels_like')
        humidade = dados.get('main', {}).get('humidity')
        descricao = dados.get('weather', [{}])[0].get('description')

        # Exibição formatada dos dados filtrados
        print("=" * 40)
        print(f" CLIMA EM {nome_cidade.upper()} - {pais}")
        print("=" * 40)
        print(f" Condição:     {descricao.capitalize()}")
        print(f" Temperatura:  {temp:.1f}°C")
        print(f" Sensação:     {sensacao:.1f}°C")
        print(f" Humidade:     {humidade}%")
        print("=" * 40)
    else:
        print(f"Erro ao buscar dados: {dados.get('message', 'Erro desconhecido')}")

if __name__ == "__main__":
    API_KEY = "SUA_API_KEY_AQUI"
    CIDADE = "Rio de Janeiro"
    
    consultar_clima_filtrado(CIDADE, API_KEY)