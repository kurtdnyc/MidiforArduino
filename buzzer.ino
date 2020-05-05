#include "periods.h"

int melody[];
int beats[]  = { 16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16 };
int noteDurations[] = { 8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8 };
int MAX_COUNT = sizeof(melody1) / 2; // Melody length, for looping.
int pin1 = 8; //green
int pin2 = 9; //yellow
int pin3 = 11; //orange
int pin4 = 12; //red
int inPin = 0;
int reading =0;
int previous;
boolean breakme = false;
long time = 0;         // the last time the output pin was toggled
long debounce = 200;
// Set overall tempo
long tempo = 10000;
// Set length of pause between notes
int pause = 1000;

int rest_count = 100;
int tone_ = 0;
int tone_2 = 0;
int tone_3 = 0;
int tone_4 = 0;
int beat = 0;
long duration  = 0;
int DEBUG =1;
int formultiple = 1;
void setup()
{
 pinMode(pin1, OUTPUT);
 pinMode(pin2, OUTPUT);
 delay(500);
 boolean finalAnswer = waitfor('k',200,60);
  if (finalAnswer)
  {
    Serial.println("K");
    detonate = false;
    Serial.end();
  }
}

void readChar(int polltime)
{
   delayMicroseconds(200);
   if (Serial.available() > 0)
  {
    for (int j = 0; j < 100000; j++)
    {
     inputChar = Serial.read();
     if (inputChar ==expected)
     {
        goto here
     }
     melody[j] = inputChar;
    }
   here:
   hasTyped = true;
  }

}


void analyze(char expected) {
 if (hasTyped == true)
 {

    if(inputChar == expected)
    {
      breakMe = true;
      answer = true;
      hasTyped = false;
    }
 }
}

boolean waitfor(char expected, int polltime, int timeout)
{
  int t=timeout;
  while(!breakMe)
  {
    delay(1000);
    t--;
    if (t == 0)
    {
      breakMe = true;
      Serial.println("Timed out");
      Serial.end();
    }
    readChar(polltime);
    analyze(expected);
  }
  breakMe=false;

  return answer;
}

void playTone()
{
  long elapsed_time = 0;
  if (tone_ > 0) {

    while (elapsed_time < duration) {

      digitalWrite(pin1,HIGH);
      delayMicroseconds(tone_ / 2);
      digitalWrite(pin1, LOW);
      delayMicroseconds(tone_ / 2);




      elapsed_time += (tone_);
    }
  }
  else {
    for (int j = 0; j < rest_count; j++) {
      delayMicroseconds(duration);
    }
  }
}
void loop()
{
    boolean finalAnswer = waitfor('?',200,60);
    if (finalAnswer)
    {
        Serial.println("K");
        detonate = false;
        play = true;
    }
    if (play)
    {
      for (int i=0; i<MAX_COUNT; i++)
      {
        tone_ = melody[i];

        beat = 32;

        duration = beat * tempo;

        playTone();

        delayMicroseconds(pause);

      }
    }
}