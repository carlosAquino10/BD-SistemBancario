def criar_relacionamento_transacoes_bancos(connection):
    cursor = connection.cursor()

    # Criação da chave estrangeira
    try:
        cursor.execute('ALTER TABLE Transacoes ADD CONSTRAINT fk_Bancos FOREIGN KEY (Banco) REFERENCES Bancos(Nome)')
        print("Relacionamento entre Transacoes e Bancos criado com sucesso!")
    except Exception as e:
        print(f"Erro ao criar relacionamento entre Transacoes e Bancos: {e}")

    cursor.close()
    
