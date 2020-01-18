#include <LiquidCrystal.h>


#define BUFSIZE     4
#define LINE0_NOW   0
#define LINE0_NEXT  1
#define LINE1_NOW   2
#define LINE1_NEXT  3

uint8_t buf[BUFSIZE];

const int rs = 12, en = 11, d4 = 5, d5 = 4, d6 = 3, d7 = 2;
LiquidCrystal lcd(rs, en, d4, d5, d6, d7);
  
void setup(){
    Serial.begin(9600);
    memset(buf, 0, BUFSIZE);
    lcd.begin(16,2);
}

void setup_display(){
  lcd.clear();
  lcd.setCursor(0,0);
  lcd.print("1 City");
  lcd.setCursor(0,1);
  lcd.print("1 Prater");
  
}


 
void loop(){
  
    if (Serial.available()) {
        Serial.readBytes(buf, BUFSIZE);
        Serial.write(buf, BUFSIZE);
    }
    
    setup_display();
    print_time(buf[LINE0_NOW], 0);
    print_time(buf[LINE1_NOW], 1);
    delay(3000);
    
    setup_display();
    print_time(buf[LINE0_NEXT], 0);
    print_time(buf[LINE1_NEXT], 1);
    delay(3000);    
}
