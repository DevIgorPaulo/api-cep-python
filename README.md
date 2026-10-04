# Consulta de CEP em Python

Um projeto simples feito em Python para consultar endereços a partir de um CEP, utilizando a API pública **ViaCEP**.

## O que ele faz?

1. Pede para você digitar um CEP no terminal (funciona com ou sem traço).
2. Valida se o que foi digitado tem 8 dígitos numéricos.
3. Faz a busca automática na API do ViaCEP.
4. Mostra o endereço formatado no terminal:
   - **Logradouro** (Rua/Avenida)
   - **Bairro**
   - **Cidade**
   - **UF** (Estado)

Se o CEP for inválido, não for encontrado ou se houver erro de conexão com a internet, o programa avisa com uma mensagem.

## Como rodar

### 1. Pré-requisitos
- Ter o **Python 3** instalado na sua máquina.
- Ter a biblioteca `requests` instalada:
  ```bash
  pip install requests
  ```

### 2. Execução
No terminal, execute o arquivo:
```bash
python main.py
```

Depois, é só digitar qualquer CEP e conferir o resultado!
