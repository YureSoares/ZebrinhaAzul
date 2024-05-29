import requests

from cidade import Cidade
class Clima:

    # Metodo que busca dados de clima e verificando se eles sao validos
    def buscar_clima(latitude, longitude, api_key):
        url = f"https://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&appid={api_key}"
        response = requests.get(url)
        data = response.json()
        if data:
            dados_clima = data
            return data
        else:
            raise ValueError("Não foram encontrados dados para a coordenadas fornecidas.")


    #Definindo varaiveis para busca na API
    api_key = "710dd4e0a7d2504d1a6bfd39fddc344b" #(DE PREFERENCIA SUBSTITUIR ESTE CAMPO POR SUA CHAVE PESSOAL)
    cidade_origem = Cidade('Ubêrlandia',api_key)
    cidade_destino =  Cidade("São José dos Campos",api_key)

    #printa dados de clima da cidade de origem
    print(buscar_clima(cidade_destino.latitude,cidade_destino.longitude,api_key))


