# Classe Banco
class Banco:
    def __init__(self, nome):
        self.nome = nome
        self.contas = {}
        self.clientes = {}
        self.proximo_numero_conta = 1

    # Métodos do banco...

    def abrir_conta(self, nome, saldo_inicial, senha, escolha_banco):
        numero_conta = self.proximo_numero_conta#byMaciel
        novo_cliente = Cliente(nome, senha, None)  # Cliente criado sem associação a uma conta
        nova_conta = Conta(numero_conta, saldo_inicial, senha, escolha_banco, novo_cliente)
        novo_cliente.conta = nova_conta  # Agora o cliente está associado à conta
        self.contas[numero_conta] = nova_conta
        self.clientes[numero_conta] = novo_cliente
        self.proximo_numero_conta += 1
        return numero_conta, self.nome, escolha_banco

    # Métodos de manipulação de contas e clientes aqui...

    def consultar_saldo(self, numero_conta, senha):
        conta = self.get_conta(numero_conta)
        if conta is not None:
            if senha == conta.senha:
                return conta.saldo
            else:
                print('Senha incorreta. Não é possível consultar o saldo.')
        else:
            print('Conta não encontrada. Não é possível consultar o saldo.')

    def depositar(self, numero_conta, valor, senha):
        conta = self.contas.get(numero_conta)

        if conta is not None:
            saldo_atual = conta.depositar(valor, senha)
            if saldo_atual is not None:
                return saldo_atual, numero_conta
        else:
            print('Número de conta inválido.')

    def mostrar_clientes(self):
      for numero_conta, cliente in self.clientes.items():
        conta = cliente.conta
        print(f"Número da Conta: {numero_conta}, Cliente: {cliente.nome}, Saldo: R${conta.consultar_saldo(cliente.senha)}, Banco: {self.nome}")

    def get_conta(self, numero_conta):
        return self.contas.get(numero_conta)

    def fechar_conta(self, numero_conta, senha):
        conta = self.contas.get(numero_conta)

        if conta is not None:
            if senha == conta.senha:
                del self.contas[numero_conta]
                del self.clientes[numero_conta]

                # Atualizar a lista de clientes
                self.mostrar_clientes()

                print('Conta fechada com sucesso.')
            else:
                print('Senha incorreta.')
        else:
            print('Número de conta inválido.')

    def sacar(self, numero_conta, valor, senha):
        conta = self.contas.get(numero_conta)

        if conta is not None:
            saldo_atual = conta.sacar(valor, senha)
            if saldo_atual is not None:
                print(f'Saque de R${valor} realizado. Novo saldo: R${saldo_atual}')
        else:
            print('Número de conta inválido.')

    def consultar_cliente(self, numero_conta, senha):
        cliente = self.clientes.get(numero_conta)
        if cliente is not None:
            if senha == cliente.senha:
                return cliente.conta.consultar_saldo(senha)
            else:
                print('Senha incorreta.')
        else:
            print('Número de conta inválido.')

    def transferencia_pix(self, remetente, destinatario, valor, senha):
        conta_remetente = self.get_conta(remetente)
        conta_destinatario = self.get_conta(destinatario)

        if conta_remetente is not None and conta_destinatario is not None:
            if senha == conta_remetente.senha:
                if valor > 0 and valor <= conta_remetente.saldo:
                    saldo_atual = conta_remetente.transferir(valor, senha, conta_destinatario)

                    nome_remetente = conta_remetente.cliente.nome
                    nome_destinatario = conta_destinatario.cliente.nome

                    print(f'Transferência PIX de R${valor} realizada com sucesso.')
                    print(f'Novo saldo do remetente ({conta_remetente.banco}): R${saldo_atual} - Cliente: {nome_remetente}')
                    print(f'Novo saldo do destinatário ({conta_destinatario.banco}): R${conta_destinatario.saldo} - Cliente: {nome_destinatario}')
                else:
                    print('Valor inválido ou saldo insuficiente.')
            else:
                print('Senha incorreta. Transação não efetuada.')
        else:
            print('Conta(s) inválida(s).')

    def transferencia_ted(self, valor, senha, conta_destino):
        print(f'Valor a transferir: {valor}')
        print(f'Senha: {senha}')
        print(f'Saldo inicial remetente: {self.saldo}')
        print(f'Saldo inicial destinatario: {conta_destino.saldo}')

        if senha != self.senha:
            print('Senha incorreta.')
            return self.saldo

        if valor < 0:
            print('Você não pode transferir um valor negativo.')
            return self.saldo

        if valor > self.saldo:
            print('Saldo insuficiente.')
            return self.saldo

        conta_destino.saldo += valor
        self.saldo -= valor

        print(f'Saldo final remetente: {self.saldo}')
        print(f'Saldo final destinatario: {conta_destino.saldo}')

        return self.saldo

    def transferencia_doc(self, remetente, destinatario, valor, senha):
        print(f'Valor a transferir: {valor}')
        print(f'Senha: {senha}')
        conta_remetente = self.get_conta(remetente)
        conta_destinatario = self.get_conta(destinatario)

        if senha != conta_remetente.senha:
            print('Senha incorreta.')
            return self.saldo, self.numero_conta

        if valor < 0:
            print('Você não pode transferir um valor negativo.')
            return None

        if valor > conta_remetente.saldo:
            print('Saldo insuficiente.')
            return conta_remetente.saldo

        print(f'Antes da transferência - Saldo remetente: {conta_remetente.saldo}, Saldo destinatario: {conta_destinatario.saldo}')

        conta_destinatario.saldo += valor
        conta_remetente.saldo -= valor

        print(f'Depois da transferência - Saldo remetente: {conta_remetente.saldo}, Saldo destinatario: {conta_destinatario.saldo}')

        return conta_remetente.saldo


    def transferencia_pix(self, remetente, destinatario, valor, senha):
        # Implementação da transferência PIX aqui...
        pass

    def transferencia_ted(self, remetente, destinatario, valor, senha):
        # Implementação da transferência TED aqui...
        pass

    def transferencia_doc(self, remetente, destinatario, valor, senha):
        # Implementação da transferência DOC aqui...
        pass

    def limpar_contas(self):
        self.contas = {}
        self.clientes = {}
        self.proximo_numero_conta = 1

        # Criando o cliente e salvando no banco de dados
        novo_cliente = Cliente(nome, senha, nova_conta)
        novo_cliente.salvar_no_banco()
