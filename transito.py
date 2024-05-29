import requests

class Transito:

    # Metodo que busca dados de rota e verificando se eles sao validos
    def _buscar_transito(origem, destino, tipo, api_key):
        url = f"https://maps.googleapis.com/maps/api/directions/json?origin={origem}&destination={destino}&key={api_key}"
        if tipo.upper() == "onibus".upper():
            url = url + "&mode=transit&transit_mode=bus"
        response = requests.get(url)
        data = response.json()
        if data:
            dados_rota = data
            return data
        else:
            raise ValueError(f"Não foram encontrados dados para origem = {origem}, destino= {destino}.")


    #Definindo varaiveis para busca na API
    api_key = "AIzaSyAuFZdhjEqIM4ABsMcv6IeK4pPyp1If7nU" #(DE PREFERENCIA SUBSTITUIR ESTE CAMPO POR SUA CHAVE PESSOAL)
    origem = 'Uberlândia'
    destino = "São José do Rio Preto"



    onibus = _buscar_transito(origem,destino,"onibus", api_key)


    print("onibus")
    print(f"{onibus["routes"][0]["legs"][0]["duration"]["text"]}")
    print("carro")
    #print(_buscar_transito(origem, destino, "carro", api_key))
