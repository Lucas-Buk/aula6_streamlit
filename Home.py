# Importando as bibliotecas
import streamlit as st

st.set_page_config(  # Alternate names: setup_page, page, layout
	layout='wide',  # Can be "centered" or "wide". In the future also "dashboard", etc.
	initial_sidebar_state='auto',  # Can be "auto", "expanded", "collapsed"
	page_title='Aula 6 - Serviços de Software de IA',  # String or None. Strings get appended with "• Streamlit". 
	page_icon=None,  # String, anything supported by st.image, or None.
)
st.write('# Aula 6 - Serviços de Software de IA') 

st.write('### Estamos criando uma página usando o Streamlit para usar os serviços da Azure vistos em aula :sunglasses:')

st.write('Use as páginas ao lado para usar um dos serviços disponíveis')
