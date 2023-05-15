// Sensoriamento Mestrado versão 0.0.3 - Joni Gund - Outubro 2021

// inclusão das bibliotecas
#include <OneWire.h>
#include <DallasTemperature.h>

OneWire onewire(4);
DallasTemperature sensor(&onewire);
float temperaturaAgua;

#include "DFRobot_PH.h"
#include <EEPROM.h>
#include <LiquidCrystal_I2C.h>

#define PH_PIN A1
float voltage,phValue,temperature = 25;
DFRobot_PH ph;

LiquidCrystal_I2C lcd(0x27,16,2);

//inicializacao dos sensores e demais componentes
void setup() {
  Serial.begin(9600);
  sensor.begin();
  ph.begin();
  lcd.init();
}

//rotina da leitura
void loop() {
{
   static unsigned long timepoint = millis();
    if(millis()-timepoint>30000U){                  //intervalo: 10s=1000U    5min=30000U
        timepoint = millis();                       //Tipo de intervalo de leitura
        //temperature = readTemperature();           // Lê a temperatura do ar pelo sensor do módulo pH para fazer a compensação
        voltage = analogRead(PH_PIN)*2.7;  // Lê a voltagem da sonda       /1024.0*5000
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

        lcd.backlight();
        lcd.setCursor(0,0);
        lcd.print("T Agua:");
        lcd.setCursor(10,0);
        lcd.print(temperaturaAgua);
        lcd.setCursor(0,1);
        lcd.print("pH Agua:");
        lcd.setCursor(10,1);
        lcd.print(phValue);
        
    }
    ph.calibration(voltage,temperature);           // Calibração pode ser ajustada pelo cmd serial
}
{
}
}
