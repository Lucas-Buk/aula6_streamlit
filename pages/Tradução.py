# Importando as bibliotecas
import streamlit as st
import requests, uuid, json

st.set_page_config(  # Alternate names: setup_page, page, layout
	layout='wide',  # Can be "centered" or "wide". In the future also "dashboard", etc.
	initial_sidebar_state='auto',  # Can be "auto", "expanded", "collapsed"
	page_title='Serviço de Tradução - Azure',  # String or None. Strings get appended with "• Streamlit". 
	page_icon=None,  # String, anything supported by st.image, or None.
)
st.header('Tradução de frases') 

# Função para utilizar o serviço de OCR
def traducao(texto, trad_para):
    
    # URL do serviço
    endpoint = "https://api.cognitive.microsofttranslator.com/translate"

    # Parâmetros
    params = {'api-version': '3.0',
              'from': 'pt-BR',
              'to': trad_para}

    # Cabeçalhos
    headers = {'Ocp-Apim-Subscription-Key': 'YOUR_KEY',
               'Ocp-Apim-Subscription-Region': 'global',
                'Content-type': 'application/json',
                'X-ClientTraceId': str(uuid.uuid4())}

    # Corpo
    body = [{'text': texto}]

    # Requisição
    response = requests.post(endpoint, params=params, headers=headers, json=body)

    return response

idiomas = {'Inglês': 'en', 'Japonês': 'ja', 'Alemão': 'de', 'Espanhol': 'es', 'Francês': 'fr', 'Italiano': 'it'}
texto = st.text_area('Digite uma frase em português para ser traduzida:')
ops = st.multiselect('Traduzir para:', idiomas.keys())

id_list = []
for op in ops:
    id_list.append(idiomas[op])

if st.button('Traduzir'):
    if texto == '':
        st.write('Adicione uma frase para traduzir :pencil:')
    else:
        resp = traducao(texto, id_list)
        st.write('#### Traduções:')
        for i, trad in enumerate(resp.json()[0]['translations']):
            texto = trad['text']
            idioma = ops[i]
            st.write(f'{idioma}: {texto}')
    
