#include <Streaming.h>
#include <string.h>
#define max_length 24

int btnNext = 46;
int motor[max_length] = {22, 24, 26, 23, 25, 27, 
                        28, 30, 32, 29, 31, 33, 
                        34, 36, 38, 35, 37, 39, 
                        40, 42, 44, 41, 43, 45};
int braille[max_length] = {
    0,
};

String binary_str = "";

void Motor_power();
void Motor_off();
void setup()
{ 
  Serial.begin(9600);
  Serial.println("Hello!");
  Serial1.begin(9600);
  for (int i = 0; i < max_length; i++)
    pinMode(motor[i], OUTPUT);
  pinMode(btnNext, INPUT_PULLUP);
}

void loop()
{
//  if (Serial.available())
//  {
//    binary_str = Serial.readStringUntil('\n');
//    
//    for(int i = 0 ; i < max_length ; i++){
//      braille[i] = 0;
//    }
//
//    int j = 0;
//    for (int i = 0; i <  binary_str.length(); i++)
//    {
//      if (binary_str[i] == '1'){
//        braille[j] = 1;
//        j++;
//      }
//      else if (binary_str[i] == '0'){
//        braille[j] = 0;
//        j++;
//      }
//    } 
//    while (1)
//    {
//      Motor_power();
//      if (digitalRead(btnNext) == LOW)
//      {
//        Serial << "q" << endl;
//        delay(1000);
//        Motor_off();
////        delay(3000);
//        break;
//      }
//    }
//  }
  
  if (Serial1.available())
  {
    binary_str = Serial1.readStringUntil('\n');
    for (int i = 0; i < max_length; i++)
    {
      braille[i] = 0;
    }
    int textLen = binary_str.length();
    int j = 0;
    for (int i = 0; i < textLen; i++)
    {
      if (binary_str[i] == '1')
      {
        braille[j] = 1;
        j++;
      }
      else if (binary_str[i] == '0')
      {
        braille[j] = 0;
        j++;
      }
    }
    while (1)
    {
      Motor_power();
      if (digitalRead(btnNext) == LOW)
      {
        Serial1.print("q\r\n");
        Motor_off();
        delay(1000);
//        delay(3000);
        break;
      }
    }
  }
}

void Motor_power()
{
  for (int i = 0; i < max_length; i++)
  {
    if (braille[i] == 1)
      digitalWrite(motor[i], HIGH);
    else if (braille[i] == 0)
      digitalWrite(motor[i], LOW);
  }
}
void Motor_off(){
  for (int i = 0 ; i<max_length;i++){
    digitalWrite(motor[i],LOW);
  }
}
 
