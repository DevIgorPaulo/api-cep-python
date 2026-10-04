import requests

def solicita_cep():

    while True:
        cep = input("Digite o seu CEP: ").strip().replace("-", "")
            
        if len(cep) == 8 and cep.isdigit():
            return cep
        else:
            print("CEP inválido. Digite novamente.")

def busca_ce(cep):

    try:
        response = requests.get(
            "https://viacep.com.br/ws/" + cep + "/json/",
        )
        response.raise_for_status()
        dados = response.json()

    except requests.exceptions.RequestException as e:
        print(f"Erro ao buscar CEP: {e}")
        return None
        
    except ValueError:
        print("A resposta não é um JSON válido.")
        return None

    if dados.get("erro"):
        print("CEP não encontrado.")
        return None
        
    return dados

def main():
    cep = solicita_cep()
    dados = busca_ce(cep)

    if dados:
        print(f"CEP:         {dados.get('cep')}")
        print(f"Logradouro:  {dados.get('logradouro')}")
        print(f"Bairro:      {dados.get('bairro')}")
        print(f"Cidade:      {dados.get('localidade')}")
        print(f"UF:          {dados.get('uf')}")

main()
        


