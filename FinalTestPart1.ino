LED = 2;
void setup() {
  Serial.begin(9600);
  pinMode(LED, OUTPUT);
}

void loop() {
  if (Serial.available() > 0) {   //if there is data going to serial
    inByte = Serial.read();       //gets data in serial
    if (inByte == 'H') {          //if that data is 'H'
      digitalWrite(LED, HIGH);    //turn LED on
    }
    if (inByte == 'L') {          //if that data is 'L'
      digitalWrite(LED, LOW);     //turn LED off 
    }
  }
}
