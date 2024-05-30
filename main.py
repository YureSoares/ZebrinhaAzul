from conexaoBanco import ConexaoBanco
from clima import Clima
from transito import Transito

class main:

    # Inicia a conexao com o banco de dados
    conexao = ConexaoBanco()
    # cria as informacoes inicias
    conexao.firstInit()
    #Inicia clima
    clima = Clima()
    #Inicia transito
    transito = Transito()

