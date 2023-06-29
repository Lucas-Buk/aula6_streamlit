# Importando as bibliotecas
import streamlit as st
import requests

st.set_page_config(  # Alternate names: setup_page, page, layout
	layout='wide',  # Can be "centered" or "wide". In the future also "dashboard", etc.
	initial_sidebar_state='auto',  # Can be "auto", "expanded", "collapsed"
	page_title='Serviço OCR - Azure',  # String or None. Strings get appended with "• Streamlit". 
	page_icon=None,  # String, anything supported by st.image, or None.
)
st.header('Reconhecimento Óptico de Caracteres (OCR)') 

st.write('### Faça o upload de uma imagem para usar o serviço')

# Função para utilizar o serviço de OCR
def ocr(url, file, key):

    # Cabeçalhos
    headers = {'Content-Type': 'application/octet-stream',
               'Ocp-Apim-Subscription-Key': key}

    # Requisição
    response = requests.request("POST", url, headers=headers, data=file)

    return response

col1, col2 = st.columns(2)
img = col1.file_uploader('Upload da imagem')
if img is not None:
    col3, col4, col5 = col2.columns(3)
    col4.image(img, width=300)

url = 'https://pg-aula3.cognitiveservices.azure.com/computervision/imageanalysis:analyze?api-version=2023-02-01-preview&features=Read&language=en&gender-neutral-caption=False'
key = 'e5c24d57caad490684fbff40c0171ef4'

if col1.button('Utilizar serviço'):
    if img is None:
        col1.write(':face_with_spiral_eyes: Adicione uma imagem para continuar :face_with_spiral_eyes:')
    else:
        file = img.getvalue()
        resp = ocr(url, file, key)
        texto = resp.json()['readResult']['content']
        col2.write('#### Texto da imagem:')
        col2.text(texto)
    
