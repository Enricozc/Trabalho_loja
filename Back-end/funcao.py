from conexao import conectar

def criar_tabela():
    conexao, cursor = conectar()
    if conexao:
        try:
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS produtos (
                    id SERIAL PRIMARY KEY,
                    nome TEXT NOT NULL,
                    descricao TEXT,
                    preco REAL NOT NULL,
                    estoque INTEGER NOT NULL,
                    categoria TEXT
                )
            """)
            conexao.commit()
            print("✅ Tabela 'produtos' criada com sucesso!")
        except Exception as erro:
            print(f"❌ Erro ao criar tabela: {erro}")
        finally:
            cursor.close()
            conexao.close()

criar_tabela()


def inserir_produto(nome, descricao, preco, estoque, categoria):
    conexao, cursor = conectar()
    if conexao:
        try:
            cursor.execute(
                "INSERT INTO produtos (nome, descricao, preco, estoque, categoria) VALUES (%s, %s, %s, %s, %s)",
                (nome, descricao, preco, estoque, categoria)
            )
            conexao.commit()
            print(" Produto inserido com sucesso!")
        except Exception as erro:
            print(f" Erro ao inserir produto: {erro}")
        finally:
            cursor.close()
            conexao.close()

