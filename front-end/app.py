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
 