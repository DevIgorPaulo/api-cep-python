# Importa a biblioteca requests, utilizada para realizar requisições
# HTTP e estabelecer a comunicação com a API ViaCEP.
import requests


    # Função responsável por solicitar e validar o CEP informado pelo usuário.
def solicita_cep():

        # Mantém a solicitação em repetição até que um CEP válido seja informado.
    while True:

        # Solicita o CEP ao usuário.
        # strip() remove espaços no início e no final da entrada.
        # replace("-", "") remove o hífen caso o CEP seja informado no formato 00000-000.
        cep = input("Digite o seu CEP: ").strip().replace("-", "")

            # Verifica se o CEP possui exatamente 8 caracteres
            # e se todos os caracteres são números.
        if len(cep) == 8 and cep.isdigit():

            # Retorna o CEP para ser utilizado na consulta à API.
            return cep

            # Informa ao usuário que o CEP não atende aos critérios
            # e solicita uma nova entrada.
        else:
            print("CEP inválido. Digite novamente.")


    # Função responsável por consultar a API ViaCEP
    # utilizando o CEP informado pelo usuário.
def busca_cep(cep):

        # Realiza uma requisição HTTP GET para a API ViaCEP.
        # O CEP informado é inserido na URL da requisição.
        # O trecho "/json/" indica que a resposta deve ser retornada em JSON.
    try:
        response = requests.get(
            "https://viacep.com.br/ws/" + cep + "/json/",
        )

        # Verifica se a requisição HTTP apresentou algum erro.
        # Caso ocorra um erro na comunicação, uma exceção será gerada.
        response.raise_for_status()

        # Converte a resposta em formato JSON para uma estrutura
        # que pode ser manipulada pelo Python, neste caso, um dicionário.
        dados = response.json()

        # Captura erros relacionados à requisição, como problemas
        # de conexão ou falhas na comunicação com a API.
    except requests.exceptions.RequestException as e:

        # Exibe na tela a mensagem correspondente ao erro ocorrido.
        print(f"Erro ao buscar CEP: {e}")

        # Indica que não foi possível obter os dados do endereço.
        return None

        # Captura um erro caso a resposta recebida não possa
        # ser interpretada corretamente como JSON.
    except ValueError:

        # Informa ao usuário que a resposta recebida não possui
        # um formato JSON válido.
        print("A resposta não é um JSON válido.")

        # Encerra a consulta sem retornar dados.
        return None

        # Verifica, no dicionário retornado pela API,
        # se existe a indicação de que o CEP não foi encontrado.
    if dados.get("erro"):

        # Informa ao usuário que não existe um endereço correspondente ao CEP informado.
        print("CEP não encontrado.")

        # Encerra a função sem retornar dados.
        return None

    # Retorna o dicionário contendo as informações do endereço.
    return dados


    # Função principal do programa, responsável por organizar
    # a execução das demais funções.
def main():

    # Chama a função que solicita e valida o CEP.
    cep = solicita_cep()

    # Envia o CEP validado para a função responsável pela consulta à API.
    dados = busca_cep(cep)

        # Verifica se a consulta retornou dados válidos.
    if dados:

        # Exibe o CEP retornado pela API.
        print(f"CEP:         {dados.get('cep')}")

        # Exibe o logradouro correspondente ao CEP.
        print(f"Logradouro:  {dados.get('logradouro')}")

        # Exibe o bairro correspondente ao endereço.
        print(f"Bairro:      {dados.get('bairro')}")

        # Exibe a cidade correspondente ao CEP.
        print(f"Cidade:      {dados.get('localidade')}")

        # Exibe a sigla do estado (Unidade Federativa).
        print(f"UF:          {dados.get('uf')}")


# Chama a função principal e inicia a execução do programa.
main()
