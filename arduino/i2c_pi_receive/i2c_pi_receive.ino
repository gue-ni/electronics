#include <Wire.h>

#define adress 0x05
#define BUFSIZE (2)

uint8_t buf[BUFSIZE];

void setup() {
  Serial.begin(9600);
  Serial.println("Ready");
  Wire.begin(adress);
  Wire.onReceive(receiveData);
  Wire.onRequest(sendData);

}

void loop() {
  delay(100);
}

void receiveData(int bytes)
{
  Serial.print("Received: ");
  Serial.println(bytes);

  for (int i = 0; i < bytes && bytes <= BUFSIZE; i++){
    buf[i] = Wire.read();
  }
  Serial.print("Read: ");
  Serial.println(buf[0]);
  
}

void sendData(){
  buf[0] = 0x47;
  buf[1] = 0x48;
  Wire.write(buf, BUFSIZE);
  Serial.println("Sending data"); 
}
