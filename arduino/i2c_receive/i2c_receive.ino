#include <Wire.h>
#include <LiquidCrystal.h>

#define LINE 16
#define adresse 0x05

uint8_t number = 0;
uint8_t last_number = 0;
uint8_t last_line = 0;
uint8_t line = 0;

char line0[LINE];
char line1[LINE];
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
  print_time(last_number, last_line);
}

void print_time(uint8_t number, uint8_t line){
    if (number < 10){
    lcd.setCursor(15,line);
  } else if(number < 100) {
    lcd.setCursor(14,line);
  } else {
    lcd.setCursor(13,line);
  }
  lcd.print(number);
  
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
    last_number = number;
    number = Wire.read();
    last_line = line;
    line = number >> 7; // first bit of byte is line number
    number &= 0x7f;
    Serial.print("Data received: ");
    Serial.print(number);
    Serial.print(", writing to line: ");
    Serial.println(line);
  }
}

void sendData() {
  clear_display();
  print_time(number, line);
  Wire.write(number);
  
  
  
  
}
