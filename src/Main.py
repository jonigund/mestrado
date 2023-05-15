import threading
from tkinter import *
from serial import Serial
from datetime import datetime
import time
import ex003



porta = "COM3"
velocidade = 9600
arduino = Serial(porta, velocidade)
ex003.tempAgua = "0"
pHAgua2 = ex003.pHAgua
NH3 = ex003.cursor

loop1 = True
loop2 = True

# --- thread para função de leitura serial e armazenamento ---
def tarefa2():

    while loop2 == True:
        sensorTempAgua = str(arduino.readline())
        tempAgua = (sensorTempAgua[70:-5])
        pHAgua = (sensorTempAgua[39:-35])
        global tempAgua2
        tempAgua2 = tempAgua
        global pHAgua2
        pHAgua2 = pHAgua
        agora = datetime.now()
        diaAtu = (str(agora.day) + "/" + str(agora.month) + "/" + str(agora.year))
        horaAtu = (str(agora.hour) + ":" + str(agora.minute) + ":" + str(agora.second))
        print(sensorTempAgua)
        print(diaAtu, horaAtu)


# --- Bloco de atualização dos dados ---
def tarefa3():
    for second in range(10000):
        if pHAgua2 != "":
            dados_ph['text'] = pHAgua2
            dados_temperatura['text'] = tempAgua2

        else:
            dados_ph['text'] = "Carregando"
            dados_temperatura['text'] = "Carregando"

        print("teste atualização")
        time.sleep(5)


# --- Bloco para renderização da tela ---
master = Tk()
master.title("Sistema de monitoramento - Aquaponia")
master.geometry("600x400+610+150")
master.resizable(width=FALSE, height=FALSE)

img_fundo = PhotoImage(file="..\\imagens\\fundo2.png")

lab_fundo = Label(master, image=img_fundo)
lab_fundo.pack()


dados_temperatura = Label(master, text=tempAgua2, bd=2, font=("calibri", 22), justify=CENTER)
dados_temperatura.place(width=90, height=50, x=46, y=174)

dados_ph = Label(master, text=pHAgua2, bd=2, font=("calibri", 22), justify=CENTER)
dados_ph.place(width=90, height=50, x=244, y=174)

dados_NH3 = Label(master, text=NH3, bd=2, font=("calibri", 22), justify=CENTER)
dados_NH3.place(width=90, height=50, x=442, y=174)

threading.Thread(target=tarefa2).start()
threading.Thread(target=tarefa3).start()

master.mainloop()
