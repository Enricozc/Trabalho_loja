from conexao import conectar

def criar_tabela():
    conexao = conectar()
    if conexao:
        cursor = conexao.cursor()
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
            print("Tabela 'produtos' criada com sucesso!")
        except Exception as erro:
            print(f"Erro ao criar tabela: {erro}")
        finally:
            cursor.close()
            conexao.close()


criar_tabela()


def inserir_produto(nome, descricao, preco, estoque, categoria):
    conexao = conectar()
    if conexao:
        cursor = conexao.cursor()
        try:
            cursor.execute(
                """
                INSERT INTO produtos (nome, descricao, preco, estoque, categoria)
                VALUES (%s, %s, %s, %s, %s)
                """,
                (nome, descricao, preco, estoque, categoria)
            )
            conexao.commit()
            print("Produto inserido com sucesso!")
        except Exception as erro:
            print(f"Erro ao inserir produto: {erro}")
        finally:
            cursor.close()
            conexao.close()



def listar_produtos():
    conexao = conectar()
    if conexao:
        cursor = conexao.cursor()
        try:
            cursor.execute("SELECT * FROM produtos ORDER BY id")
            return cursor.fetchall()
        except Exception as erro:
            print(f"Erro ao listar produtos: {erro}")
        finally:
            cursor.close()
            conexao.close()



def atualizar_produto(id_produto, novo_preco=None, novo_estoque=None):
    conexao = conectar()
    if conexao:
        cursor = conexao.cursor()
        try:
            if novo_preco is not None and novo_estoque is not None:
                cursor.execute(
                    "UPDATE produtos SET preco = %s, estoque = %s WHERE id = %s",
                    (novo_preco, novo_estoque, id_produto)
                )
            elif novo_preco is not None:
                cursor.execute(
                    "UPDATE produtos SET preco = %s WHERE id = %s",
                    (novo_preco, id_produto)
                )
            elif novo_estoque is not None:
                cursor.execute(
                    "UPDATE produtos SET estoque = %s WHERE id = %s",
                    (novo_estoque, id_produto)
                )
            else:
                print("⚠️ Nenhum valor fornecido para atualização.")
                return

            conexao.commit()
            print("Produto atualizado com sucesso!")
        except Exception as erro:
            print(f"Erro ao atualizar produto: {erro}")
        finally:
            cursor.close()
            conexao.close()

def deletar_produto(id_produto):
    conexao = conectar()
    if conexao:
        cursor = conexao.cursor()
        try:
            cursor.execute("DELETE FROM produtos WHERE id = %s", (id_produto,))
            conexao.commit()
            print("Produto deletado com sucesso!")
        except Exception as erro:
            print(f"Erro ao deletar produto: {erro}")
        finally:
            cursor.close()
            conexao.close()



def buscar_produto(id_produto):
    conexao = conectar()
    if conexao:
        cursor = conexao.cursor()
        try:
            cursor.execute("SELECT * FROM produtos WHERE id = %s", (id_produto,))
            produto = cursor.fetchone()
            if produto:
                return produto
            else:
                print("Produto não encontrado.")
                return None
        except Exception as erro:
            print(f"Erro ao buscar produto: {erro}")
        finally:
            cursor.close()
            conexao.close()
