import requests
from cidade import Cidade
from deep_translator import GoogleTranslator
from conexaoBanco import ConexaoBanco

class Clima:

    def __init__(self):
        self._bd = ConexaoBanco()
        self.api_key = ""  # (DE PREFERENCIA SUBSTITUIR ESTE CAMPO POR SUA CHAVE PESSOAL)
        self.insert_tabela_clima(Cidade('Ubêrlandia', self.api_key), self.api_key)  # INSERIR AQUI CIDADE QUE VOCE QUER USAR DE ORIGEM
        self.insert_tabela_clima(Cidade("São José dos Campos", self.api_key), self.api_key)  # INSERIR AQUI CIDADE QUE VOCE QUER USAR DE DESTINO

    # Método para traduzir o texto de inglês para português
    @staticmethod
    def traduzir(texto):
        return GoogleTranslator(source="en", target="pt").translate(texto)

    # Método para converter Kelvin em Celsius
    @staticmethod
    def kelvin_to_celsius(kelvin):
        return f"{round(kelvin - 273.15)}°C"

    # Método que busca dados de clima e verifica se eles são válidos
    @staticmethod
    def buscar_clima(latitude, longitude, api_key):
        url = f"https://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&appid={api_key}&lang=pt_br"
        try:
            response = requests.get(url)
            data = response.json()
            if data:
                return data
            else:
                raise ValueError("Não foram encontrados dados para as coordenadas fornecidas.")
        except requests.exceptions.RequestException as e:
            raise Exception(f"Falha ao buscar dados do clima: {e}") from e

    # Insere os dados de clima na tabela
    def insert_tabela_clima(self, cidade, api_key):
        getCidade = self.buscar_clima(cidade.latitude, cidade.longitude, api_key)
        cidade_id = cidade._id
        condicao = self.traduzir(getCidade["weather"][0]["main"])
        descricao = getCidade["weather"][0]["description"]
        temperatura = self.kelvin_to_celsius(getCidade["main"]["temp"])
        sensacao = self.kelvin_to_celsius(getCidade["main"]["feels_like"])
        minina = self.kelvin_to_celsius(getCidade["main"]["temp_min"])
        maxima = self.kelvin_to_celsius(getCidade["main"]["temp_max"])
        umidade = f"{getCidade["main"]["humidity"]}%"
        self._bd.insertClima(cidade_id, condicao, descricao, temperatura, sensacao, minina, maxima, umidade)
