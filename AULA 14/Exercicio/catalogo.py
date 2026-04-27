import os
import json
from datetime import date


ARQUIVO_DADOS = "meus_filmes.json"

def limpar_console():
    os.system("cls" if os.name == "nt" else "clear")
    #* Limpar a tela.


def carregar_dados():
    #o try aq é essencial pra caso n ache um arquivo, ao invés de dar erro, vai avisar e continuar da forma que eu quiser
    try:
        with open(ARQUIVO_DADOS, "r", encoding="utf-8") as arquivo:
        # esse encoding="utf-8" é para o python entender caracteres especiais e emojis
            return json.load(arquivo) #* este return serve para retornar as informações a quem chamar está função, no caso é o main.py
    except:
        print("Arquivo não existe. Criando lista vazia...")
        return []


def salvar_dados(dados):
    with open(ARQUIVO_DADOS, "w", encoding="utf-8") as arquivo:
        json.dump(dados, arquivo, indent=4, ensure_ascii=False)
        #* Esse "dados" está carregando uma lista (no dicionário que está dentro da lista) da def carregar_dados 
        #* obs: (especificadamente em json.load(arquivo))
        #* Esse "arquivo" é o que o computador vai salvar (dentro do dicionário que está dentro da lista)

def obter_ano_valido():
    while True:
        try:
            ano = int(input("Ano de lançamento: "))

            if ano < 1888 or ano > date.today().year:
                print("Por favor, digite um ano realista.")
                continue

            return ano
        except ValueError:
            print("Erro. Digite apenas números inteiros para o ano")


def obter_nota_valida():
    while True:
        try:
            nota = float(input("Nota (0.0 a 5.0): "))
            if nota < 0.0 or nota > 5.0:
                print("A nota deve estar entre 0.0 ou 5.0")
                continue

            return nota
        except ValueError:
            print("Digite um valor numérico (use ponto para decimais).")


def adicionar_filmes(catalogo):
    limpar_console()
    print("--- 🎬 REGISTRAR NOVO FILME ---")
    titulo = input("Título: ").strip()

    for filme in catalogo:
        if filme['titulo'].lower() == titulo.lower():
            print(f"\n Atenção: o Filme '{filme['titulo']}' já está cadastrado no seu catalogo!")
            return #* Tudo o que acontecer aqui dentro é retornado para quem chamar a def
        
    genero = input("Gênero (ex: Ação, Comédia, Drama)").strip()
    ano = obter_ano_valido()
    nota = obter_nota_valida()
    critica = input("Breve crítica: ").strip()

    filme = {
        "titulo" : titulo,
        "genero" : genero,
        "ano" : ano,
        "nota" : nota,
        "critica" : critica
    }

    catalogo.append(filme)
    salvar_dados(catalogo)
    print(f"'{titulo}' adicionadio com sucesso ao seu catálogo")


def listar_filmes(catalogo):
    limpar_console()
    print("=" * 40)
    print("     MINHA COLEÇÃO    ")
    print("=" * 40)

    if not catalogo:
        print("O seu catálogo está vazio. Adicione um filme primeiro!")
        print("=" * 40)
        return

    for filme in catalogo:
        estrelas = "⭐" * int(filme["nota"])
        genero = filme.get("genero", "Desconhecido") #get = caso ele n tenha achado dentro do dicionario o genero, ele põem desconhecido
        # isso serve para n quebrar o código, mas mostrar que o filme (ou o que eu codar e quiser achar) não está ali

        print(f"[{filme['ano']}] {filme['titulo'].upper} ({genero}) | Nota: {filme['nota']:.1f} {estrelas}")
        print("=" * 40)


def pesquisar_por_titulo(catalogo):
    limpar_console()
    termo = input("Digite parte do titulo para pesquisar: ").strip().lower()

    resultados = []
    for filme in catalogo:
        if termo in filme["titulo"].lower():
            resultados.append(filme)

    _exibir_resultado_pesquisa(resultados)
    #esse _ no inicio da função é pra dizer que ela vai ser usada dentro da pasta dela, e não em outra pasta


def pesquisar_por_genero(catalogo):
    limpar_console()


def pesquisar_por_ano(catalogo):
    limpar_console()
    while True:
        try:
            ano_pesquisa = int(input("Digite o ano de lançamento exato para pesquisar: "))
            if filme['ano'] == ano_pesquisa:
                resultado.append(filme)
        except ValueError:
            print("Digite apenas numeros!")
            continue


def _exibir_resultado_pesquisa(resultado):

    if resultado:
        print(f"\n Encontrados: {len(resultado)} resultado(s)")

        for filme in resultado:
            genero = filme.get("Genero", "Desconhecido")
            print(f"> {filme['titulo']} ({filme['ano']})- {genero} - Nota: {filme['nota']}")

    else:
        print("Nenhum filme encontrado com esses critérios")

if __name__ == "__main__": # esse código detecta que este arquivo é o principal, na qual só dentro dele podemos fazer testes
    listar_filmes = carregar_dados()
    pesquisar_por_titulo(listar_filmes) 