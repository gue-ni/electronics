#include <Wire.h>
#include <LiquidCrystal.h>

#define adress 0x05
#define BUFSIZE (5)
#define LINE0_NOW   1
#define LINE0_NEXT  2
#define LINE1_NOW   3
#define LINE1_NEXT  4


uint8_t buf[BUFSIZE];
const int rs = 12, en = 11, d4 = 5, d5 = 4, d6 = 3, d7 = 2;
LiquidCrystal lcd(rs, en, d4, d5, d6, d7);

void setup() {
  Serial.begin(9600);
  Serial.println("Ready");
  
  Wire.begin(adress);
  Wire.onReceive(receiveData);
  Wire.onRequest(sendData);
  Serial.begin(9600);
  memset(buf, 0, BUFSIZE);
  lcd.begin(16,2);
  

}

void print_time(uint8_t number, uint8_t line)
{
  if (number < 10){
    lcd.setCursor(15,line);
  } else if(number < 100) {
    lcd.setCursor(14,line);
  } else {
    lcd.setCursor(13,line);
  }
  lcd.print(number);
}

void setup_display(){
  lcd.clear();
  lcd.setCursor(0,0);
  lcd.print("1 City");
  lcd.setCursor(0,1);
  lcd.print("1 Prater");
  
}


void loop() {
    setup_display();
    print_time(buf[LINE0_NOW], 0);
    print_time(buf[LINE1_NOW], 1);
    delay(5000);
    
    setup_display();
    print_time(buf[LINE0_NEXT], 0);
    print_time(buf[LINE1_NEXT], 1);
    delay(5000);    
}

void receiveData(int bytes)
{

  Serial.println("Read: ");
  int bytesRead = Wire.available();
  for (int i = 0; i< bytesRead; i++){
    buf[i] = Wire.read();
    Serial.println(buf[i]);
  }  
}

void sendData(){
  Wire.write(buf, BUFSIZE);
  Serial.println("Sending data"); 
  
}
