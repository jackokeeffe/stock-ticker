/*
    PROJECT  : Project 2.7. Long ISP: The Stock Market Ticker
    PURPOSE  : Recieve & display stock information on LED matrix
    DATE     : 2021 05 29
    MCU      : 328P
    STATUS   : Working
    NOTES    : None
    REFERENCE: http://darcy.rsgc.on.ca/ACES/TEI3M/2021/ISPs.html
*/

#include <MD_Parola.h>

#define HARDWARE_TYPE MD_MAX72XX::FC16_HW // Device type of matrix (given)
uint8_t devicesUsed = 4;                  // # of LED Matrices
uint8_t csPin = 10;                       // Pin CS on Matrix is connected to

MD_Parola md = MD_Parola(HARDWARE_TYPE, csPin, devicesUsed);  //Create MD_Parola object for use

void setup() {
  md.begin();               // Start MD_Parola for use
  Serial.begin(9600);       // Start Serial Monitor with baud 9600
  Serial.println("Ready");  // Let user know (in Python) when ready
}
void loop() {
  if (Serial.available()) {               // Check if data has been sent
    String message = Serial.readString(); // Get stock info sent as message var
    Serial.println(message);              // Print so it can be seen in python terminal

    // Scrolling text on screen
    int stringLength = (message.length() - 5);  //Doesn't keep scrolling after whole message has been seen
    while (stringLength > 0) {        // While the string still has characters
      md.print(message);              // Print message to LED Matrix
      delay(500);                     // Wait 0.5s
      message = message.substring(1); // Remove first letter from string (to look like scrolling)
      stringLength --;                // Adjust stringLength for removed letter
    }
    delay(1500);   // Wait 1.5s to ensure user can read all data shown (on LCD)
  }
}
