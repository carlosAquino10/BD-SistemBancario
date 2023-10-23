# Criando os bancos Nubank e BTG Pactual

nubank = Banco("Nubank")
btg_pactual = Banco("BTG Pactual")

# Menu Principal

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
            btg_pactual.clientes[numero_conta_btgpactual] = cliente_btgpactual #byMaciel
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
			#Atualizações feitas em 16/10/2023-byMaciel
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
			#Atualizações feitas em 16/10/2023-byMaciel
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
		        #Atualizações feitas em 16/10/2023-byMaciel
        conta_remetente = banco_remetente.get_conta(remetente)
        conta_destinatario = banco_destinatario.get_conta(destinatario)

        if conta_remetente is not None and conta_destinatario is not None:
            if senha == conta_remetente.senha:
                nome_remetente = conta_remetente.cliente.nome
                nome_destinatario = conta_destinatario.cliente.nome

                saldo_atual_remetente = conta_remetente.transferir(valor, senha, conta_destinatario)
                if saldo_atual_remetente is not None: #Atualizações feitas em 16/10/2023-byMaciel
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
                    print(f'Transferência DOC de R${valor} realizada com sucesso.') #Atualizações feitas em 16/10/2023-byMaciel
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

