import cx_Oracle
import tkinter as tk
from tkinter import messagebox
# Outras importações necessárias

def conectar_banco():
    try:
        connection = cx_Oracle.connect('seu_usuario/sua_senha@localhost:1521/seu_sid')
        return connection
    except cx_Oracle.Error as error:
        messagebox.showerror("Erro de Conexão", f"Erro ao conectar ao banco de dados: {error}")
        return None

def realizar_insercao(connection, dados):
    try:
        cursor = connection.cursor()

        # Execute sua instrução de inserção aqui
        # Exemplo: cursor.execute("INSERT INTO tabela (coluna1, coluna2) VALUES (:valor1, :valor2)", valor1=dados[0], valor2=dados[1])

        connection.commit()
        cursor.close()
        messagebox.showinfo("Sucesso", "Inserção realizada com sucesso!")
    except cx_Oracle.Error as error:
        messagebox.showerror("Erro ao Inserir", f"Erro ao inserir dados: {error}")

def realizar_remocao(connection, id):
    try:
        cursor = connection.cursor()

        # Execute sua instrução de remoção aqui
        # Exemplo: cursor.execute("DELETE FROM tabela WHERE id = :id", id=id)

        connection.commit()
        cursor.close()
        messagebox.showinfo("Sucesso", "Remoção realizada com sucesso!")
    except cx_Oracle.Error as error:
        messagebox.showerror("Erro ao Remover", f"Erro ao remover dados: {error}")

def realizar_atualizacao(connection, id, novos_dados):
    try:
        cursor = connection.cursor()

        # Execute sua instrução de atualização aqui
        # Exemplo: cursor.execute("UPDATE tabela SET coluna1 = :valor1, coluna2 = :valor2 WHERE id = :id", valor1=novos_dados[0], valor2=novos_dados[1], id=id)

        connection.commit()
        cursor.close()
        messagebox.showinfo("Sucesso", "Atualização realizada com sucesso!")
    except cx_Oracle.Error as error:
        messagebox.showerror("Erro ao Atualizar", f"Erro ao atualizar dados: {error}")

def realizar_consulta(connection, query):
    try:
        cursor = connection.cursor()

        # Execute sua instrução de consulta aqui
        # Exemplo: cursor.execute(query)

        resultado = cursor.fetchall()
        cursor.close()
        return resultado
    except cx_Oracle.Error as error:
        messagebox.showerror("Erro ao Consultar", f"Erro ao consultar dados: {error}")

def exibir_menu_principal():
    root = tk.Tk()
    root.title("Menu Principal")
    root.geometry("400x300")

    label = tk.Label(root, text="Menu Principal", font=("Helvetica", 20))
    label.pack(pady=20)

    # Botões para acessar os submenus
    button_relatorios = tk.Button(root, text="Relatórios", command=exibir_submenu_relatorios)
    button_relatorios.pack()

    button_inserir = tk.Button(root, text="Inserir Registros", command=exibir_submenu_inserir)
    button_inserir.pack()

    button_remover = tk.Button(root, text="Remover Registros", command=exibir_submenu_remover)
    button_remover.pack()

    button_atualizar = tk.Button(root, text="Atualizar Registros", command=exibir_submenu_atualizar)
    button_atualizar.pack()

    button_sair = tk.Button(root, text="Sair", command=root.quit)
    button_sair.pack(pady=20)

    root.mainloop()

def exibir_submenu_relatorios():
    root = tk.Tk()
    root.title("Submenu de Relatórios")
    root.geometry("400x300")

    label = tk.Label(root, text="Relatórios", font=("Helvetica", 20))
    label.pack(pady=20)

    # 1. Conectar ao banco de dados Oracle (utilize a função conectar_ao_banco)
    connection = conectar_ao_banco()

    # 2. Realizar consultas SQL para obter os dados desejados
    relatorio_pix = realizar_consulta(connection, "SELECT COUNT(*) FROM Transacoes WHERE tipo = 'PIX';")
    relatorio_clientes = realizar_consulta(connection, "SELECT COUNT(*) FROM Clientes;")

    # 3. Exibir os resultados na interface gráfica
    tk.Label(root, text=f"Quantidade de Transações PIX: {relatorio_pix[0][0]}").pack()
    tk.Label(root, text=f"Quantidade de Clientes Cadastrados: {relatorio_clientes[0][0]}").pack()

    # 4. Desconectar do banco de dados
    desconectar_do_banco(connection)

    button_voltar = tk.Button(root, text="Voltar", command=root.quit)
    button_voltar.pack(pady=20)

    root.mainloop()


def exibir_submenu_inserir():
    root = tk.Tk()
    root.title("Submenu de Inserção")
    root.geometry("400x300")

    label = tk.Label(root, text="Inserir Registros", font=("Helvetica", 20))
    label.pack(pady=20)

    # Lógica para inserção de registros
    # Exemplo: Inserir um novo cliente
    
    # 1. Conectar ao banco de dados Oracle (utilize a função conectar_ao_banco)
    connection = conectar_ao_banco()

    # 2. Coletar os dados do novo cliente do usuário (utilize widgets como Entry)
    tk.Label(root, text="Nome:").pack()
    entry_nome = tk.Entry(root)
    entry_nome.pack()

    tk.Label(root, text="CPF:").pack()
    entry_cpf = tk.Entry(root)
    entry_cpf.pack()


    # 3. Criar um botão para enviar os dados e realizar a inserção
    def inserir_cliente():
        nome = entry_nome.get()
        cpf = entry_cpf.get()

        # 4. Realizar a inserção no banco de dados
        realizar_insercao(connection, ("Clientes", ["Nome", "CPF"], [nome, cpf]))

        # 5. Informar ao usuário que a inserção foi realizada com sucesso
        tk.Label(root, text="Cliente inserido com sucesso!").pack()

    button_inserir = tk.Button(root, text="Inserir Cliente", command=inserir_cliente)
    button_inserir.pack(pady=20)

    # 6. Desconectar do banco de dados
    desconectar_do_banco(connection)

    button_voltar = tk.Button(root, text="Voltar", command=root.quit)
    button_voltar.pack(pady=20)

    root.mainloop()


def exibir_submenu_remover():
    root = tk.Tk()
    root.title("Submenu de Remoção")
    root.geometry("400x300")

    label = tk.Label(root, text="Remover Registros", font=("Helvetica", 20))
    label.pack(pady=20)

    # Lógica para remoção de registros
    # Exemplo: Remover um cliente
    
    # 1. Conectar ao banco de dados Oracle (utilize a função conectar_ao_banco)
    connection = conectar_ao_banco()

    # 2. Exibir os registros disponíveis para o usuário selecionar
    registros = realizar_consulta(connection, "SELECT * FROM Clientes;")

    tk.Label(root, text="Selecione um cliente para remover:").pack()

    for registro in registros:
        tk.Radiobutton(root, text=registro[1], variable=registro[0]).pack()

    # 3. Criar um botão para confirmar a remoção
    def remover_cliente():
        cliente_selecionado = tk.StringVar().get()

        # 4. Realizar a remoção no banco de dados
        realizar_remocao(connection, cliente_selecionado)

        # 5. Informar ao usuário que a remoção foi realizada com sucesso
        tk.Label(root, text="Cliente removido com sucesso!").pack()

    button_remover = tk.Button(root, text="Remover Cliente", command=remover_cliente)
    button_remover.pack(pady=20)

    # 6. Desconectar do banco de dados
    desconectar_do_banco(connection)

    button_voltar = tk.Button(root, text="Voltar", command=root.quit)
    button_voltar.pack(pady=20)

    root.mainloop()


def exibir_submenu_atualizar():
    root = tk.Tk()
    root.title("Submenu de Atualização")
    root.geometry("400x300")

    label = tk.Label(root, text="Atualizar Registros", font=("Helvetica", 20))
    label.pack(pady=20)

    # Lógica para atualização de registros
    # Exemplo: Atualizar o nome de um cliente
    
    # 1. Conectar ao banco de dados Oracle (utilize a função conectar_ao_banco)
    connection = conectar_ao_banco()

    # 2. Exibir os registros disponíveis para o usuário selecionar
    registros = realizar_consulta(connection, "SELECT * FROM Clientes;")

    tk.Label(root, text="Selecione um cliente para atualizar:").pack()

    for registro in registros:
        tk.Radiobutton(root, text=registro[1], variable=registro[0]).pack()

    tk.Label(root, text="Novo Nome:").pack()
    entry_nome = tk.Entry(root)
    entry_nome.pack()

    # 3. Criar um botão para confirmar a atualização
    def atualizar_cliente():
        cliente_selecionado = tk.StringVar().get()
        novo_nome = entry_nome.get()

        # 4. Realizar a atualização no banco de dados
        realizar_atualizacao(connection, cliente_selecionado, {"Nome": novo_nome})

        # 5. Informar ao usuário que a atualização foi realizada com sucesso
        tk.Label(root, text="Cliente atualizado com sucesso!").pack()

    button_atualizar = tk.Button(root, text="Atualizar Cliente", command=atualizar_cliente)
    button_atualizar.pack(pady=20)

    # 6. Desconectar do banco de dados
    desconectar_do_banco(connection)

    button_voltar = tk.Button(root, text="Voltar", command=root.quit)
    button_voltar.pack(pady=20)

    root.mainloop()


def exibir_submenu_inserir():
    root = tk.Tk()
    root.title("Submenu de Inserção")
    root.geometry("400x300")

    label = tk.Label(root, text="Inserir Registros", font=("Helvetica", 20))
    label.pack(pady=20)

    # Implemente a lógica para inserir registros aqui

    button_voltar = tk.Button(root, text="Voltar", command=root.quit)
    button_voltar.pack(pady=20)

    root.mainloop()

def exibir_submenu_remover():
    root = tk.Tk()
    root.title("Submenu de Remoção")
    root.geometry("400x300")

    label = tk.Label(root, text="Remover Registros", font=("Helvetica", 20))
    label.pack(pady=20)

    # Implemente a lógica para remover registros aqui

    button_voltar = tk.Button(root, text="Voltar", command=root.quit)
    button_voltar.pack(pady=20)

    root.mainloop()

def exibir_submenu_atualizar():
    root = tk.Tk()
    root.title("Submenu de Atualização")
    root.geometry("400x300")

    label = tk.Label(root, text="Atualizar Registros", font=("Helvetica", 20))
    label.pack(pady=20)

    # Implemente a lógica para atualizar registros aqui

    button_voltar = tk.Button(root, text="Voltar", command=root.quit)
    button_voltar.pack(pady=20)

    root.mainloop()
