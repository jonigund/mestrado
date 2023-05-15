// Sensoriamento Mestrado versão 0.0.1 - Joni Gund - Outubro 2021

#include <OneWire.h>
#include <DallasTemperature.h>

OneWire onewire(4);
DallasTemperature sensor(&onewire);
float temperatura;

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
        timepoint = millis();
        //temperature = readTemperature();           // read your temperature sensor to execute temperature compensation
        voltage = analogRead(PH_PIN)/1024.0*5000;  // read the voltage
        phValue = ph.readPH(voltage,temperature);  // convert voltage to pH with temperature compensation
        sensor.requestTemperatures();
        temperatura = sensor.getTempCByIndex(0);
        
        Serial.print("temperatura ar: ");
        Serial.print(temperature,1);
        Serial.print("^C     pH tanque: ");
        Serial.print(phValue,2);
        Serial.print("      temperatura tanque: ");     
        Serial.println(temperatura,1);
        delay(10000);
    }
    ph.calibration(voltage,temperature);           // calibration process by Serial CMD
}



{
  
}

}
