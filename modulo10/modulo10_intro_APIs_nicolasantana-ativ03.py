import requests

def consultar_clima_seguro(cidade: str, api_key: str):
    """
    Faz a requisição à API do OpenWeatherMap implementando tratamento de exceções
    para falhas HTTP, problemas de conexão, timeout e erros de requisição em geral.
    """
    url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': cidade,
        'appid': api_key,
        'units': 'metric',
        'lang': 'pt_br'
    }

    try:
        # Define um tempo limite de 5 segundos para a resposta
        response = requests.get(url, params=params, timeout=5)
        
        # Lança um HTTPError se o código de status for de erro (4xx ou 5xx)
        response.raise_for_status()

        dados = response.json()
        print(f"--- Clima em {dados['name']} ---")
        print(f"Temperatura: {dados['main']['temp']}°C")
        print(f"Condição: {dados['weather'][0]['description'].capitalize()}")

    except requests.exceptions.HTTPError as http_err:
        if response.status_code == 404:
            print("Erro 404: Cidade não encontrada. Verifique o nome digitado.")
        elif response.status_code == 401:
            print("Erro 401: Chave de API (API Key) inválida ou não autorizada.")
        else:
            print(f"Erro HTTP ocorrido: {http_err}")

    except requests.exceptions.ConnectionError:
        print("Erro de Conexão: Não foi possível conectar ao servidor. Verifique sua conexão de internet.")

    except requests.exceptions.Timeout:
        print("Erro de Tempo Limite: A requisição demorou muito para responder (Timeout).")

    except requests.exceptions.RequestException as err:
        print(f"Ocorreu um erro inesperado na requisição: {err}")

if __name__ == "__main__":
    API_KEY = "SUA_API_KEY_AQUI"
    
    # Teste 1: Cidade válida
    consultar_clima_seguro("Curitiba", API_KEY)
    
    # Teste 2: Cidade inválida para demonstrar o tratamento do erro 404
    print("\nTestando com cidade inexistente:")
    consultar_clima_seguro("CidadeInexistenteXYZ123", API_KEY)