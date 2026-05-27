import requests

while True:
    cep = input("Digite o seu CEP: ").replace("-", "").strip()

    if cep == "0":
        break
    response = requests.get(f"https://viacep.com.br/ws/{cep}/json/")

    if response.status_code >= 500:
        print(f"Erro no servidor {response.status_code}")
        break
    elif response.status_code >= 400:
        print(f"CEP inválido {response.status_code}")
        break
    else:
        dados = response.json()

        # *"erro" como dado de verificação, pois o json, caso de erro, ele não retorna um valor booleano, ele retorna uma string (erro)
        if "erro" in dados:
            print("CEP não encontrado")

            for campo in dados.keys():
                print(campo.capitalize())
                break
        else:
            rua    = dados.get("logradouro") or "Não informado"
            cidade = dados.get("localidade") or "Não informado"
            break