# 1 titulo
# 2 input do chat
# 3 a cada mensagem enviada
''' mostra no chat a mensagem do usuario
    enviar mensagem para IA
    aparece na tela a resposta '''

import streamlit as st
from openai import OpenAI

modelo = OpenAI()

st.write("#### Chatbot com IA")

if not "lista_mensagens" in st.session_state:
    st.session_state["lista_mensagens"] = []

for mensagem in st.session_state["lista_mensagens"]:
    role = mensagem["role"]
    content = mensagem["content"]
    st.chat_message(role).write(content)



mensagem_usuario  = st.chat_input("Escreva em que posso te ajudar! :)")

if mensagem_usuario:
    st.chat_message("user").write(mensagem_usuario)
    mensagem = {"role": "user", "content": mensagem_usuario}
    st.session_state["lista_mensagens"].append(mensagem)

    resposta_modelo= modelo.chat.completions.create(messages = st.session_state["lista_mensagens"], model = "gpt-4o")
    resposta_ia = resposta_modelo.choices[0].message.content

    st.chat_message("assistant").write(resposta_ia)
    mensagem_ia = {"role": "assistant", "content"   : resposta_ia}
    st.session_state["lista_mensagens"].append(mensagem_ia)
