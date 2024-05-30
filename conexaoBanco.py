import mysql.connector

class ConexaoBanco:
    def __init__(self):
        self.host = "localhost"  # Insira aqui seu host
        self.user = "root"  # Insira aqui seu usuário
        self.password = "123456"  # Insira aqui sua senha
        self.database = "ZebrinhaAzul"

    # Usado para criar os campos necessários na primeira vez que o programa é executado
    def firstInit(self):
        self.createDatabase()
        self.createCidade()
        self.createClima()
        self.createTransito()

    # Criando conexão com o banco de dados
    def iniciaConexao(self):
        try:
            conexao = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database
            )
            print("Conectado ao MySQL com sucesso!")
            return conexao
        except mysql.connector.Error as e:
            print(f"Erro ao conectar ao MySQL: {e}")

    # Usado para finalizar a conexão aberta para alguma consulta
    def finalizaConexao(self, conexao):
        if conexao:
            conexao.close()

    # Verifica se um banco de dados MySQL existe.
    def check_database_exists(self, connection, nome):
        cursor = None
        try:
            cursor = connection.cursor()
            cursor.execute("SHOW DATABASES")
            databases = [db[0] for db in cursor.fetchall()]
            return nome in databases

        except mysql.connector.Error as e:
            print(f"Erro ao conectar ao MySQL: {e}")
        finally:
            if cursor:
                cursor.close()

    # Verifica se a tabela existe
    def check_table_exists(self, connection, nome):
        cursor = None
        try:
            cursor = connection.cursor()
            cursor.execute(f"SHOW TABLES LIKE '{nome}'")
            return cursor.fetchone() is not None

        except mysql.connector.Error as e:
            print(f"Erro ao conectar ao MySQL: {e}")
        finally:
            if cursor:
                cursor.close()

    # Cria o database pela primeira vez
    def createDatabase(self):
        con = None
        try:
            con = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password
            )
            print("Conectado ao MySQL com sucesso!")

            if not self.check_database_exists(con, self.database):
                cursor = con.cursor()
                cursor.execute(f"CREATE DATABASE {self.database}")
                print(f"Banco de dados '{self.database}' criado com sucesso!")
            else:
                print(f"Banco de dados '{self.database}' já existe.")
        except mysql.connector.Error as e:
            print(f"Erro ao conectar ao MySQL: {e}")
        finally:
            if con:
                con.close()

    # Cria a tabela de cidade
    def createCidade(self):
        conexao = self.iniciaConexao()
        cursor = None
        try:
            cursor = conexao.cursor()
            if not self.check_table_exists(conexao, "cidade"):
                sql = """
                    CREATE TABLE `cidade` (
                          `cidade_id` int NOT NULL AUTO_INCREMENT,
                          `nome` varchar(45) DEFAULT NULL,
                          PRIMARY KEY (`cidade_id`)
                        )
                """
                cursor.execute(sql)
                print("Tabela 'cidade' criada com sucesso!")
            else:
                print("Tabela 'cidade' já existe.")
        except mysql.connector.Error as e:
            print(f"Erro ao conectar ao MySQL: {e}")
        finally:
            if cursor:
                cursor.close()
            self.finalizaConexao(conexao)

    # Cria a tabela de trânsito
    def createTransito(self):
        conexao = self.iniciaConexao()
        cursor = None
        try:
            cursor = conexao.cursor()
            if not self.check_table_exists(conexao, "transito"):
                sql = """
                        CREATE TABLE `transito` (
                              `transito_id` int NOT NULL AUTO_INCREMENT,
                              `origem` varchar(255) DEFAULT NULL,
                              `destino` varchar(255) DEFAULT NULL,
                              `distancia` int DEFAULT NULL,
                              `duracao` varchar(20) DEFAULT NULL,
                              PRIMARY KEY (`transito_id`)
                            )
                    """
                cursor.execute(sql)
                print("Tabela 'transito' criada com sucesso!")
            else:
                print("Tabela 'transito' já existe.")
        except mysql.connector.Error as e:
            print(f"Erro ao conectar ao MySQL: {e}")
        finally:
            if cursor:
                cursor.close()
            self.finalizaConexao(conexao)

    # Cria a tabela de clima
    def createClima(self):
        conexao = self.iniciaConexao()
        cursor = None
        try:
            cursor = conexao.cursor()
            if not self.check_table_exists(conexao, "clima"):
                sql = """ CREATE TABLE `clima` (
                              `clima_id` int NOT NULL AUTO_INCREMENT,
                              `cidade_id` int NOT NULL,
                              `condicao` varchar(100) DEFAULT NULL,
                              `descricao` varchar(100) DEFAULT NULL,
                              `temperatura` varchar(5) DEFAULT NULL,
                              `sensacao` varchar(5) DEFAULT NULL,
                              `minina` varchar(5) DEFAULT NULL,
                              `maxima` varchar(5) DEFAULT NULL,
                              `umidade` varchar(5) DEFAULT NULL,
                              PRIMARY KEY (`clima_id`),
                              KEY `fk_clima` (`cidade_id`),
                              CONSTRAINT `fk_clima` FOREIGN KEY (`cidade_id`) REFERENCES `cidade` (`cidade_id`)
                            )  """
                cursor.execute(sql)
                print("Tabela 'clima' criada com sucesso!")
            else:
                print("Tabela 'clima' já existe.")
        except mysql.connector.Error as e:
            print(f"Erro ao conectar ao MySQL: {e}")
        finally:
            if cursor:
                cursor.close()
            self.finalizaConexao(conexao)

    # Faz insert na tabela de trânsito
    def insertTransito(self, origem, destino, distancia, duracao):
        conexao = self.iniciaConexao()
        cursor = None
        try:
            cursor = conexao.cursor()
            sql = "INSERT INTO transito (origem, destino, distancia, duracao) VALUES (%s, %s, %s, %s)"
            cursor.execute(sql, (origem, destino, distancia, duracao))
            conexao.commit()
        except mysql.connector.Error as e:
            print(f"Erro ao conectar ao MySQL: {e}")
        finally:
            if cursor:
                cursor.close()
            self.finalizaConexao(conexao)

    # Faz insert na tabela de clima
    def insertClima(self, cidade_id, condicao, descricao, temperatura, sensacao, minina, maxima, umidade):
        conexao = self.iniciaConexao()
        cursor = None
        try:
            cursor = conexao.cursor()
            sql = "INSERT INTO clima (cidade_id, condicao, descricao, temperatura, sensacao, minina, maxima, umidade) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
            cursor.execute(sql, (cidade_id, condicao, descricao, temperatura, sensacao, minina, maxima, umidade))
            conexao.commit()
        except mysql.connector.Error as e:
            print(f"Erro ao conectar ao MySQL: {e}")
        finally:
            if cursor:
                cursor.close()
            self.finalizaConexao(conexao)

    # Faz insert na tabela de cidade
    def insertCidade(self, nome):
        conexao = self.iniciaConexao()
        cursor = None
        try:
            cursor = conexao.cursor()
            sql = """
                SELECT * FROM cidade
                WHERE UPPER(nome) = UPPER(%s)
            """
            cursor.execute(sql, (nome.upper(),))

            cidade = cursor.fetchone()
            if not cidade:
                sql = "INSERT INTO cidade (nome) VALUES (%s)"
                cursor.execute(sql, (nome,))
                conexao.commit()
        except mysql.connector.Error as e:
            print(f"Erro ao conectar ao MySQL: {e}")
        finally:
            if cursor:
                cursor.close()
            self.finalizaConexao(conexao)

    # Seleciona o ID da cidade pelo Nome fornecido
    def selectIdByName(self, nome):
        conexao = self.iniciaConexao()
        cursor = None
        cidade_id = None
        try:
            cursor = conexao.cursor()
            sql = """
                   SELECT cidade_id FROM cidade
                   WHERE UPPER(nome) = UPPER(%s)
               """
            cursor.execute(sql, (nome.upper(),))
            resultado = cursor.fetchone()
            if resultado:
                cidade_id = resultado[0]
        except mysql.connector.Error as e:
            print(f"Erro ao conectar ao MySQL: {e}")
        finally:
            if cursor:
                cursor.close()
            self.finalizaConexao(conexao)
        return cidade_id
