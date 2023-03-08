from config.database import mydb

class Fornecedores:
    def listaFornecedor():
        cursor = mydb.cursor()
        cursor.execute("SELECT * FROM fornecedores")
        fornec = cursor.fetchall()
        return fornec
    
    def listaFornecedoresPorID(id):
        cursor = mydb.cursor()
        cursor.execute("SELECT * FROM fornecedores WHERE idFornec=%s", (id,))
        fornec = cursor.fetchone()
        return fornec
    
    def cadastraFornecedor(dados):
        cursor = mydb.cursor()
        cursor.execute("INSERT INTO fornecedores(nome, email, telefone, idUsuario) VALUES (%s, %s, %s, %s)", (dados["nome"], dados["email"], dados["telefone"], dados["id"]))
        fornec = mydb.commit()
        return fornec
    
    def atualizarFornecedor(dados):
        cursor = mydb.cursor()
        cursor.execute("UPDATE fornecedor SET nome=%s, email=$s, telefone=%s WHERE idFornec=%s", (dados["nome"], dados["email"], dados["telefone"], dados["idFornec"]))
        fornec = mydb.commit()
        return fornec
    
    def deletarFornecedor(id):
        cursor = mydb.cursor()
        cursor.execute("DELETE FROM fornecedor WHERE idFornec=%s", (id,))
        fornec = mydb.commit()
        return fornec