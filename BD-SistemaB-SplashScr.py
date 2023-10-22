import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import cx_Oracle

# Função para conectar ao banco de dados Oracle
def conectar_ao_banco():
    connection = cx_Oracle.connect("seu_usuario/sua_senha@localhost:1521/seu_sid")
    return connection

# Função para desconectar do banco de dados Oracle
def desconectar_do_banco(connection):
    connection.close()

# Função para realizar inserção de dados
def realizar_insercao(connection, tabela, atributos, valores):
    cursor = connection.cursor()
    cursor.execute(f"INSERT INTO {tabela} ({','.join(atributos)}) VALUES ({','.join([':1' for _ in valores])})", valores)
    connection.commit()
    cursor.close()

# Função para realizar remoção de dados
def realizar_remocao(connection, tabela, chave_primaria, valor_chave_primaria):
    cursor = connection.cursor()
    cursor.execute(f"DELETE FROM {tabela} WHERE {chave_primaria} = :1", (valor_chave_primaria,))
    connection.commit()
    cursor.close()

# Função para realizar atualização de dados
def realizar_atualizacao(connection, tabela, novos_valores, chave_primaria, valor_chave_primaria):
    sets = ', '.join([f'{atributo} = :{i+1}' for i, atributo in enumerate(novos_valores.keys())])
    cursor = connection.cursor()
    cursor.execute(f"UPDATE {tabela} SET {sets} WHERE {chave_primaria} = :{len(novos_valores) + 1}",
                   (*novos_valores.values(), valor_chave_primaria))
    connection.commit()
    cursor.close()

# Função para realizar consulta de dados
def realizar_consulta(connection, query):
    cursor = connection.cursor()
    cursor.execute(query)
    result = cursor.fetchall()
    cursor.close()
    return result

# Submenu de Relatórios
def exibir_submenu_relatorios():
    root = tk.Tk()
    root.title("Submenu de Relatórios")
    root.geometry("400x300")

    label = tk.Label(root, text="Relatórios", font=("Helvetica", 20))
    label.pack(pady=20)

    # Lógica para exibir os relatórios
    # Exemplo: Relatório de transações PIX e quantidade de clientes cadastrados

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

# Submenu de Inserção
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
        realizar_insercao(connection, "Clientes", ["Nome", "CPF"], [nome, cpf])

        # 5. Informar ao usuário que a inserção foi realizada com sucesso
        messagebox.showinfo("Sucesso", "Cliente inserido com sucesso!")

        # 6. Limpar os campos após a inserção
        entry_nome.delete(0, tk.END)
        entry_cpf.delete(0, tk.END)

    button_inserir = tk.Button(root, text="Inserir Cliente", command=inserir_cliente)
    button_inserir.pack(pady=20)

    # 7. Desconectar do banco de dados
    desconectar_do_banco(connection)

    button_voltar = tk.Button(root, text="Voltar", command=root.quit)
    button_voltar.pack(pady=20)

    root.mainloop()

# Submenu de Remoção
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

    # 2. Exibir os registros disponíveis para remoção (pode ser em uma Listbox ou Treeview)
    registros = realizar_consulta(connection, "SELECT * FROM Clientes;")
    listbox = tk.Listbox(root)
    for registro in registros:
        listbox.insert(tk.END, f"ID: {registro[0]}, Nome: {registro[1]}, CPF: {registro[2]}")
    listbox.pack()

    # 3. Criar um botão para remover o registro selecionado
    def remover_cliente():
        # 4. Obter o ID do cliente selecionado (é possível separar o ID do resto do texto)
        selected_item = listbox.get(listbox.curselection())
        id_cliente = int(selected_item.split(":")[1].split(",")[0])

        # 5. Realizar a remoção no banco de dados
        realizar_remocao(connection, "Clientes", "ID", id_cliente)

        # 6. Informar ao usuário que a remoção foi realizada com sucesso
        messagebox.showinfo("Sucesso", "Cliente removido com sucesso!")

        # 7. Atualizar a lista de registros após a remoção
        listbox.delete(0, tk.END)
        registros_atualizados = realizar_consulta(connection, "SELECT * FROM Clientes;")
        for registro in registros_atualizados:
            listbox.insert(tk.END, f"ID: {registro[0]}, Nome: {registro[1]}, CPF: {registro[2]}")

    button_remover = tk.Button(root, text="Remover Cliente", command=remover_cliente)
    button_remover.pack(pady=20)

    # 8. Desconectar do banco de dados
    desconectar_do_banco(connection)

    button_voltar = tk.Button(root, text="Voltar", command=root.quit)
    button_voltar.pack(pady=20)

    root.mainloop()

# Submenu de Atualização
def exibir_submenu_atualizar():
    root = tk.Tk()
    root.title("Submenu de Atualização")
    root.geometry("400x300")

    label = tk.Label(root, text="Atualizar Registros", font=("Helvetica", 20))
    label.pack(pady=20)

    # Lógica para atualização de registros
    # Exemplo: Atualizar os dados de um cliente

    # 1. Conectar ao banco de dados Oracle (utilize a função conectar_ao_banco)
    connection = conectar_ao_banco()

    # 2. Exibir os registros disponíveis para atualização (pode ser em uma Listbox ou Treeview)
    registros = realizar_consulta(connection, "SELECT * FROM Clientes;")
    listbox = tk.Listbox(root)
    for registro in registros:
        listbox.insert(tk.END, f"ID: {registro[0]}, Nome: {registro[1]}, CPF: {registro[2]}")
    listbox.pack()

    # 3. Criar um botão para abrir uma nova janela com os campos de atualização
    def abrir_janela_atualizacao():
        selected_item = listbox.get(listbox.curselection())
        id_cliente = int(selected_item.split(":")[1].split(",")[0])

        # 4. Criar uma nova janela para a atualização
        janela_atualizacao = tk.Toplevel(root)
        janela_atualizacao.title("Atualizar Cliente")
        janela_atualizacao.geometry("300x200")

        tk.Label(janela_atualizacao, text="Novo Nome:").pack()
        entry_nome = tk.Entry(janela_atualizacao)
        entry_nome.pack()

        tk.Label(janela_atualizacao, text="Novo CPF:").pack()
        entry_cpf = tk.Entry(janela_atualizacao)
        entry_cpf.pack()

        # 5. Criar um botão para realizar a atualização
        def atualizar_cliente():
            novo_nome = entry_nome.get()
            novo_cpf = entry_cpf.get()

            # 6. Realizar a atualização no banco de dados
            realizar_atualizacao(connection, "Clientes", {"Nome": novo_nome, "CPF": novo_cpf}, "ID", id_cliente)

            # 7. Informar ao usuário que a atualização foi realizada com sucesso
            messagebox.showinfo("Sucesso", "Cliente atualizado com sucesso!")

            # 8. Fechar a janela de atualização
            janela_atualizacao.destroy()

            # 9. Atualizar a lista de registros após a atualização
            listbox.delete(0, tk.END)
            registros_atualizados = realizar_consulta(connection, "SELECT * FROM Clientes;")
            for registro in registros_atualizados:
                listbox.insert(tk.END, f"ID: {registro[0]}, Nome: {registro[1]}, CPF: {registro[2]}")

        button_atualizar = tk.Button(janela_atualizacao, text="Atualizar", command=atualizar_cliente)
        button_atualizar.pack(pady=20)

    button_abrir_janela = tk.Button(root, text="Atualizar Cliente", command=abrir_janela_atualizacao)
    button_abrir_janela.pack(pady=20)

    # 10. Desconectar do banco de dados
    desconectar_do_banco(connection)

    button_voltar = tk.Button(root, text="Voltar", command=root.quit)
    button_voltar.pack(pady=20)

    root.mainloop()

# Função para exibir o menu principal
def exibir_menu_principal():
    root = tk.Tk()
    root.title("Menu Principal")
    root.geometry("400x300")

    label = tk.Label(root, text="Menu Principal", font=("Helvetica", 20))
    label.pack(pady=20)

    # Botões para acessar os submenus
    button_relatorios = tk.Button(root, text="Relatórios", command=exibir_submenu_relatorios)
    button_relatorios.pack(pady=10)

    button_inserir = tk.Button(root, text="Inserir Registros", command=exibir_submenu_inserir)
    button_inserir.pack(pady=10)

    button_remover = tk.Button(root, text="Remover Registros", command=exibir_submenu_remover)
    button_remover.pack(pady=10)

    button_atualizar = tk.Button(root, text="Atualizar Registros", command=exibir_submenu_atualizar)
    button_atualizar.pack(pady=10)

    button_sair = tk.Button(root, text="Sair", command=root.quit)
    button_sair.pack(pady=20)

    root.mainloop()

# Função para exibir a splash screen
def splash_screen():
    root = tk.Tk()
    root.title("Sistema Bancário")
    root.geometry("900x400")

    # Criar um canvas
    canvas = tk.Canvas(root, width=900, height=453)
    canvas.pack()

    # Carregar a imagem
    image = Image.open(".\\imagem\\openbanking.jpg")
    photo = ImageTk.PhotoImage(image)

    # Exibir a imagem no canvas
    canvas.create_image(476, 226, anchor=tk.CENTER, image=photo)

    # Informações dos desenvolvedores
    desenvolvido_por = [
        "Bem-vindo ao Sistema Bancário",
        "Desenvolvido por:",
        "Carlos de Aquino Itaboray",
        "Fabrício Dias de Oliveira",
        "Maciel Costa do Nascimento",
    ]

    # Adicionar as informações como texto no canvas
    y_pos = 100
    for info in desenvolvido_por:
        canvas.create_text(30, y_pos, text=info, font=("Helvetica", 18, "bold"), fill="white", anchor=tk.W)
        y_pos += 30
        y_pos += 10  # Adicionando um espaçamento de 10 pixels entre cada linha

    # Após 5 segundos, fechar a splash screen e exibir o menu principal
    root.after(5000, lambda: [root.destroy(), exibir_menu_principal()])

    root.mainloop()

# Chamar a função para exibir a splash screen
splash_screen()
