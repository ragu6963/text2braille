#include <Streaming.h>
#include <string.h>
#define max_length 24

int check_btn = 46;
int led[max_length] = {22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45};
void LED_state(int braille[]);
void braille_print(int braille[]);
void setup()
{
  Serial.begin(9600);
  for (int i = 0; i < max_length; i++)
    pinMode(led[i], OUTPUT);
  pinMode(check_btn, INPUT_PULLUP);
}

void loop()
{
  while (Serial.available())
  {
    String input_str = Serial.readStringUntil('\n');
    Serial << input_str<<endl;
    int braille[max_length] = {
        0,
    };
    int str_len = input_str.length();
    int j = 0;
    for (int i = 0; i < str_len; i++)
    {
      if (input_str[i] == '1')
        braille[j++] = 1;
      else if (input_str[i] == '0')
        braille[j++] = 0;
    }
    // braille_print(braille);
    while (1)
    {
      LED_state(braille);
      // delay(5000)
      // Serial << "1" << endl;

      if (digitalRead(check_btn) == LOW)
      {
        Serial << "1" << endl;
        delay(1000);
        break;
      }
    }
  }
}

void braille_print(int braille[])
{
  for (int i = 0; i < max_length; i++)
  {
    Serial<<  "braille[" <<i<<"] = "<< braille[i]<< endl;
  }
}
void LED_state(int braille[])
{
  for (int i = 0; i < max_length; i++)
  {
    if (braille[i] == 1)
      digitalWrite(led[i], HIGH);
    else if (braille[i] == 0)
      digitalWrite(led[i], LOW);
  }
}