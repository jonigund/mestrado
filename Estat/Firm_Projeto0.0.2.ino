// Sensoriamento Mestrado versão 0.0.1 - Joni Gund - Outubro 2021

// inclusão
#include <OneWire.h>
#include <DallasTemperature.h>

OneWire onewire(4);
DallasTemperature sensor(&onewire);
float temperaturaAgua;

#include "DFRobot_PH.h"
#include <EEPROM.h>

#define PH_PIN A1
float voltage,phValue,temperature = 25;
DFRobot_PH ph;


void setup() {
  Serial.begin(9600);
  sensor.begin();
  ph.begin();

}

void loop() {
{
   static unsigned long timepoint = millis();
    if(millis()-timepoint>1000U){                  //intervalo: 10s
        timepoint = millis();                       //Tipo de intervalo de leitura
        //temperature = readTemperature();           // Lê a temperatura do ar pelo sensor do módulo pH para fazer a compensação
        voltage = analogRead(PH_PIN)/1024.0*5000;  // Lê a voltagem da sonda
        phValue = ph.readPH(voltage,temperature);  // Converte a voltagem da sonda para pH com compensação da T do ar
        sensor.requestTemperatures();
        temperaturaAgua = sensor.getTempCByIndex(0);
        
        Serial.print("temperatura ar: ");
        Serial.print(temperature,1);
        Serial.print("^C     pH tanque: ");
        Serial.print(phValue,2);
        Serial.print("      temperatura tanque: ");     
        Serial.println(temperaturaAgua,1);
        delay(10000);
    }
    ph.calibration(voltage,temperature);           // Calibração pode ser ajustada pelo cmd serial
}



{
  
}

}
