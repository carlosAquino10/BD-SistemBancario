# Classe Conta
class Conta:
    def __init__(self, numero_conta, saldo, senha, banco, cliente):
        self.numero_conta = numero_conta
        self.saldo = int(saldo)
        self.senha = senha
        self.banco = banco
        self.cliente = cliente

    def consultar_saldo(self, senha):
        if senha != self.senha:
            print('Senha incorreta.')
            return None

        return self.saldo

    def depositar(self, valor, senha):
        if senha != self.senha:
            print('Senha incorreta.')
            return self.saldo, self.numero_conta

        if valor < 0:
            print('Você não pode depositar um valor negativo.')
            return None

        self.saldo += valor
        return self.saldo

    def sacar(self, valor, senha):
        if senha != self.senha:
            print('Senha incorreta.')
            return self.saldo

        if valor < 0:
            print('Você não pode sacar um valor negativo.')
            return self.saldo

        if valor > self.saldo:
            print('Saldo insuficiente.')
            return self.saldo

        self.saldo -= valor
        return self.saldo

    def transferir(self, valor, senha, conta_destino):
        print(f'Valor a transferir: {valor}')
        print(f'Senha: {senha}')
        print(f'Saldo inicial remetente: {self.saldo}')
        print(f'Saldo inicial destinatario: {conta_destino.saldo}')

        if senha != self.senha:
            print('Senha incorreta.')
            return self.saldo, self.numero_conta

        if valor < 0:
            print('Você não pode transferir um valor negativo.')
            return None

        if valor > self.saldo:
            print('Saldo insuficiente.')
            return self.saldo

        conta_destino.saldo += valor
        self.saldo -= valor

        print(f'Saldo final remetente: {self.saldo}')
        print(f'Saldo final destinatario: {conta_destino.saldo}')

        return self.saldo
        
    
