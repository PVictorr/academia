class AvaliacaoDAO:
    def __init__(self, con):
        self.con = con

    def inserir(self, avaliacao):
        try:
            sql = "INSERT INTO avaliacao (peso, altura, braco, ombro, peito, cintura, quadril, abdominal, coxaMedial, panturrilha, Usuario_codigous) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"

            cursor = self.con.cursor()
            cursor.execute(sql, (avaliacao.peso, avaliacao.altura, avaliacao.braco, avaliacao.ombro, avaliacao.peito, avaliacao.cintura, avaliacao.quadril, avaliacao.abdominal, avaliacao.coxaMedial, avaliacao.panturrilha, avaliacao.Usuario_codigous))
            self.con.commit()
            codigo = cursor.lastrowid
            return codigo
        except:
            return 0

    def listar(self, codigo=None):
        try:
            cursor = self.con.cursor()
            if codigo != None:
                # pegar somente uma planta
                sql = "SELECT * FROM Avaliacao WHERE codigo=%s"
                cursor.execute(sql, (codigo,))
                avaliacao = cursor.fetchone()
                return avaliacao
            else:
                # pegar todas as plantas
                sql = "SELECT * FROM Avaliacao"
                cursor.execute(sql)
                ficha = cursor.fetchall()
                return ficha
        except:
            return None