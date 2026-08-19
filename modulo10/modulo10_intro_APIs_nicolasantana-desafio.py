import requests

# Mapeamento prévio dos principais gêneros do TMDB para exibição amigável
GENEROS_TMDB = {
    28: "Ação", 12: "Aventura", 16: "Animação", 35: "Comédia", 80: "Crime",
    99: "Documentário", 18: "Drama", 10751: "Família", 14: "Fantasia",
    36: "História", 27: "Terror", 10402: "Música", 9648: "Mistério",
    10749: "Romance", 878: "Ficção Científica", 10770: "Cinema TV",
    53: "Thriller", 10752: "Guerra", 37: "Faroeste"
}

def buscar_filme_tmdb(nome_filme: str, api_key: str):
    """
    Busca dados de um filme na API do TMDB e exibe título, gênero e sinopse.
    """
    url = "https://api.themoviedb.org/3/search/movie"
    params = {
        'api_key': api_key,
        'query': nome_filme,
        'language': 'pt-BR'
    }

    try:
        response = requests.get(url, params=params, timeout=5)
        response.raise_for_status()

        resultados = response.json().get('results', [])

        if not resultados:
            print(f"Nenhum filme encontrado com o título: '{nome_filme}'")
            return

        # Pega o primeiro filme retornado na busca
        filme = resultados[0]

        titulo = filme.get('title', 'Sem título')
        titulo_original = filme.get('original_title', '')
        sinopse = filme.get('overview', 'Sinopse não disponível em português.')
        ids_generos = filme.get('genre_ids', [])

        # Traduz os IDs de gênero para nomes legíveis
        generos = [GENEROS_TMDB.get(gid, "Outro") for gid in ids_generos]
        generos_str = ", ".join(generos) if generos else "Não especificado"

        print("=" * 60)
        print(f" TÍTULO: {titulo} ({titulo_original})")
        print("=" * 60)
        print(f" Gênero(s): {generos_str}")
        print("-" * 60)
        print(f" Sinopse:\n {sinopse if sinopse else 'Sem sinopse disponível.'}")
        print("=" * 60)

    except requests.exceptions.RequestException as err:
        print(f"Erro ao conectar à API do TMDB: {err}")

if __name__ == "__main__":
    # Substitua pela sua chave da API do TMDB (v3 auth)
    API_KEY_TMDB = "SUA_API_KEY_TMDB_AQUI"
    
    filme_busca = input("Digite o nome de um filme para buscar: ").strip()
    if filme_busca:
        buscar_filme_tmdb(filme_busca, API_KEY_TMDB)
    else:
        print("Nenhum termo digitado. Executando busca padrão por 'Inception'...")
        buscar_filme_tmdb("Inception", API_KEY_TMDB)