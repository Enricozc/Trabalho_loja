import streamlit as st
import requests

BASE_URL = "http://127.0.0.1:8000"

st.set_page_config(page_title="Gerenciador de Produtos", page_icon="🛒")
st.title("🛒 Gerenciador de Produtos")

# --- MENU ---
menu = st.sidebar.selectbox("Menu", ["Listar Produtos", "Adicionar Produto"])

# --- LISTAR PRODUTOS ---
if menu == "Listar Produtos":
    st.subheader("📦 Lista de Produtos")

    response = requests.get(f"{BASE_URL}/produtos")

    if response.status_code == 200:
        produtos = response.json()["produtos"]

        if produtos:
            for p in produtos:
                with st.container():
                    st.markdown(f"### {p['nome']}")
                    st.write(f"📝 Descrição: {p['descricao']}")
                    st.write(f"💰 Preço: R$ {p['preco']:.2f}")
                    st.write(f"📦 Estoque: {p['estoque']} unidades")
                    st.write(f"🏷️ Categoria: {p['categoria']}")
        else:
            st.info("Esse produto ainda não foi cadastrado!!")
    else:
        st.error("Erro ao buscar produto na api")
elif menu == "Adicionar Produto":
    st.subheader("Cadastrar novo produto")

    with st.form("form_produto"):
        nome = st.text_input("Nome do produto")
        descricao = st.text_area("Descrição")
        preço = st.text_input("$Preço")
        estoque = st.text_input("Estoque")
        categoria = st.text_input("Categoria")
        enviar = st.form_submit_button("Salvar")

        if enviar:
            dados = {
                "nome": nome,
                "descricao": descricao,
                "preco": preço, 
                "estoque": estoque,
                "categoria": categoria
            }

            response = requests.post(f"{BASE_URL}/produtos", json=dados)

            if response.status_code == 200:
                st.success("✅ Produto cadastrado com sucesso!")
            else:
                st.error("❌ Erro ao cadastrar produto.")
    
elif menu == "Buscar Produto":
    st.subheader("Buscar produto pelo nome")

    nome_busca = st.text_input("Digite o nome do produto para buscar")
    if st.button("Buscar"):
        response = requests.get(f"{BASE_URL}/produtos/{nome_busca}")
        if response.status_code == 200:
            produto = response.json()
            if produto:
                st.markdown(f"### {produto['nome']}")
                st.write(f"📝 Descrição: {produto['descricao']}")
                st.write(f"💰 Preço: R$ {produto['preco']:.2f}")
                st.write(f"📦 Estoque: {produto['estoque']} unidades")
                st.write(f"🏷️ Categoria: {produto['categoria']}")
            else:
                st.info("Produto não encontrado.")
        else:
            st.error("Erro ao buscar produto.")