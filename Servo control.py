{\rtf1\ansi\ansicpg1252\deff0\nouicompat\deflang1033{\fonttbl{\f0\fnil\fcharset0 Calibri;}}
{\*\generator Riched20 10.0.22000}\viewkind4\uc1 
\pard\sa200\sl276\slmult1\f0\fs22\lang9 // Includes the Servo library\par
#include <Servo.h>. \par
// Defines Tirg and Echo pins of the Ultrasonic Sensor\par
const int trigPin = 10;\par
const int echoPin = 11;\par
// Variables for the duration and the distance\par
long duration;\par
int distance;\par
Servo myServo; // Creates a servo object for controlling the servo motor\par
void setup() \{\par
  pinMode(trigPin, OUTPUT); // Sets the trigPin as an Output\par
  pinMode(echoPin, INPUT); // Sets the echoPin as an Input\par
  Serial.begin(9600);\par
  myServo.attach(12); // Defines on which pin is the servo motor attached\par
\}\par
void loop() \{\par
  // rotates the servo motor from 15 to 165 degrees\par
  for(int i=15;i<=165;i++)\{  \par
  myServo.write(i);\par
  delay(30);\par
  distance = calculateDistance();// Calls a function for calculating the distance measured by the Ultrasonic sensor for each degree\par
  \par
  Serial.print(i); // Sends the current degree into the Serial Port\par
  Serial.print(","); // Sends addition character right next to the previous value needed later in the Processing IDE for indexing\par
  Serial.print(distance); // Sends the distance value into the Serial Port\par
  Serial.print("."); // Sends addition character right next to the previous value needed later in the Processing IDE for indexing\par
  \}\par
  // Repeats the previous lines from 165 to 15 degrees\par
  for(int i=165;i>15;i--)\{  \par
  myServo.write(i);\par
  delay(30);\par
  distance = calculateDistance();\par
  Serial.print(i);\par
  Serial.print(",");\par
  Serial.print(distance);\par
  Serial.print(".");\par
  \}\par
\}\par
// Function for calculating the distance measured by the Ultrasonic sensor\par
int calculateDistance()\{ \par
  \par
  digitalWrite(trigPin, LOW); \par
  delayMicroseconds(2);\par
  // Sets the trigPin on HIGH state for 10 micro seconds\par
  digitalWrite(trigPin, HIGH); \par
  delayMicroseconds(10);\par
  digitalWrite(trigPin, LOW);\par
  duration = pulseIn(echoPin, HIGH); // Reads the echoPin, returns the sound wave travel time in microseconds\par
  distance= duration*0.034/2;\par
  return distance;\par
\}\par
}
 