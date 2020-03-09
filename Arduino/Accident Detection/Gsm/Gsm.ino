 #include <SoftwareSerial.h>

SoftwareSerial mySerial(9, 10);

void setup()
{
  mySerial.begin(9600);   // Setting the baud rate of GSM Module  
  Serial.begin(9600);    // Setting the baud rate of Serial Monitor (Arduino)
 
}


void loop()
{
  Gsm();
}


void Gsm() {
  
  Serial.println("SOS Messaging System ...");
  Serial.println("Please Enter 's' for Sending Message and 'r' for receiving");
  Serial.println("");
  while(Serial.available() == 0 ) {}
  Serial.println("Processing ... ");
  Serial.println("");
if (Serial.available()>0)
  {
   switch(Serial.read())
  {
    case 's':
      mySerial.println("AT+CMGF=1");    //Sets the GSM Module in Text Mode
     delay(1000);  // Delay of 1 second
     mySerial.println("AT+CMGS=\"+918169193145\"\r"); 
     delay(1000);
     
     mySerial.println("Emergency Need Help");
     delay(1000);
     mySerial.println((char)26);// ASCII code of CTRL+Z for saying the end of sms to  the module 
      delay(1000);
      Serial.println("SOS Message Send Successfully ");
      
      break;
      
    case 'r':
      mySerial.println("AT+CNMI=2,2,0,0,0"); // AT Command to receive a live SMS
      delay(1000);
      break;

    default:
      Serial.println("Please enter valid input ! ");
  }
  }

// if (mySerial.available()>0)
//   Serial.write(mySerial.read());

}
