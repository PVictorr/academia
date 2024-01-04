class UsuarioDAO():
    def __init__(self,con):
        self.con = con

    def inserir(self, usuario):
        try:
            sql = "INSERT INTO Usuario(nome, sobrenome, email, senha) VALUES(%s, %s, %s, %s)"

            cursor = self.con.cursor()
            cursor.execute(sql, (usuario.nome, usuario.sobrenome, usuario.email, usuario.senha,))
            self.con.commit()
            codigo = cursor.lastrowid
            return codigo
        except:
            return 0


    def autenticar(self, email, senha):
        try:
            sql = "SELECT * FROM Usuario WHERE email=%s AND senha=%s"
            cursor = self.con.cursor()
            cursor.execute(sql,(email, senha))
            usuario = cursor.fetchone()
            return usuario
        except:
            return None

    def obter(self, email):
        sql = "SELECT * FROM Usuario WHERE email=%s"

        cursor = self.con.cursor()
        cursor.execute(sql, (email,))

        return cursor.fetchone()