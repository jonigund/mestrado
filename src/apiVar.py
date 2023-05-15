from serial import Serial
from datetime import datetime
import time
import streamlit as st;
import pandas as pd;


# with open("styles.module.css") as f:
#     st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html= True)
#     st.text(f"<style>{f.read()}</style>", unsafe_allow_html= True)


porta = "COM3"
velocidade = 9600
arduino = Serial(porta, velocidade)
tempAgua2 = "0"
pHAgua2 = "0"

loop1 = True
loop2 = True

col1, col2, col3 = st.columns([1, 5, 1])
with col2:
    st.markdown("Painel de monitoramento")

    st.text(tempAgua2)
    st.text(pHAgua2)
    st.text("NH3 ANI")
#for seconds in range(2000):
    #time.sleep(10)


# enquanto todos os dados necessarios para o correto armazenamento estiverem sendo obtidos, passar para os tratamentos
# de erros caso ocorram nos bds
while True:
    sensorTempAgua = str(arduino.readline())
    tempAgua = (sensorTempAgua[70:-5])
    pHAgua = (sensorTempAgua[39:-35])
    tempAgua2 = tempAgua
    pHAgua2 = pHAgua
    agora = datetime.now()
    diaAtu = (str(agora.day) + "/" + str(agora.month) + "/" + str(agora.year))
    horaAtu = (str(agora.hour) + ":" + str(agora.minute) + ":" + str(agora.second))
    print(sensorTempAgua)
    print(diaAtu, horaAtu)








