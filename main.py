import streamlit as st
import pandas as pd
import numpy as np
from semantica import desambiguar, sinonimos, antonimos



def desambiguacion():
    st.subheader("Análisis semántico")
    input_method = st.radio('Elige un método', ['Escribir texto', 'Subir un archivo'])
    message = ''
    synsets = None

    if input_method == 'Escribir texto':
        message = st.text_area("Introduce texto (en inglés) a analizar...")
        synsets = desambiguar(message)
    else:
        input_file = st.file_uploader("... o arrastra aquí un fichero", encoding='auto', type=["csv", "txt"])
    
        if input_file is not None:
            message = input_file.read()
            synsets = desambiguar(message)


    if synsets:
        option = st.selectbox("Elige una palabra a desambiguar:", [x for x in sorted(synsets.keys())])
        st.markdown("**"+synsets[option].name()+"**: "+synsets[option].definition())

        if len(synsets[option].examples()) > 0:
            st.write("Un ejemplo de uso: _{}_".format(synsets[option].examples()[0]))

    st.markdown("***")

    if st.checkbox('Sinónimos'):
        st.markdown('''
        ##### Aquí se muestra el texto introducido, pero las palabras han sido sustituidas por los sinónimos que ha encontrado el sistema. La palabra <span style=color:red> _original luce así_</span> y su <span style=color:blue> **sustituta, así**</span>.
        #####''', unsafe_allow_html=True)

        name_regex = st.checkbox('Nombres')
        adj_regex = st.checkbox("Adjetivos")
        vrb_regex = st.checkbox("Verbos")
        adv_regex = st.checkbox("Adverbios")
        output_text = sinonimos(message, name_regex, adj_regex, vrb_regex, adv_regex)
        st.markdown(output_text, unsafe_allow_html=True)
    
    st.markdown("***")
    if st.checkbox('Antónimos'):
        st.markdown('''
        ##### Aquí se muestra el texto introducido, pero las palabras han sido sustituidas por los antónimos que ha encontrado el sistema. La palabra <span style=color:red> _original luce así_</span> y su <span style=color:blue> **sustituta, así**</span>.
        #####''', unsafe_allow_html=True)
        name_regex = st.checkbox('Nombres')
        adj_regex = st.checkbox("Adjetivos")
        vrb_regex = st.checkbox("Verbos")
        adv_regex = st.checkbox("Adverbios")
        output_text = antonimos(message, name_regex, adj_regex, vrb_regex, adv_regex)
        st.markdown(output_text, unsafe_allow_html=True)

    

def morfologico():
    # st.markdown('Some _Markdown_ text with <span style="background-color:blue;color:white">some **blue** text</span>.', unsafe_allow_html=True)
    st.subheader("Análisis morfológico")

def entities():
    st.subheader("Reconocimiento de entidades")

def main():
	# Title
    st.title("Procesamiento del lenguaje Natural")
    st.subheader("Aplicación web para analizar texto de varias maneras")

    st.markdown("***")
    option = st.radio("Elige el modo de análisis", ['Análisis semántico' ,'Análisis morfológico', 'Reconocedor de entidades'])
    st.markdown("***")
    if option == 'Análisis semántico':
        desambiguacion()
    elif option == 'Análisis morfológico':
        morfologico()
    elif option == 'Reconocedor de entidades':
        entities()

    
    st.sidebar.subheader("About")
    st.sidebar.text("Práctica final de PLN")
    st.sidebar.info("Jesús Enrique Cartas Rascón")





if __name__ == "__main__":
    main()