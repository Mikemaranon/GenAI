import os
import streamlit as st
from openai import AzureOpenAI

# Configuración del cliente Azure OpenAI
client = AzureOpenAI(
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
    api_key=os.getenv("AZURE_OPENAI_API_KEY"),
    api_version="2024-02-15-preview"
)

# Función para generar resumen
def generate_summary(text):
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",  # Cambia al modelo que tengas configurado
            messages=[{"role": "user", "content": f"Summarize the following text: {text}"}]
        )
        return response.choices[0].message.content  # Acceder al contenido correctamente
    except Exception as e:
        st.error(f"Error al generar resumen: {e}")
        return None

# Función para generar respuesta
def generate_answer(text):
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",  # Cambia al modelo que tengas configurado
            messages=[{"role": "user", "content": f"Provide an appropriate response to the following email: {text}"}]
        )
        return response.choices[0].message.content  # Acceder al contenido correctamente
    except Exception as e:
        st.error(f"Error al generar respuesta: {e}")
        return None

# Interfaz de usuario con Streamlit
st.title("Email Summarization and Answer App")
st.write("Esta aplicación te ayuda a resumir y responder correos electrónicos de manera eficiente utilizando Azure OpenAI.")

# Área de texto para ingresar el correo electrónico
email_input = st.text_area("Introduce tu correo electrónico aquí:", height=200)

# Botones para generar el resumen y la respuesta
if st.button("Generar Resumen"):
    if email_input.strip():
        summary = generate_summary(email_input)
        if summary:
            st.subheader("Resumen generado:")
            st.write(summary)
    else:
        st.warning("Por favor, introduce un correo electrónico válido.")

if st.button("Generar Respuesta"):
    if email_input.strip():
        answer = generate_answer(email_input)
        if answer:
            st.subheader("Respuesta generada:")
            st.write(answer)
    else:
        st.warning("Por favor, introduce un correo electrónico válido.")