// Sensoriamento Mestrado versão 0.0.1 - Joni Gund - Outubro 2021

#include <OneWire.h>
#include <DallasTemperature.h>

OneWire onewire(4);
DallasTemperature sensor(&onewire);
float temperatura;

void setup() {
  Serial.begin(9600);
  sensor.begin();

}

void loop() {
  sensor.requestTemperatures();
  temperatura = sensor.getTempCByIndex(0);
  Serial.println(temperatura);
  delay(10000);

}
