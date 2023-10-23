# Classe Cliente
class Cliente:
    def __init__(self, nome, senha, conta):
        self.nome = nome
        self.senha = senha
        self.conta = conta

    def salvar_no_banco(self):
        cursor.execute("INSERT INTO clientes_nubank (nome, senha, conta_numero) VALUES (:nome, :senha, :conta_numero)",
                       {'nome': self.nome, 'senha': self.senha, 'conta_numero': self.conta.numero_conta})
        conexao.commit()
