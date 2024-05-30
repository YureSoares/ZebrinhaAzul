import requests
import datetime
from conexaoBanco import ConexaoBanco

class Transito:

    #Inicia classe transito
    def __init__(self):
        self._bd = ConexaoBanco()
        self.origem = 'Uberlândia'  # INSIRA AQUI A CIDADE QUE VOCE QUER USAR COMO ORIGEM
        self.destino = "São José do Rio Preto"  # INSIRA AQUI A CIDADE QUE VOCE QUER USAR COMO DESTINO
        self.api_key = ""  # (DE PREFERENCIA SUBSTITUIR ESTE CAMPO POR SUA CHAVE PESSOAL)
        self.insert_tabela_transito(self.origem, self.destino, "carro", self.api_key)
        self.insert_tabela_transito(self.origem, self.destino, "onibus", self.api_key)

    #metodo usado para converter segundos em horas
    @staticmethod
    def _seg_to_hour(seg):
        return str(datetime.timedelta(seconds=seg))

    #busca informacao de transito na api
    def _buscar_transito(self, origem, destino, tipo, api_key):
        url = f"https://maps.googleapis.com/maps/api/directions/json?origin={origem}&destination={destino}&key={api_key}&language=pt-BR"
        if tipo.upper() == "onibus".upper():
            url = url + "&mode=transit&transit_mode=bus"
        response = requests.get(url)
        data = response.json()
        if data:
            return data
        else:
            raise ValueError(f"Não foram encontrados dados para origem = {origem}, destino= {destino}.")

    #insere os dados na tabela transito
    def insert_tabela_transito(self, origem, destino, tipo, api_key):
        transito = self._buscar_transito(origem, destino, tipo, api_key)
        origemTransito = transito["routes"][0]["legs"][0]["start_address"]
        destinoTransito = transito["routes"][0]["legs"][0]["end_address"]
        distancia = round((transito["routes"][0]["legs"][0]["distance"]["value"]) / 1000)
        duracao = self._seg_to_hour(transito["routes"][0]["legs"][0]["duration"]["value"])
        self._bd.insertTransito(origemTransito, destinoTransito, distancia, duracao)

if __name__ == "__main__":
    Transito()
