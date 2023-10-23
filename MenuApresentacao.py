import cx_Oracle

def conectar_banco():
    conexao = cx_Oracle.connect('seu_usuario/sua_senha@seu_host:seu_porta/seu_sid')
    return conexao

def contar_registros(tabela):
    conexao = conectar_banco()
    cursor = conexao.cursor()
    cursor.execute(f"SELECT COUNT(*) FROM {tabela}")
    total_registros = cursor.fetchone()[0]
    cursor.close()
    conexao.close()
    return total_registros

def exibir_splash_screen():
    print("Bem-vindo ao Sistema de Relatórios CRUD")
    print("Desenvolvido por: [Nome 1], [Nome 2], [Nome 3]")
    print("=" * 40)

def exibir_menu():
    print("\nMENU:")
    print("1. Relatórios")
    print("2. Inserir Registros")
    print("3. Remover Registros")
    print("4. Atualizar Registros")
    print("5. Sair")

def exibir_relatorios():
    total_clientes_nubank = contar_registros("clientes_nubank")
    total_clientes_btgpactual = contar_registros("clientes_btgpactual")
    total_transferencias_pix_nubank = contar_registros("transferencias_pix_nubank")
    total_transferencias_pix_btgpactual = contar_registros("transferencias_pix_btgpactual")

    print(f"\nRelatórios:")
    print(f"Total de Clientes no Nubank: {total_clientes_nubank}")
    print(f"Total de Clientes no BTG Pactual: {total_clientes_btgpactual}")
    print(f"Total de Transferências PIX no Nubank: {total_transferencias_pix_nubank}")
    print(f"Total de Transferências PIX no BTG Pactual: {total_transferencias_pix_btgpactual}")

def inserir_registros():
    # Implementar a inserção de registros no banco de dados
    pass

def remover_registros():
    # Implementar a remoção de registros no banco de dados
    pass

def atualizar_registros():
    # Implementar a atualização de registros no banco de dados
    pass

def main():
    exibir_splash_screen()
    while True:
        exibir_menu()
        escolha = input("Escolha a opção (1-5): ")

        if escolha == "1":
            exibir_relatorios()
        elif escolha == "2":
            inserir_registros()
        elif escolha == "3":
            remover_registros()
        elif escolha == "4":
            atualizar_registros()
        elif escolha == "5":
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()

