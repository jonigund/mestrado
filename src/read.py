import time
import streamlit as st;
import mysql.connector
from mysql.connector import Error

#import ex003 as bk;
import pandas as pd;

with open("styles.module.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html= True)

   
   
    col1, col2, col3 = st.columns([1,2,1])

    for seconds in range(2000):
        try:
            acesso = mysql.connector.connect(host='localhost', database='aquaponia', user='root', password='123456')
            # pula a calibração do sensor ate encontrar a primeira leitura para não dar erro no bd
            if acesso.is_connected():
                buscaDados = "SELECT data,hora,tempAgua, phAgua FROM tanque1 ORDER BY data DESC limit 1"
                cursor = acesso.cursor()
                cursor.execute(buscaDados)
                linhas = cursor.fetchall()
                print("Número total de registros retornados: ", cursor.rowcount)

                print("\nMostrando o registro:")
                for linha in linhas:
                    print("data:", linha[0])
                    print("hora:", linha[1])
                    print("tempAgua:", linha[2])
                    print("phAgua:", linha[3])
                cursor.close()
        except Error as erro:
            print("falha na busca:{}".format(erro))
        finally:
            if acesso.is_connected():
                acesso.close()
                print("conexão DB local finalizada")
    time.sleep(1)

    with col2:

            st.markdown("Painel de monitoramento")
            st.text("1")
            st.text("2")
            st.text("NH3 ANI")
            

    




