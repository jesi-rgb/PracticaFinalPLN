import streamlit as st
import pandas as pd
import numpy as np
from semantica import desambiguar, sinonimos, antonimos
from morfologico import morph_analysis
from entidades import named_entity_recognition
import pandas as pd

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
        option = st.selectbox("Clica y teclea una palabra para ver sus definiciones:", [x for x in sorted(synsets.keys())])

        if len(synsets[option]) == 0:
            st.write("No se ha encontrado ninguna entrada para el término **{}**.".format(option))
        else:
            for syn in synsets[option]:
                st.write("**"+syn.name()+"**: "+syn.definition())
                if len(syn.examples()) > 0:
                    st.markdown("###### Ejemplo: _{}_".format(syn.examples()[0]))

                st.markdown("***")


        option_highlight = st.radio('', ['Sinónimos', 'Antónimos'])

        if option_highlight == 'Sinónimos':
            st.markdown('''
            ##### Aquí se muestra el texto introducido, pero las palabras han sido sustituidas por los sinónimos que ha encontrado el sistema. La palabra <span style=color:red> _original luce así_</span> y su <span style=color:blue> **sustituta, así**</span>.
            #####''', unsafe_allow_html=True)

            name_regex = st.checkbox('Nombres')
            adj_regex = st.checkbox("Adjetivos")
            vrb_regex = st.checkbox("Verbos")
            adv_regex = st.checkbox("Adverbios")
            output_text = sinonimos(message, name_regex, adj_regex, vrb_regex, adv_regex)
            st.markdown(output_text, unsafe_allow_html=True)
        

        if option_highlight == 'Antónimos':
            st.markdown('''
            ##### Aquí se muestra el texto introducido, pero las palabras han sido sustituidas por los antónimos que ha encontrado el sistema. La palabra <span style=color:red> _original luce así_</span> y su <span style=color:blue> **sustituta, así**</span>.
            #####''', unsafe_allow_html=True)
            name_regex = st.checkbox("Nombres")
            adj_regex = st.checkbox("Adjetivos")
            vrb_regex = st.checkbox("Verbos")
            adv_regex = st.checkbox("Adverbios")
            output_text = antonimos(message, name_regex, adj_regex, vrb_regex, adv_regex)
            st.markdown(output_text, unsafe_allow_html=True)


def morfologico():
    st.subheader("Análisis morfológico")
    input_method = st.radio('Elige un método', ['Escribir texto', 'Subir un archivo'])
    data = None
    message = None

    if input_method == 'Escribir texto':
        message = st.text_area("Introduce texto (en inglés) a analizar...")
        data = morph_analysis(message)
    else:
        input_file = st.file_uploader("... o arrastra aquí un fichero", encoding='auto', type=["csv", "txt"])
    
        if input_file is not None:
            message = input_file.read()
            data = morph_analysis(message)


    if message:
        st.markdown("***")
        if data[0] == 1:
            st.markdown("Este texto contiene una única oración.")
        else:
            st.markdown("Este texto contiene **{}** oraciones.".format(data[0]))
        
        
        st.markdown("***")

        st.write("Algunos datos de tu texto:")

        st.bar_chart(pd.DataFrame.from_dict(data[1], orient='index'), height=600)
        st.write("En total, el texto contiene **{}** palabras.".format(sum(data[1].values())))

        st.markdown("***")

        st.write("Las 5 palabras más utilizadas son:")
        st.bar_chart(pd.DataFrame.from_dict(data[2], orient='index'))

        st.markdown("***")

        st.write("Y aquí tenemos una distribución de las categorías de las palabras:")
        st.bar_chart(pd.DataFrame.from_dict(data[3], orient='index'), height=600)



def entities():
    st.subheader("Reconocimiento de entidades")
    input_method = st.radio('Elige un método', ['Escribir texto', 'Subir un archivo'])
    data = None
    message = None

    if input_method == 'Escribir texto':
        message = st.text_area("Introduce texto (en inglés) a analizar...")
        data = named_entity_recognition(message)
    else:
        input_file = st.file_uploader("... o arrastra aquí un fichero", encoding='auto', type=["csv", "txt"])
    
        if input_file is not None:
            message = input_file.read()
            data = named_entity_recognition(message)

    if data:
        st.markdown(data, unsafe_allow_html=True)


def main():
	# Title
    st.title("Procesamiento del lenguaje Natural")
    st.header("Aplicación web para analizar texto de varias maneras")

    
    option = st.sidebar.radio("Elige el modo de análisis", ['Análisis semántico' ,'Análisis morfológico', 'Reconocedor de entidades'])
  
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