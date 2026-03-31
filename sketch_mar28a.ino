#include "LowPower.h"

int ledPin = 2;
int pinLDR = A0;
int LDRValue = 0;
int batasCahaya = 150;
int timer = 0;

void setup() {
  Serial.begin(9600);
  pinMode(LED_BUILTIN, OUTPUT);
  pinMode(ledPin, OUTPUT);
  pinMode(pinLDR, INPUT);
}

void loop() {
  LDRValue = analogRead(pinLDR);
  LDRValue = map(LDRValue,0,1023,1023,0);
  Serial.println(LDRValue);
  delay(500);

  if(LDRValue < batasCahaya){ /*Gelap*/
    digitalWrite(ledPin, HIGH);
    if(timer<30){
      delay(1000);
      timer++;
      Serial.println("Menghitung : " + String(timer));
    }else{
      LowPower.powerDown(SLEEP_8S, ADC_OFF, BOD_OFF);
      Serial.println("Sudah 30 detik..");
    }
  }else{ /*Terang*/
    digitalWrite(ledPin, LOW);
    timer = 0;
    delay(1000);
  }
}
