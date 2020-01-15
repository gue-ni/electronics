#include <Wire.h>
#include <LiquidCrystal.h>

#define adresse 0x05
uint8_t number = 0;
uint8_t old_number = 0;
uint8_t line = 0;
const int rs = 12, en = 11, d4 = 5, d5 = 4, d6 = 3, d7 = 2;
LiquidCrystal lcd(rs, en, d4, d5, d6, d7);

void setup_display(){
  lcd.clear();
  lcd.print("S. F.-Platz");
  lcd.setCursor(0,1);
  lcd.print("Prater HA");
}

void clear_display(){
  setup_display();
  print_time(old_number, line == 0 ? 1 : 0);
}

void print_time(uint8_t number, uint8_t line){
    if (number < 10){
    lcd.setCursor(15,line);
  } else {
    lcd.setCursor(14,line);
  }
  lcd.print(number);
  
}

void print_wait_time(uint8_t wait_time){
  print_time(wait_time, line);
  
  if (line == 0){
    line = 1;
  } else {
    line = 0;
  }
}

void setup() {
  lcd.begin(16,2);
  setup_display();
  
  Serial.begin(9600);
  Wire.begin(adresse);
  Wire.onReceive(receiveData);
  Wire.onRequest(sendData);
  Serial.println("Ready");
}

void loop() {
  delay(100);
}

void receiveData(int byteCount) {
  while (Wire.available()) {
    old_number = number;
    number = Wire.read();
    Serial.print("Data received: ");
    Serial.println(number);
  }
}

void sendData() {
  Wire.write(number);
  clear_display();
  print_wait_time(number);
  
  
  
  
}
