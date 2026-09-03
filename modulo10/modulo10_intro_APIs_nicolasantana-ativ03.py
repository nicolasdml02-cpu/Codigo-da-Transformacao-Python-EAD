import requests

API_KEY = "731aba53421e296ce01d6b5648ea30ea"
CIDADE = "São Paulo"
URL = f"http://api.openweathermap.org/data/2.5/weather?q={CIDADE}&appid={API_KEY}&units=metric&lang=pt_br"

try:
    # Define um tempo limite de 5 segundos para a requisição
    resposta = requests.get(URL, timeout=5)
    
    # Lança uma exceção se a resposta HTTP indicar erro (códigos 4xx ou 5xx)
    resposta.raise_for_status()

    dados = resposta.json()
    
    temperatura = dados["main"]["temp"]
    descricao = dados["weather"][0]["description"].capitalize()
    
    print(f"Conexão bem-sucedida! Cidade: {CIDADE}")
    print(f"Temperatura atual: {temperatura}°C ({descricao})")

except requests.exceptions.HTTPError as err_http:
    print(f"Erro HTTP encontrado: {err_http}")
    if resposta.status_code == 401:
        print("Dica: Verifique se a sua API_KEY do OpenWeatherMap está correta.")
    elif resposta.status_code == 404:
        print("Dica: Verifique se o nome da cidade foi digitado corretamente.")

except requests.exceptions.ConnectionError:
    print("Erro de Conexão: Não foi possível conectar ao servidor. Verifique sua internet.")

except requests.exceptions.Timeout:
    print("Erro de Tempo Limite: A requisição demorou demais para responder.")

except requests.exceptions.RequestException as err:
    print(f"Ocorreu um erro inesperado na requisição: {err}")