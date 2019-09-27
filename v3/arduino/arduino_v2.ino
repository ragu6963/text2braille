#include <Streaming.h>
#include <string.h>
#define max_length 18
int check_btn = 46;
int motor[max_length] = {22, 23, 24, 25, 26, 27,28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39};
int braille[max_length] = {0,};
String input_str;
void Motor_power();
void Motor_off();
void setup()
{
  Serial.begin(9600);
  for (int i = 0; i < max_length; i++)
    pinMode(motor[i], OUTPUT);
  pinMode(check_btn, INPUT_PULLUP);
}

void loop()
{
  while (Serial.available())
  {
    input_str = Serial.readStringUntil('\n');
    for(int i = 0 ; i < max_length ; i++){
      braille[i] = 0;
    }
    int str_len = input_str.length();
    int j = 0;
    for (int i = 0; i < str_len; i++)
    {
      if (input_str[i] == '1'){
        braille[j] = 1;
        j++;
      }
      else if (input_str[i] == '0'){
        braille[j] = 0;
        j++;
      }
    }
    while (1)
    {
      Motor_power();
      if (digitalRead(check_btn) == LOW)
      {
        Serial << "q" << endl;
        Motor_off();
        delay(3000);
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