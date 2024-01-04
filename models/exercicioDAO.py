class ExercicioDAO:
    def __init__(self, con):
        self.con = con

    def inserir(self, exercicios):
        try:
            sql = "INSERT INTO Treino_has_Exercicios (carga, series, repeticoes) VALUES (%s, %s, %s)"

            cursor = self.con.cursor()
            cursor.execute(sql, (exercicios.carga, exercicios.series, exercicios.repeticoes))
            self.con.commit()
            codigo = cursor.lastrowid
            return codigo
        except:
            return 0

    def listar_peito(self, codigo=None):
        try:
            cursor = self.con.cursor()
            if codigo != None:
                sql = 'SELECT * FROM Exercicios WHERE tp_treino="Peito"'
                cursor.execute(sql, (codigo,))
                peito = cursor.fetchone()
                return peito
            else:
                sql = 'SELECT * FROM Exercicios WHERE tp_treino="Peito"'
                cursor.execute(sql)
                peitos = cursor.fetchall()
                return peitos
        except:
            return None

    def listar_perna(self, codigo=None):
        try:
            cursor = self.con.cursor()
            if codigo != None:
                sql = 'SELECT * FROM Exercicios WHERE tp_treino="Perna"'
                cursor.execute(sql, (codigo,))
                perna = cursor.fetchone()
                return perna
            else:
                sql = 'SELECT * FROM Exercicios WHERE tp_treino="Perna"'
                cursor.execute(sql)
                pernas = cursor.fetchall()
                return pernas
        except:
            return None

    def listar_braco(self, codigo=None):
        try:
            cursor = self.con.cursor()
            if codigo != None:
                # pegar somente uma planta
                sql = 'SELECT * FROM Exercicios WHERE tp_treino="Braço"'
                cursor.execute(sql, (codigo,))
                braco = cursor.fetchone()
                return braco
            else:
                # pegar todas as plantas
                sql = 'SELECT * FROM Exercicios WHERE tp_treino="Braço"'
                cursor.execute(sql)
                bracos = cursor.fetchall()
                return bracos
        except:
            return None

    def listar_costas(self, codigo=None):
        try:
            cursor = self.con.cursor()
            if codigo != None:
                sql = 'SELECT * FROM Exercicios WHERE tp_treino="Costas"'
                cursor.execute(sql, (codigo,))
                costas = cursor.fetchone()
                return costas
            else:
                sql = 'SELECT * FROM Exercicios WHERE tp_treino="Costas"'
                cursor.execute(sql)
                costass = cursor.fetchall()
                return costass
        except:
            return None

    def listar_abdomen(self, codigo=None):
        try:
            cursor = self.con.cursor()
            if codigo != None:
                sql = 'SELECT * FROM Exercicios WHERE tp_treino="Abdome"'
                cursor.execute(sql, (codigo,))
                abdomen = cursor.fetchone()
                return abdomen
            else:
                sql = 'SELECT * FROM Exercicios WHERE tp_treino="Abdome"'
                cursor.execute(sql)
                abdomens = cursor.fetchall()
                return abdomens
        except:
            return None

    def listar_alongamento(self, codigo=None):
        try:
            cursor = self.con.cursor()
            if codigo != None:
                sql = 'SELECT * FROM Exercicios WHERE tp_treino="Alongamento"'
                cursor.execute(sql, (codigo,))
                alongamento = cursor.fetchone()
                return alongamento
            else:
                sql = 'SELECT * FROM Exercicios WHERE tp_treino="Alongamento"'
                cursor.execute(sql)
                alongamentos = cursor.fetchall()
                return alongamentos
        except:
            return None