#include <SoftwareSerial.h>
SoftwareSerial mySerial(9, 10);
String inputString = "";
boolean stringComplete = false; // whether the string is complete
String signal = "$GPGLL";

const int xpin = A3;                  // x-axis of the accelerometer
const int ypin = A2;                  // y-axis
const int zpin = A1;                  // z-axis (only on 3-axis models)

const int buzzer = 13;
int a;
int b;
int c;



 
 void setup() {
  Serial.begin(9600);
  mySerial.begin(9600);
  pinMode(buzzer, OUTPUT); // Set buzzer - pin 9 as an output

  // Provide ground and power by using the analog inputs as normal digital pins.
  // This makes it possible to directly connect the breakout board to the
  // Arduino. If you use the normal 5V and GND pins on the Arduino,
  // you can remove these lines.
}

void loop() {
  a=analogRead(xpin);
  Serial.print(a);
  if(a>350)
  {
    Buzzer();
  }
  
  Serial.print("\t");
  b=analogRead(ypin);
  Serial.print(b);
  if(b>350)
  {
    Buzzer();
  }
  Serial.print("\t");
  c=analogRead(zpin);
  Serial.print(c);
  if(c>350)
  {
    Buzzer();
  }
  Serial.println();
  
  delay(3000);
  Gps(); 
}



void Buzzer(){
  tone(buzzer, 100); // Send 1KHz sound signal...
  delay(1000);        // ...for 1 sec
  noTone(buzzer);     // Stop sound...
  delay(1000);        // ...for 1sec
 }



 void Gsm() {
  Serial.println("SOS Messaging System ...");
  Serial.println("Please Enter 's' for Sending Message and 'r' for receiving");
  Serial.println("");
  
  while(Serial.available() == 0 ) {}
  Serial.println("Processing ... ");
  Serial.println("");
if (Serial.available()>0)
  
   switch(Serial.read())
  {
    case 's':
      mySerial.println("AT+CMGF=1");    //Sets the GSM Module in Text Mode
     delay(1000);  // Delay of 1 second
     mySerial.println("AT+CMGS=\"+919820835824\"\r"); // Replace x with mobile number
     delay(1000);
     
 
     mySerial.println("Emergency Need Help");
     mySerial.println("Current Location of soldier is 27.2038 N, 77.5011 E");
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

 if (mySerial.available()>0)
   Serial.write(mySerial.read());
}

void Gps()
{
  if (stringComplete) {
        String BB = inputString.substring(0, 6);
        if (BB == signal) {
            String LAT = inputString.substring(7, 17);
            int LATperiod = LAT.indexOf('.');
            int LATzero = LAT.indexOf('0');
            if (LATzero == 0) {
                LAT = LAT.substring(1);
            }

            String LON = inputString.substring(20, 31);
            int LONperiod = LON.indexOf('.');
            int LONTzero = LON.indexOf('0');
            if (LONTzero == 0) {
                LON = LON.substring(1);
            }

            Serial.println(LAT);
            Serial.println(LON);

        }

        // Serial.println(inputString);
        // clear the string:
        inputString = "";
        stringComplete = false;
    }
//    else {
//        Serial.println("");
//      Serial.println("Current Location of soldier is 27.2038° N, 77.5011° E");
//    }
}
