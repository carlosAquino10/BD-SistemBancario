class Cliente:
    def __init__(self, nome, senha, conta):
        self.nome = nome
        self.senha = senha
        self.conta = conta

class Conta:
    def __init__(self, numero_conta, saldo, senha, banco, cliente):
        self.numero_conta = numero_conta
        self.saldo = int(saldo)
        self.senha = senha
        self.banco = banco
        self.cliente = cliente  # Adicionando o cliente à conta

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


class Banco:

    def __init__(self, nome):
        self.nome = nome
        self.contas = {}
        self.clientes = {}
        self.proximo_numero_conta = 1

    def abrir_conta(self, nome, saldo_inicial, senha, escolha_banco):
        numero_conta = self.proximo_numero_conta
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

# Criando os bancos Nubank e BTG Pactual
nubank = Banco("Nubank")
btg_pactual = Banco("BTG Pactual")

while True:
    print()
    print('Selecione a operação que deseja realizar:')
    print('1 - Abrir Nova Conta')
    print('2 - Consultar Saldo')
    print('3 - Fechar Conta')
    print('4 - Realizar Depósito')
    print('5 - Realizar Saque')
    print('6 - Transferência PIX')
    print('7 - Transferência TED')
    print('8 - Transferência DOC')
    print('9 - Mostrar Clientes')
    print('10 - Limpar Todas as Contas')
    print('0 - Sair do Programa')

    escolha = input('Opção: ')

    if escolha == '1':
        nome = input('Informe seu nome: ')
        saldo = input('Informe o saldo inicial: ')
        saldo = int(saldo)  # Convertendo a entrada para inteiro
        senha = input('Escolha uma senha: ')

        print('Escolha o banco:')
        print('1 - Nubank')
        print('2 - BTG Pactual')
        escolha_banco = input('Opção: ')

        if escolha_banco == '1':
            numero_conta_nubank, nome_banco_nubank, escolha_banco_nubank = nubank.abrir_conta(nome, saldo, senha, "Nubank")
            cliente_nubank = Cliente(nome, senha, nubank.get_conta(numero_conta_nubank))
            nubank.clientes[numero_conta_nubank] = cliente_nubank
            print(f'Conta criada com sucesso no banco {nome_banco_nubank}! Seu número de conta é: {numero_conta_nubank}, Banco: {escolha_banco_nubank}')

        elif escolha_banco == '2':
            numero_conta_btgpactual, nome_banco_btgpactual, escolha_banco_btgpactual = btg_pactual.abrir_conta(nome, saldo, senha, "BTG Pactual")
            cliente_btgpactual = Cliente(nome, senha, btg_pactual.get_conta(numero_conta_btgpactual))
            btg_pactual.clientes[numero_conta_btgpactual] = cliente_btgpactual
            print(f'Conta criada com sucesso no banco {nome_banco_btgpactual}! Seu número de conta é: {numero_conta_btgpactual}, Banco: {escolha_banco_btgpactual}')

    elif escolha == '2':
        print('Escolha o banco:')
        print('1 - Nubank')
        print('2 - BTG Pactual')
        escolha_banco = input('Opção: ')

        if escolha_banco == '1':
            numero_conta = int(input('Por favor, insira o número da sua conta no Nubank: '))
            senha = input('Por favor, insira a senha: ')
            saldo = nubank.consultar_saldo(numero_conta, senha)
            if saldo is not None:
                print(f'Seu saldo no Nubank é: R${saldo}')

        elif escolha_banco == '2':
            numero_conta = int(input('Por favor, insira o número da sua conta no BTG Pactual: '))
            senha = input('Por favor, insira a senha: ')
            saldo = btg_pactual.consultar_saldo(numero_conta, senha)
            if saldo is not None:
                print(f'Seu saldo no BTG Pactual é: R${saldo}')

        else:
            print('Opção de banco inválida.')


    elif escolha == '3':
        numero_conta = int(input('Por favor, insira o número da sua conta: '))
        senha = input('Por favor, insira a senha: ')

        conta_nubank = nubank.get_conta(numero_conta)
        conta_btgpactual = btg_pactual.get_conta(numero_conta)

        if conta_nubank is not None:
            nubank.fechar_conta(numero_conta, senha)
        elif conta_btgpactual is not None:
            btg_pactual.fechar_conta(numero_conta, senha)
        else:
            print('Número de conta inválido.')

    elif escolha == '4':
        print('Escolha o banco:')
        print('1 - Nubank')
        print('2 - BTG Pactual')
        escolha_banco = input('Opção: ')
        numero_conta = int(input('Por favor, insira o número da sua conta: '))
        valor = float(input('Informe o valor do depósito: '))
        senha = input('Por favor, insira a senha: ')

        if escolha_banco == '1':
            conta_nubank = nubank.get_conta(numero_conta)
            if conta_nubank is not None:
                saldo_atual, numero_conta = nubank.depositar(numero_conta, valor, senha)
                print(f'Depósito de R${valor} realizado no Nubank. Novo saldo da Conta {numero_conta}: R${saldo_atual}')
            else:
                print('Número de conta inválido.')

        elif escolha_banco == '2':
            conta_btgpactual = btg_pactual.get_conta(numero_conta)
            if conta_btgpactual is not None:
                saldo_atual, numero_conta = btg_pactual.depositar(numero_conta, valor, senha)
                print(f'Depósito de R${valor} realizado no BTG Pactual. Novo saldo da Conta {numero_conta}: R${saldo_atual}')
            else:
                print('Número de conta inválido.')
        else:
            print('Opção de banco inválida.')

    elif escolha == '5':
        numero_conta = int(input('Por favor, insira o número da sua conta: '))
        senha = input('Por favor, insira a senha: ')
        print('Escolha o banco:')
        print('1 - Nubank')
        print('2 - BTG Pactual')
        escolha_banco = input('Opção: ')

        if escolha_banco == '1':
            conta = nubank.get_conta(numero_conta)
        elif escolha_banco == '2':
            conta = btg_pactual.get_conta(numero_conta)
        else:
            print('Opção inválida. Tente novamente.')
            continue

        if conta is not None:
            valor = float(input('Informe o valor do saque: '))

            saldo_atual = conta.sacar(valor, senha)
            if saldo_atual is not None:
                print(f'Saque de R${valor} realizado. Novo saldo: R${saldo_atual}')
        else:
            print('Número de conta inválido.')

    elif escolha == '6':
        print('Escolha o banco do remetente:')
        print('1 - Nubank')
        print('2 - BTG Pactual')
        escolha_banco_remetente = input('Opção: ')
        if escolha_banco_remetente == '1':
            banco_remetente = nubank
        elif escolha_banco_remetente == '2':
            banco_remetente = btg_pactual
        else:
            print('Opção inválida. Tente novamente.')
            continue

        print(f'Por favor, insira o número da conta do remetente ({banco_remetente.nome}): ')
        remetente = int(input())

        print('Escolha o banco do destinatário:')
        print('1 - Nubank')
        print('2 - BTG Pactual')
        escolha_banco_destinatario = input('Opção: ')
        if escolha_banco_destinatario == '1':
            banco_destinatario = nubank
        elif escolha_banco_destinatario == '2':
            banco_destinatario = btg_pactual
        else:
            print('Opção inválida. Tente novamente.')
            continue

        print(f'Por favor, insira o número da conta do destinatário ({banco_destinatario.nome}): ')
        destinatario = int(input())

        valor = float(input('Informe o valor da transferência: '))
        senha = input('Por favor, insira a senha: ')

        conta_remetente = banco_remetente.get_conta(remetente)
        conta_destinatario = banco_destinatario.get_conta(destinatario)

        if conta_remetente is not None and conta_destinatario is not None:
            if senha == conta_remetente.senha:
                nome_remetente = conta_remetente.cliente.nome
                nome_destinatario = conta_destinatario.cliente.nome

                saldo_atual_remetente = conta_remetente.transferir(valor, senha, conta_destinatario)
                if saldo_atual_remetente is not None:
                    print(f'Transferência de R${valor} realizada com sucesso.')
                    print(f'Novo saldo do remetente ({banco_remetente.nome}): R${saldo_atual_remetente} - Cliente: {nome_remetente}')
                    print(f'Novo saldo do destinatário ({banco_destinatario.nome}): R${conta_destinatario.saldo} - Cliente: {nome_destinatario}')
            else:
                print('Senha incorreta. Transação não efetuada.')
        else:
            print('Conta(s) inválida(s).')

    elif escolha == '7':
        print('Escolha o banco do remetente:')
        print('1 - Nubank')
        print('2 - BTG Pactual')
        escolha_banco_remetente = input('Opção: ')

        if escolha_banco_remetente == '1':
            banco_remetente = nubank
        elif escolha_banco_remetente == '2':
            banco_remetente = btg_pactual
        else:
            print('Opção inválida. Tente novamente.')
            continue

        print(f'Por favor, insira o número da conta do remetente ({banco_remetente.nome}): ')
        remetente = int(input())

        print('Escolha o banco do destinatário:')
        print('1 - Nubank')
        print('2 - BTG Pactual')
        escolha_banco_destinatario = input('Opção: ')

        if escolha_banco_destinatario == '1':
            banco_destinatario = nubank
        elif escolha_banco_destinatario == '2':
            banco_destinatario = btg_pactual
        else:
            print('Opção inválida. Tente novamente.')
            continue

        print(f'Por favor, insira o número da conta do destinatário ({banco_destinatario.nome}): ')
        destinatario = int(input())

        valor = float(input('Informe o valor da transferência: '))
        senha = input('Por favor, insira a senha: ')

        conta_remetente = banco_remetente.get_conta(remetente)
        conta_destinatario = banco_destinatario.get_conta(destinatario)

        if conta_remetente is not None and conta_destinatario is not None:
            if senha == conta_remetente.senha:
                nome_remetente = conta_remetente.cliente.nome
                nome_destinatario = conta_destinatario.cliente.nome

                saldo_atual_remetente = conta_remetente.transferir(valor, senha, conta_destinatario)
                if saldo_atual_remetente is not None:
                    print(f'Transferência TED de R${valor} realizada com sucesso.')
                    print(f'Novo saldo do remetente ({banco_remetente.nome}): R${saldo_atual_remetente} - Cliente: {nome_remetente}')
                    print(f'Novo saldo do destinatário ({banco_destinatario.nome}): R${conta_destinatario.saldo} - Cliente: {nome_destinatario}')
            else:
                print('Senha incorreta. Transação não efetuada.')
        else:
            print('Conta(s) inválida(s).')

    elif escolha == '8':
        print('Escolha o banco do remetente:')
        print('1 - Nubank')
        print('2 - BTG Pactual')
        escolha_banco_remetente = input('Opção: ')

        if escolha_banco_remetente == '1':
            banco_remetente = nubank
        elif escolha_banco_remetente == '2':
            banco_remetente = btg_pactual
        else:
            print('Opção inválida. Tente novamente.')
            continue

        print(f'Por favor, insira o número da conta do remetente ({banco_remetente.nome}): ')
        remetente = int(input())

        print('Escolha o banco do destinatário:')
        print('1 - Nubank')
        print('2 - BTG Pactual')
        escolha_banco_destinatario = input('Opção: ')

        if escolha_banco_destinatario == '1':
            banco_destinatario = nubank
        elif escolha_banco_destinatario == '2':
            banco_destinatario = btg_pactual
        else:
            print('Opção inválida. Tente novamente.')
            continue

        print(f'Por favor, insira o número da conta do destinatário ({banco_destinatario.nome}): ')
        destinatario = int(input())

        valor = float(input('Informe o valor da transferência: '))
        senha = input('Por favor, insira a senha: ')

        conta_remetente = banco_remetente.get_conta(remetente)
        conta_destinatario = banco_destinatario.get_conta(destinatario)

        if conta_remetente is not None and conta_destinatario is not None:
            if senha == conta_remetente.senha:
                nome_remetente = conta_remetente.cliente.nome
                nome_destinatario = conta_destinatario.cliente.nome

                saldo_atual_remetente = conta_remetente.transferir(valor, senha, conta_destinatario)
                if saldo_atual_remetente is not None:
                    print(f'Transferência DOC de R${valor} realizada com sucesso.')
                    print(f'Novo saldo do remetente ({banco_remetente.nome}): R${saldo_atual_remetente} - Cliente: {nome_remetente}')
                    print(f'Novo saldo do destinatário ({banco_destinatario.nome}): R${conta_destinatario.saldo} - Cliente: {nome_destinatario}')
            else:
                print('Senha incorreta. Transação não efetuada.')
        else:
            print('Conta(s) inválida(s).')

    elif escolha == '9':
        print('Clientes do Nubank:')
        nubank.mostrar_clientes()
        print('\nClientes do BTG Pactual:')
        btg_pactual.mostrar_clientes()

    elif escolha == '10':
        print('Escolha o banco:')
        print('1 - Nubank')
        print('2 - BTG Pactual')
        escolha_banco = input('Opção: ')

        if escolha_banco == '1':
            nubank.limpar_contas()
            print('Todas as contas do Nubank foram excluídas.')

        elif escolha_banco == '2':
            btg_pactual.limpar_contas()
            print('Todas as contas do BTG Pactual foram excluídas.')

        else:
            print('Opção de banco inválida.')

    elif escolha == '0':
        break

print('Fim')
# Loop de interação com o usuário aqui...
