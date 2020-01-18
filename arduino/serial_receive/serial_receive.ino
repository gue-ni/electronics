
  
void setup(){
    Serial.begin(9600);
}
 
void loop(){
    if (Serial.available()) {
        uint8_t nr = Serial.read();
        //Serial.print("Folgender char wurde empfangen: ");
        //Serial.println(nr, BIN);
        Serial.write(nr);
        Serial.write(nr+1);
    }
}
