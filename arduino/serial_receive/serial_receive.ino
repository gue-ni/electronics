

int number;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  Serial
  

}

void loop() {
  // put your main code here, to run repeatedly:
  if (Serial.available()){
    number = Serial.read()
    Serial.write(number);
  }

}
