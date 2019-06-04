#include <Streaming.h>
#include <string.h>

int check_btn = 2;
int led = 52;

String input_str, braille;
bool first_out[24] = {0};
bool second_out[24] = {0};
int cnt, str_len, letter_division_index; 
void power();
void __init__()
{
  first_out[24] = {0};
  second_out[24] = {0};
  cnt = 0;  
}

void convert_int(String braille, bool out[])
{
  for (int i = 0; i < braille.length(); i++)
  {
    // Serial<<"cnt : "<<cnt << " "<<"out[cnt] : " << out[cnt]<< " "<<"i : "<<i<<endl;
    if (braille[i] == '0')
      out[cnt] = 0;

    else if (braille[i] == '1')
      out[cnt] = 1;

    cnt++;
  }
}


void setup()
{
  Serial.begin(9600);
  pinMode(led, OUTPUT); // LED 연결
  pinMode(check_btn, INPUT_PULLUP); // LED 연결
} 
void loop()
{
  //  통신 시작
  while (Serial.available())
  {
    __init__(); // 초기화
    input_str = Serial.readStringUntil('\n');
    str_len = input_str.length();
    
    // Serial << input_str << endl;

    if (input_str[0] == 'Q') // 정상적인 데이터
    {
      String letter1 = " ";
      String letter2 = " ";
      /**/
      /*글자단위로 나누기*/
      /**/
      //마지막 글자 
      if (input_str[str_len-1] == 'E')
      {
        // Serial << "Last letter" << endl;
        // Serial<<"1"<<endl;
        letter_division_index = input_str.indexOf("#");

        // 마지막 글자가 한 글자가 아닌경우
        if (letter_division_index != -1)
        {
          // Serial<<"2"<<endl;
          // Serial << letter_division_index << endl;
          letter1 = input_str.substring(1, letter_division_index);
          letter2 = input_str.substring(letter_division_index + 1, str_len);
          // Serial << letter1 << " " << letter2 << endl;
        }

        // 마지막 신호가 한 글자인 경우
        else
        {
          // Serial<<"3"<<endl;
          int end_index = input_str.indexOf("E");
          letter1 = input_str.substring(1, end_index);
          // Serial << letter1 << endl;
        }
      }

      // 마지막 글자가 아닐 경우
      else
      {
        // Serial<<"4"<<endl;
        letter_division_index = input_str.indexOf("#");
        letter1 = input_str.substring(1, letter_division_index);
        letter2 = input_str.substring(letter_division_index + 1, str_len);
      }

      /**/
      /*초성 중성 종성 나누기*/
      /**/

      /**/
      /*첫글자 나누기*/
      /**/
      // Serial << "first letter : " << letter1 << endl;
      int char_index = 0;
      cnt = 0;
      while (1)
      {
        //char_index : 형태소 구분자(/)
        char_index = letter1.indexOf("/");
        //마지막 형태소일 경우
        if (char_index == -1)
        {
          braille = letter1.substring(char_index + 1, str_len - 1);
          // 배열에 정수형으로 저장하기
          // Serial<<"last"<<endl;
          convert_int(braille, first_out);
          break;
        }
        //마지막 형태소가 아닐 경우
        else
        {
          braille = letter1.substring(0, char_index);
          letter1 = letter1.substring(char_index + 1, str_len - 1);
          // 배열에 정수형으로 저장하기
          // Serial<<"not last"<<endl;
          convert_int(braille, first_out);
        }
      }
      /**/
      /*두번째글짜 나누기*/
      /**/
      cnt = 0;
      if (letter2 != " ")
      {
        char_index = 0;
        // Serial << "second letter : " << letter2 << endl;
        while (1)
        {
          char_index = letter2.indexOf("/");
          if (char_index == -1)
          {
            braille = letter2.substring(char_index + 1, str_len - 1);
            // 배열에 정수형으로 저장하기
            convert_int(braille, second_out);
            break;
          }
          else
          {
            braille = letter2.substring(0, char_index);
            letter2 = letter2.substring(char_index + 1, str_len - 1);
            // 배열에 정수형으로 저장하기
            convert_int(braille, second_out);
          }
        }
      }
      /**/
      /*first out, seconde : 출력 내용*/
      /**/
      // for (int i = 0; i < 24; i++)
      //   Serial << first_out[i] << " ";
      // Serial << endl;
      // for (int i = 0; i < 24; i++)
      //   Serial << second_out[i] << " ";
      // Serial << endl;
      power();   
      while(1){
        if(digitalRead(check_btn) == LOW){  
          Serial<<"1"<<endl; 
          delay(1000);
          break;
        }         
      } 
    }
    //정상적인 데이터 끝
    else
    { // 비정상적인 데이터
      Serial << "Not valid data" << endl;
    }
  }
  //  통신 끝
} 
void power()
{ 
  if (first_out[0] == 1)
  {
    digitalWrite(led, HIGH);
  }
  else
  {
    digitalWrite(led, LOW);
  }

  if (first_out[1] == 1)
  {
    digitalWrite(3, HIGH);
  }
  else
  {
    digitalWrite(3, LOW);
  }

  if (first_out[2] == 1)
  {
    digitalWrite(4, HIGH);
  }
  else
  {
    digitalWrite(4, LOW);
  }
  if (first_out[3] == 1)
  {
    digitalWrite(5, HIGH);
  }
  else
  {
    digitalWrite(5, LOW);
  }
  if (first_out[4] == 1)
  {
    digitalWrite(6, HIGH);
  }
  else
  {
    digitalWrite(6, LOW);
  }
  if (first_out[5] == 1)
  {
    digitalWrite(7, HIGH);
  }
  else
  {
    digitalWrite(7, LOW);
  } 
}