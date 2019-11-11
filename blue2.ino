
#include<Streaming.h>
#include<string.h>
#define max_length 24

int btnNext = 46;
int motor[max_length] = {22, 23, 24, 25, 26, 27,28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39,40,41,42,43,44,45};
int braille[max_length] = {0,}; 

String textInput = ""; 

void Motor_power();
void Motor_off();
void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  Serial.println("Hello!");
  Serial1.begin(9600);
  for (int i = 0; i < max_length; i++)
    pinMode(motor[i], OUTPUT);
  pinMode(btnNext, INPUT_PULLUP);
}
 
void loop() { 

  while(Serial1.available()){
    textInput = Serial1.readStringUntil('\n');
    for(int i = 0 ; i < max_length ; i++){
      braille[i] = 0;
    }
    int textLen = textInput.length();
    int j = 0;
    for (int i = 0; i < textLen; i++)
    {
      if (textInput[i] == '1'){
        braille[j] = 1;
        j++;
      }
      else if (textInput[i] == '0'){
        braille[j] = 0;
        j++;
      }
    }
    while (1)
    {
//      Motor_power();
      if (digitalRead(btnNext) == LOW)
      { 
        Serial1.print("q\r\n");
//        Motor_off();
        delay(3000);
        break;
      }
    } 
  }
}



  
  // put your main code here, to run repeatedly:
  // 블루투스 수신
//  if (Serial1.available()) {
//    Serial.write(Serial1.read());
//  }
//  
//  // Serial –> Data –> BT
//  // 블루투스 송신
//  if (Serial.available()) {
//    char s = (char)Serial.read();
//    Serial1.print(s); 
// }
//}
 
