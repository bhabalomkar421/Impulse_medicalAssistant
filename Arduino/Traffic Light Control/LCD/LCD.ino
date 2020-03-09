#include <LiquidCrystal.h>  
LiquidCrystal lcd(1, 2, 4, 5, 6, 7); 
void setup() { 
 lcd.begin(16,2); 
}
void loop() { 
  lcd.setCursor(2,1);
 lcd.print("cal da bestttc"); 
 delay(3000);
}
