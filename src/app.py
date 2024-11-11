import streamlit as st
from services.credit_card_service import analize_credit_card

def configure_interface():
    st.title("Upload de Arquivo DIO - Desafio 2 - Azure - Fake Docs")
    uploaded_file = st.file_uploader("Escolha um arquivo", type=["png", "jpg", "jpeg"])

    if uploaded_file is not None:
        file_name = uploaded_file.name  # Atribui o nome do arquivo
        st.image(uploaded_file, caption="Pré-visualização da Imagem", use_container_width=True)  # Exibe a imagem diretamente
        
        # Simulação do upload para o Blob Storage e obtenção da URL
        blob_url = upload_blob(uploaded_file, file_name)

        if blob_url:
            st.write(f"Arquivo '{file_name}' enviado com sucesso para o Azure Blob Storage")
            credit_card_info = analize_credit_card(blob_url)  # Simule: chame a função real de detecção aqui
            show_image_and_validation(blob_url, credit_card_info)
        else:
            st.write(f"Erro ao enviar o arquivo '{file_name}' para o Azure Blob Storage.")
    else:
        st.write("Por favor, faça o upload de um arquivo para continuar.")

def upload_blob(file, file_name):
    # Esta função deve implementar o upload real do arquivo para o Azure Blob Storage
    # Para esta simulação, retornaremos uma URL fictícia para testes
    if file and file_name:
        # Substitua pela integração real com Azure Blob Storage
        return f"https://exemplo.com/{file_name}"  # Simulação de URL do Blob
    return None

def show_image_and_validation(blob_url, credit_card_info):
    # Exibe a imagem usando a URL fictícia ou real do Azure Blob
    st.image(blob_url, caption="Imagem enviada", use_container_width=True)
    st.write("Resultado da validação:")

    # Verificação das informações do cartão de crédito
    if credit_card_info and credit_card_info.get("card_name"):
        st.markdown("<h1 style='color: green;'>Cartão Válido</h1>", unsafe_allow_html=True)
        st.write(f"Nome do Titular: {credit_card_info['card_name']}")
        st.write(f"Banco Emissor: {credit_card_info['bank_name']}")
        st.write(f"Data de Validade: {credit_card_info['expiry_date']}")
    else:
        st.markdown("<h1 style='color: red;'>Cartão Inválido</h1>", unsafe_allow_html=True)
        st.write("Este não é um cartão de crédito válido.")

if __name__ == "__main__":
    configure_interface()
