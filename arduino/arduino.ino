#include <string.h>
#define max_length 24

int blue_led = 8;
int port_led = 6;
int toggle = 53;
int btnNext = 52;
int btnCap = 51;
int motor[max_length] = {
  22, 24, 26, 23, 25, 27,
  28, 30, 32, 29, 31, 33,
  34, 36, 38, 35, 37, 39,
  40, 42, 44, 41, 43, 45
};
String binary_input;
String binary_data;
void Motor_power();
void Motor_off();
void setup()
{
  Serial.begin(9600);
  for (int i = 0; i < max_length; i++)
    pinMode(motor[i], OUTPUT);

  pinMode(blue_led, OUTPUT);
  pinMode(port_led, OUTPUT);
  pinMode(btnNext, INPUT_PULLUP);
  pinMode(btnCap, INPUT_PULLUP);
  pinMode(toggle, INPUT);
}

void loop()
{
  if (digitalRead(toggle) == HIGH)
  {
    //    Serial.println("serial");
    digitalWrite(port_led, HIGH);
    digitalWrite(blue_led, LOW);
    Serial1.end();
    if (digitalRead(btnCap) == LOW)
    {
      Serial.println("p"); 
      delay(3000);
    }
    if (Serial.available()) {
      binary_input = "";
      binary_data = "";
      binary_input = Serial.readStringUntil('\n');
      Serial.println(binary_input);
      for (int i = 0; i < binary_input.length(); i++)
      {
        if (binary_input[i] != '/')
          binary_data += binary_input[i];
      }
      Motor_power(binary_data);
      while (1)
      {
        if (digitalRead(toggle) == LOW)
          break;
        if (digitalRead(btnNext) == LOW)
        {
          Serial.println("q");
          Motor_off();
          delay(1500); 
          break;
        }
        if (digitalRead(btnCap) == LOW)
        {
          Serial.println("p");
          break;
        }
      }
    }
  }
  if (digitalRead(toggle) == LOW)
  {
    digitalWrite(port_led, LOW);
    digitalWrite(blue_led, HIGH);
    Serial1.begin(9600);
    delay(1000);

    if (Serial1.available())
    {
      binary_input = "";
      binary_input = Serial1.readStringUntil('\n');
      Serial.println(binary_input);
      if (!binary_input.compareTo("Q\r"))
      {
        Motor_off();
        Serial1.print("q\r\n");
      }
      else
      {
        binary_data = "";

        for (int i = 0; i < binary_input.length(); i++)
        {
          if (binary_input[i] != '/')
            binary_data += binary_input[i];
        }
        Motor_power(binary_data);
        while (1)
        {
          if (digitalRead(toggle) == HIGH)
            break;
          if (digitalRead(btnNext) == LOW)
          {
            Serial1.print("q\r\n");
            Motor_off();
            delay(1500);
            break;
          }

        }
      }
    }
  }
}

void Motor_power(String binary_data)
{

  for (int i = 0; i < max_length; i++)
  {
    digitalWrite(motor[i], binary_data[i] - '0');
  }
}

void Motor_off()
{
  for (int i = 0; i < max_length; i++)
    digitalWrite(motor[i], LOW);
}
