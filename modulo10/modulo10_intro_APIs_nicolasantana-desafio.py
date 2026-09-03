import requests

API_KEY = "731aba53421e296ce01d6b5648ea30ea"
FILME_BUSCA = "Inception"
IDIOMA = "pt-BR"

# Endpoint de busca por filmes no TMDB
URL_BUSCA = f"https://api.themoviedb.org/3/search/movie?api_key={API_KEY}&query={FILME_BUSCA}&language={IDIOMA}"

try:
    resposta = requests.get(URL_BUSCA, timeout=5)
    resposta.raise_for_status()
    
    resultados = resposta.json().get("results", [])
    
    if resultados:
        # Pega o primeiro filme retornado pela busca
        filme = resultados[0]
        
        titulo = filme.get("title")
        titulo_original = filme.get("original_title")
        sinopse = filme.get("overview") or "Sinopse não disponível."
        data_lancamento = filme.get("release_date", "N/A")
        
        print("=" * 50)
        print(f" TÍTULO: {titulo} ({data_lancamento[:4]})")
        print(f" Título Original: {titulo_original}")
        print("=" * 50)
        print(f" Sinopse:\n{sinopse}")
        print("=" * 50)
    else:
        print(f"Nenhum filme encontrado com o termo '{FILME_BUSCA}'.")

except requests.exceptions.RequestException as e:
    print(f"Falha ao consultar a API do TMDB: {e}")