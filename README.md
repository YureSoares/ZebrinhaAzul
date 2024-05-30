# README

## Descrição
Este projeto utiliza as APIs de Clima e de Trânsito para fornecer informações atualizadas sobre o tempo e condições de tráfego. O projeto requer a instalação de bibliotecas específicas e a configuração de um banco de dados MySQL.

## Pré-requisitos

1. **Contas e Chaves de API:**
   - **API de Clima:** Crie uma conta e obtenha sua chave da API no [OpenWeatherMap](https://openweathermap.org/api).
   - **API de Trânsito:** Crie uma conta e obtenha sua chave da API no [Google Maps Directions API](https://developers.google.com/maps/documentation/directions/overview).

2. **Bibliotecas Python:**
   - Instale a biblioteca `requests` através do comando:
     ```sh
     pip install requests
     ```
   - Instale a biblioteca `deep-translator` através do comando:
     ```sh
     pip install deep-translator
     ```
   - Instale a biblioteca `mysql-connector-python` através do comando:
     ```sh
     pip install mysql-connector-python
     ```

3. **Banco de Dados MySQL:**
   - É necessário ter um banco de dados MySQL instalado e configurado na sua máquina.
   - O MySQL pode ser baixado gratuitamente através do [link oficial](https://dev.mysql.com/downloads/).
   - Um arquivo SQL (`scriptBD.sql`) contendo a criação da instância vazia do banco de dados está disponível no repositório.

## Configuração

1. **Banco de Dados MySQL:**
   - Execute o arquivo `scriptBD.sql` no seu banco de dados MySQL para criar a instância necessária.
   - Substitua as variáveis de conexão com o banco de dados MySQL pelas suas variáveis pessoais.

2. **Chaves das APIs:**
   - Substitua as chaves das APIs (`API_KEY_WEATHER` e `API_KEY_TRAFFIC`) pelas suas chaves pessoais obtidas durante o registro.

## Tutorial

### Passo 1: Obter as chaves das APIs
- **API de Clima:**
  1. Vá para [OpenWeatherMap](https://openweathermap.org/api).
  2. Crie uma conta e obtenha sua chave da API.

- **API de Trânsito:**
  1. Vá para [Google Maps Directions API](https://developers.google.com/maps/documentation/directions/overview).
  2. Crie uma conta e obtenha sua chave da API.

### Passo 2: Instalar as bibliotecas Python
- Execute os seguintes comandos no seu terminal para instalar as bibliotecas necessárias:
  ```sh
  pip install requests
  pip install deep-translator
  pip install mysql-connector-python
  ```

### Passo 3: Configurar o Banco de Dados MySQL
1. Baixe e instale o MySQL da [página oficial](https://dev.mysql.com/downloads/).
2. Execute o arquivo `scriptBD.sql` para criar a instância vazia do banco de dados:
   ```sh
   mysql -u seu_usuario -p < scriptBD.sql
   ```
3. Configure as variáveis de conexão no seu script Python:
   ```python
   db_config = {
       'user': 'seu_usuario',
       'password': 'sua_senha',
       'host': 'localhost',
       'database': 'seu_banco_de_dados'
   }
   ```

### Passo 4: Substituir as Chaves das APIs
- No seu script Python, substitua as variáveis `API_KEY_WEATHER` e `API_KEY_TRAFFIC` pelas suas chaves pessoais:
  ```python
  API_KEY_WEATHER = 'sua_chave_api_weather'
  API_KEY_TRAFFIC = 'sua_chave_api_traffic'
  ```

### Passo 5: Executar o Projeto
- Após configurar tudo corretamente, execute o seu script Python para começar a utilizar as APIs e o banco de dados MySQL.

## Suporte
Para qualquer dúvida ou problema, por favor, abra uma issue no repositório ou entre em contato com o mantenedor do projeto.
