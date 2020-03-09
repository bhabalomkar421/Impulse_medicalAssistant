#include <RH_ASK.h>
#ifdef RH_HAVE_HARDWARE_SPI
#include <SPI.h> 
#endif

// connect data to pin 2
// ( Speed, receving pin , Transmitting pin , push to talk)
RH_ASK driver(2000, 4, 2, 5);
void setup()
{
#ifdef RH_HAVE_SERIAL
    Serial.begin(9600);    
#endif
    if (!driver.init())
#ifdef RH_HAVE_SERIAL
         Serial.println("init failed");
#else
  ;
#endif
}

void loop()
{
    const char *msg = "hello God";

    driver.send((uint8_t *)msg, strlen(msg));
    driver.waitPacketSent();
    delay(200);
} 
