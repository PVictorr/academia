class UsuarioDAO():
    def __init__(self,con):
        self.con = con

    def inserir(self, usuario):
        try:
            sql = "INSERT INTO usuario (nome,email,senha,objetivo) VALUES( %s, %s, %s, %s)"

            cursor = self.con.cursor()
            cursor.execute(sql, (usuario.nome, usuario.email, usuario.senha, usuario.objetivo))

            self.con.commit()
            #codigo = cursor.lastrowid
            return 1
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