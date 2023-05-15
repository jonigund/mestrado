import serial
import mysql.connector
from mysql.connector import Error
import requests
import json
from datetime import datetime



porta = "COM3"
velocidade = 9600
arduino = serial.Serial(porta, velocidade)

# enquanto todos os dados necessarios para o correto armazenamento estiverem sendo obtidos, passar para os tratamentos
# de erros caso ocorram nos bds
while True:
    sensorTempAgua = str(arduino.readline())
    tempAgua = (sensorTempAgua[70:-5])
    pHAgua = (sensorTempAgua[39:-35])
    agora = datetime.now()
    diaAtu = (str(agora.day) + "/" + str(agora.month) + "/" + str(agora.year))
    horaAtu = (str(agora.hour) + ":" + str(agora.minute) + ":" + str(agora.second))
    print(sensorTempAgua)
    print(diaAtu, horaAtu)

    # método para inserir dos dados no mysql local



    # try:
    #     acesso = mysql.connector.connect(host='localhost', database='aquaponia', user='root', password='123456')
    #     # pula a calibração do sensor ate encontrar a primeira leitura para não dar erro no bd
    #     if sensorTempAgua[0:2] == "b'_'":
    #         insertDados = "INSERT INTO tanque1 (data,hora,tempAgua, phAgua) VALUES('0','0','0','0')"
    #         cursor = acesso.cursor()
    #         cursor.execute(insertDados)
    #         acesso.commit()
    #         print(cursor.rowcount, "dados registrados")
    #         cursor.close()
    #     else:
    #         insertDados = "INSERT INTO tanque1 (data,hora,tempAgua,phAgua) " \
    #                       "VALUES('" + diaAtu + "','" + horaAtu + "','" + tempAgua + "','" + pHAgua + "')"
    #         cursor = acesso.cursor()
    #         cursor.execute(insertDados)
    #         acesso.commit()
    #         print(cursor.rowcount, "dados registrados em LocalDB")
    #         cursor.close()
    # except Error as erro:
    #     print("falha no registro:{}".format(erro))
    # finally:
    #     if acesso.is_connected():
    #         acesso.close()
    #         print("conexão DB local finalizada")






    # método para inserir dos dados no firebase
    # try:
    #     link = "https://aquaponia-5c20d-default-rtdb.firebaseio.com/"
    #     # pula a calibração do sensor ate encontrar a primeira leitura para não dar erro no bd
    #     if sensorTempAgua[0:2] == "b'_'":
    #         dados = {'data': '0', 'hora': '0', 'tempAgua': '0', 'phAgua': '0'}
    #         requisicaoFireBase = requests.post(f'{link}/tanque1/.json', data=json.dumps(dados))
    #         print(requisicaoFireBase)
    #         print(requisicaoFireBase.text)
    #         print("dados registrados")
    #     else:
    #         dados = {'data': diaAtu, 'hora': horaAtu, 'tempAgua': tempAgua, 'phAgua': pHAgua}
    #         requisicaoFireBase = requests.post(f'{link}/tanque1/.json', data=json.dumps(dados))
    #         print(requisicaoFireBase)
    #         print(requisicaoFireBase.text)
    #         print("dados registrados")
    # except Error as erro:
    #     print("falha no registro:{}".format(erro))
    # finally:
    #     print("conexão DB Firebase finalizada")

arduino.close()
