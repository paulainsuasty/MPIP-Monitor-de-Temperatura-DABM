int ps;
void setup() {
  // put your setup code here, to run once:
  
  pinMode(8, OUTPUT);
  pinMode(9, OUTPUT);
  pinMode(10, OUTPUT);
  Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
  ps = random(20,45);
  Serial.println(ps);
  delay(500);

  char lecturaSerial = Serial.read();
  if (lecturaSerial == 'H'){
    digitalWrite(8, HIGH);
    digitalWrite(9, LOW);
    digitalWrite(10,LOW);
    delay(200);
  }

  else if (lecturaSerial == 'N'){
    digitalWrite(8, LOW);
    digitalWrite(9, HIGH);
    digitalWrite(10,LOW);
    delay(200);
  }

  else if (lecturaSerial == 'F'){
    digitalWrite(8, LOW);
    digitalWrite(9, LOW);
    digitalWrite(10,HIGH);
    delay(200);
  }
}
