import streamlit as st
import sqlite3

# Conexão com o banco SQLite
conn = sqlite3.connect("database.db", check_same_thread=False)
cursor = conn.cursor()

# Criação da tabela se não existir
cursor.execute("CREATE TABLE IF NOT EXISTS pessoas (nome TEXT)")

st.title("Formulário de Nomes")

# Campo de input
nome = st.text_input("Digite seu nome")

# Botão de salvar
if st.button("Salvar"):
    if nome:
        cursor.execute("INSERT INTO pessoas (nome) VALUES (?)", (nome,))
        conn.commit()
        st.success(f"Nome '{nome}' salvo com sucesso!")
    else:
        st.warning("Digite um nome antes de salvar.")

# Botão de listar nomes
if st.button("Ver todos os nomes salvos"):
    cursor.execute("SELECT nome FROM pessoas")
    nomes = cursor.fetchall()
    st.write("Nomes salvos:")
    for n in nomes:
        st.write(f"- {n[0]}")