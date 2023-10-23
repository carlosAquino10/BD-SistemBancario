import cx_Oracle

# Função para conectar ao banco de dados Oracle
def conectar_ao_banco():
    try:
        conexao = cx_Oracle.connect("seu_usuario/sua_senha@localhost:1521/seu_sid")
        return conexao
    except Exception as e:
        print(f"Erro ao conectar ao banco de dados: {e}")
        return None

# Função para executar uma query e retornar os resultados
def executar_query(conexao, query):
    try:
        cursor = conexao.cursor()
        cursor.execute(query)
        return cursor.fetchall()
    except Exception as e:
        print(f"Erro ao executar a query: {e}")
        return None

# Função para inserir registros no banco de dados
def inserir_registro(conexao, query):
    try:
        cursor = conexao.cursor()
        cursor.execute(query)
        conexao.commit()
        print("Registro inserido com sucesso.")
    except Exception as e:
        print(f"Erro ao inserir registro: {e}")

# Função para remover registros do banco de dados
def remover_registro(conexao, query):
    try:
        cursor = conexao.cursor()
        cursor.execute(query)
        conexao.commit()
        print("Registro removido com sucesso.")
    except Exception as e:
        print(f"Erro ao remover registro: {e}")

# Função para atualizar registros no banco de dados
def atualizar_registro(conexao, query):
    try:
        cursor = conexao.cursor()
        cursor.execute(query)
        conexao.commit()
        print("Registro atualizado com sucesso.")
    except Exception as e:
        print(f"Erro ao atualizar registro: {e}")

# Conectar ao banco de dados Oracle
conexao_oracle = conectar_ao_banco()

if conexao_oracle is not None:
    print("Conexão bem-sucedida com o banco de dados Oracle.")
else:
    print("Não foi possível conectar ao banco de dados Oracle.")

# Agora você pode usar as funções de banco de dados ao longo do seu código.

# Exemplo de como executar uma query de contagem de registros:
query_contagem_clientes_nubank = "SELECT COUNT(1) FROM clientes WHERE banco = 'Nubank'"
total_clientes_nubank = executar_query(conexao_oracle, query_contagem_clientes_nubank)

if total_clientes_nubank is not None:
    print(f"Total de clientes no Nubank: {total_clientes_nubank[0][0]}")
else:
    print("Não foi possível obter o total de clientes no Nubank.")

# Exemplo de como inserir um novo cliente:
query_inserir_cliente = "INSERT INTO clientes (nome, saldo, banco) VALUES ('João', 1000, 'Nubank')"
inserir_registro(conexao_oracle, query_inserir_cliente)

# Exemplo de como remover um cliente:
query_remover_cliente = "DELETE FROM clientes WHERE id = 1"
remover_registro(conexao_oracle, query_remover_cliente)

# Exemplo de como atualizar o saldo de um cliente:
query_atualizar_saldo = "UPDATE clientes SET saldo = 1500 WHERE id = 2"
atualizar_registro(conexao_oracle, query_atualizar_saldo)

# Lembre-se de substituir os placeholders ('seu_usuario', 'sua_senha', 'localhost:1521/seu_sid')
# pelos dados reais do seu banco de dados Oracle.
