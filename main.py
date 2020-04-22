import streamlit as st
import pandas as pd
import numpy as np
from desambiguar import desambiguar

def main():
	# Title
    st.title("Procesamiento del lenguaje Natural")
    st.subheader("Aplicación para analizar texto")


    st.subheader("Desambiguación")
    message = st.text_area("Introduce texto a analizar...")
    synsets = desambiguar(message)
    
    option = st.selectbox("Elige una palabra a desambiguar:", [x for x in synsets.keys()])

    st.write(synsets[option].lemma_names())
    if len(synsets[option].examples()) > 0:
        st.write("Un ejemplo de uso: _{}_".format(synsets[option].examples()[0]))




    st.sidebar.subheader("About")
    st.sidebar.text("Práctica final de PLN")
    st.sidebar.info("Jesús Enrique Cartas Rascón")





if __name__ == "__main__":
    main()