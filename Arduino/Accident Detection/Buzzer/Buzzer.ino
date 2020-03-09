
int buzzer = 5;

void setup() {
  pinMode(buzzer,OUTPUT);

}

void loop() {
  digitalWrite(buzzer,HIGH);
  delay(3000);
  digitalWrite(buzzer,LOW);
  delay(3000);

}
