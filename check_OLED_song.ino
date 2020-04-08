/*********************************************************************

This is an example for our Monochrome OLEDs based on SSD1306 drivers

Buy OLED Here :
  ------> http://www.roboindia.com

We are using Adafruit Library 

*********************************************************************/

#include <SPI.h>
#include <Wire.h>
#include <Adafruit_GFX.h>
#include <Adafruit_SSD1306.h>

#define OLED_RESET 4
Adafruit_SSD1306 display(OLED_RESET);

#if (SSD1306_LCDHEIGHT != 64)
#error("Height incorrect, please fix Adafruit_SSD1306.h!"); // If this is the error that means
#endif
int a=1; // global variable

void setup()   
{  
  Serial.begin(9600);
 
  // by default, we'll generate the high voltage from the 3.3v line internally! (neat!)
  display.begin(SSD1306_SWITCHCAPVCC, 0x3C);  // initialize with the I2C addr 0x3C (for the 128x64)
  // Check your I2C address and enter it here, in Our case address is 0x3C
  
  // Show image buffer on the display hardware.
  // Since the buffer is intialized with an Adafruit splashscreen
  // internally, this will display the splashscreen.
 

  // Clear the buffer.
  display.clearDisplay();
 
  display.setTextSize(3); // You can select text size ex- 1, 2, 3 and so on 
  display.setTextColor(WHITE); // This will display Bright character on Black background
  display.setCursor(5,0); // You are setting the cursor as per your requirement. In short its the co-ordinates in display from where data will display
  display.println("HELLO"); // String which you are printing
  Serial.println("Hello");
  display.setTextSize(2);
  display.setTextColor(WHITE, BLACK); // Here you print 'Black character' on 'Bright Background'
  display.setCursor(12,40);
  display.println("WELCOME");
  Serial.println("WELCOME");
  display.display(); // this command will display all the data which is in buffer
  delay(2000);
  display.clearDisplay(); // clear the buffer 
  display.setTextSize(2);
  display.setTextColor(WHITE);
  display.setCursor(13,10);
  display.println("Hope you don't feel lonely");
  Serial.println("Hope you don't feel lonely");
  
  display.display(); // this command will display all the data which is in buffer
  delay(5000);
  display.clearDisplay(); // clear the buffer 
}

void loop() { 
  display.clearDisplay();
  a=random(50,500);
  //a=485;
  display.setTextSize(2);
  display.setTextColor(WHITE);
  display.setCursor(5,10);
  display.println("Device    reads:");
  Serial.println("Your Conductivity is");
  display.setTextSize(2);
  display.setTextColor(WHITE);
  display.setCursor(40,44);
  display.println(a);
  Serial.println(a);  
  display.display(); // this command will display all the data which is in buffer
  delay(3000);
  display.clearDisplay(); // clear the buffer 
  /*if(a>10){a=0;} // This loop will make counter 0 again after reaching maximum value 10
  display.drawPixel(127, 63, WHITE); // This command will help you to print a pixel on display , its the last pixel, coordinate 127,63
  display.drawPixel(0, 0, WHITE); // pixel with 0,0 coordinate*/
  if(a<430 && a>350)
  {
  display.setTextSize(2);
  display.setTextColor(WHITE);
  display.setCursor(10,0);
  display.println("Getting  disturbed??");
  Serial.println("Getting distured???");
  display.setCursor(10,40);
  display.setTextSize(2);
  display.println("RELAX...."); // printing a variable
  Serial.println("RELAX....");
  display.display(); // this command will display all the data which is in buffer
  delay(2000);
  display.clearDisplay(); // clear the buffer
  display.setCursor(10,10);
  display.setTextSize(3);
  display.println("stay   CALM"); // printing a variable
  Serial.println("stay CALM");
  display.display(); // this command will display all the data which is in buffer
  delay(4000);
  display.clearDisplay(); // clear the buffer
  display.setCursor(0,10);
  display.setTextSize(2);
  display.println("Deviate   your"); // printing a variable
  display.setTextSize(3);
  display.println("Thought"); 
  Serial.println("Thoughts");
  display.display();
  delay(5000);
  display.clearDisplay(); // clear the buffer 
  }
  if(a<350 && a>200)
  {
    display.setTextSize(1);
  display.setTextColor(WHITE);
  display.setCursor(10,0);
  display.println("What happend?");
  Serial.println("What happend?");
  display.setCursor(10,20);
  display.setTextSize(2);
  display.println("LOST IN  THOUGHTS"); // printing a variable
  Serial.println("LOST IN THOUGHTS");
  display.display(); // this command will display all the data which is in buffer
  delay(2000);
  display.clearDisplay(); // clear the buffer
  display.setCursor(10,0);
  display.setTextSize(3);
  display.println("MUSIC LOVER??"); // printing a variable
  Serial.println("MUSIC LOVER??");
  display.display(); // this command will display all the data which is in buffer
  delay(2000);
  display.clearDisplay(); // clear the buffer
  display.setCursor(10,0);
  display.setTextSize(3);
  display.println("Song"); // printing a variable
  Serial.println("Song");
  display.setTextSize(2);
  display.println("specially for you"); // printing a variable
  Serial.println("specially for you");
  display.display(); // this command will display all the data which is in buffer
  delay(2000);
  display.clearDisplay(); // clear the buffer
  display.setCursor(10,10);
  display.setTextSize(3);
  display.println("Song  lyrics"); // printing a variable
  Serial.println("Song lyrics..");
  display.display();
  delay(8000);
  display.clearDisplay(); // clear the buffer 
  }
  if(a<200)
  {
  display.setTextSize(3);
  display.setTextColor(WHITE);
  display.setCursor(10,0);
  display.println("WHY SO SAD?");
  Serial.println("WHY SO SAD?");
  display.display(); // this command will display all the data which is in buffer
  delay(2000);
  display.clearDisplay();
  display.setCursor(5,20);
  display.setTextSize(2);
  display.println("Share your pain"); // printing a variable
  Serial.println("Share your pain");
  display.display(); // this command will display all the data which is in buffer
  delay(2000);
  display.clearDisplay(); // clear the buffer
  display.setCursor(10,10);
  display.setTextSize(3);
  display.println("FIGHT song"); // printing a variable
  Serial.println("Song  Lyrics..");
  display.display(); // this command will display all the data which is in buffer
  delay(8000);
  display.clearDisplay(); // clear the buffer 
  }
  delay(5000);
}
