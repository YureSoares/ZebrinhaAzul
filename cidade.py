import requests

class Cidade:
    def __init__(self, nome, api_key):
        self.nome = nome
        self.api_key = api_key
        self._latitude = None
        self._longitude = None
        self._buscar_coordenadas()


    #buscando coordenadas e verificando se elas sao validas
    def _buscar_coordenadas(self):
        url = f"http://api.openweathermap.org/geo/1.0/direct?q={self.nome}&appid={self.api_key}"
        response = requests.get(url)
        data = response.json()
        if data:
            self._latitude = data[0].get('lat')
            self._longitude = data[0].get('lon')
        else:
            raise ValueError("Não foram encontrados dados para a cidade fornecida.")

    #setando valor de latitude
    @property
    def latitude(self):
        return self._latitude

    # setando valor de longetitude
    @property
    def longitude(self):
        return self._longitude

