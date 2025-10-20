from fastapi import FastAPI
import funcao


app = FastAPI(title="Gerenciador de Loja")

@app.get("/")
def home():
    return {"mensagem": "Bem-vindo ao gerenciador de loja!"}


@app.post("/produtos")
def criar_produto(
    nome: str,
    descricao: str,
    preco: float,
    estoque: int,
    categoria: str
):
    funcao.inserir_produto(nome, descricao, preco, estoque, categoria)
    return {"mensagem": "Produto adicionado com sucesso!"}


@app.get("/produtos")
def listar_produtos():
    produtos = funcao.listar_produtos()
    lista = []
    for linha in produtos:
        lista.append({
            "id": linha[0],
            "nome": linha[1],
            "descricao": linha[2],
            "preco": linha[3],
            "estoque": linha[4],
            "categoria": linha[5]
        })
    return {"produtos": lista}


@app.get("/produtos/{id_produto}")
def buscar_produto(id_produto: int):
    produto = funcao.buscar_produto(id_produto)
    if produto:
        return {
            "id": produto[0],
            "nome": produto[1],
            "descricao": produto[2],
            "preco": produto[3],
            "estoque": produto[4],
            "categoria": produto[5]
        }
    else:
        return {"erro": "Produto não encontrado"}



@app.put("/produtos/{id_produto}")
def atualizar_produto(
    id_produto: int,
    novo_preco: float = None,
    novo_estoque: int = None
):
    produto = funcao.buscar_produto(id_produto)
    if produto:
        funcao.atualizar_produto(id_produto, novo_preco, novo_estoque)
        return {"mensagem": "Produto atualizado com sucesso!"}
    else:
        return {"erro": "Produto não encontrado"}


@app.delete("/produtos/{id_produto}")
def deletar_produto(id_produto: int):
    produto = funcao.buscar_produto(id_produto)
    if produto:
        funcao.deletar_produto(id_produto)
        return {"mensagem": "Produto excluído com sucesso!"}
    else:
        return {"erro": "Produto não encontrado"}
