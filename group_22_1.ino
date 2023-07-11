/*
  ELEC1100 Your Lab#06 & Project Template

  To program the car tracking the white line on a dark mat

  Group No. (number on your project box):
  Group Member 1 (name & SID): Clement Darmawan SETIABUDHI 20817485
  Group Member 2 (name & SID): Andre CHARLES 20767422

*/

// assign meaningful names to those pins that will be used
const int pinR_Sensor = A3;      //pin A3
const int bumper_Sensor = A4;    //pin A4
const int pinL_Sensor = A5;      //pin A5
const int pinL_PWM = 9;          //pin D9
const int pinR_PWM = 11;         //pin D11
const int pinL_DIR = 10;         //pin D10
const int pinR_DIR = 12;         //pin D12

//define variables to be used in script
int leftSensor = 1;
int bumperSensor = 1;
int rightSensor = 1;
bool hasStarted = false;
int junctionsPassed = 0;
bool enteredSlightBends = false;
bool enteredBend = false;

void setup () {
  // define pins as input and output
  pinMode(pinL_Sensor, INPUT);
  pinMode(bumper_Sensor, INPUT);
  pinMode(pinR_Sensor, INPUT);
  pinMode(pinL_DIR, OUTPUT);
  pinMode(pinR_DIR, OUTPUT);
  pinMode(pinL_PWM, OUTPUT);
  pinMode(pinR_PWM, OUTPUT);
  
  // initialize output pins
  digitalWrite(pinL_DIR, HIGH);   //forward direction
  digitalWrite(pinR_DIR, HIGH);   //forward direction
  analogWrite(pinL_PWM, 1000);    //forward speed
  analogWrite(pinR_PWM, 1000);   //forward speed
  delay(10);
  digitalWrite(pinL_DIR, LOW); //go backwards for a lil to stop the wheelios
  digitalWrite(pinR_DIR, LOW);
  delay(50);
  analogWrite(pinL_PWM, 0);
  analogWrite(pinR_PWM, 0);  
}

void runLikeTheWind() {
  digitalWrite(pinL_DIR, HIGH);
  digitalWrite(pinR_DIR, HIGH);
  analogWrite(pinL_PWM, 1000);
  analogWrite(pinR_PWM, 1000);
  delay(500);
}

void turnLeftAtY() {
  digitalWrite(pinL_DIR, LOW);
  digitalWrite(pinR_DIR, HIGH);
  analogWrite(pinL_PWM, 90);
  analogWrite(pinR_PWM, 120);
  delay(300);
}

void turnRightAtY() {
  digitalWrite(pinL_DIR, HIGH);
  digitalWrite(pinR_DIR, LOW);
  analogWrite(pinL_PWM, 120);
  analogWrite(pinR_PWM, 90);
  delay(500);
  digitalWrite(pinL_DIR, HIGH);
  digitalWrite(pinR_DIR, HIGH);
  analogWrite(pinL_PWM, 100);
  analogWrite(pinR_PWM, 100);
  delay(300);
}

void loop() {
  leftSensor = digitalRead(pinL_Sensor); //leftSensor = left sensor is on black
  rightSensor = digitalRead(pinR_Sensor);
  bumperSensor = digitalRead(bumper_Sensor);

  //if !bumperSensor start if not started; go back if started

  if(!hasStarted){
    if(!bumperSensor){
      //starting cue
      hasStarted = true;
      runLikeTheWind();
      digitalWrite(pinL_DIR, HIGH);
      digitalWrite(pinR_DIR, HIGH);
      analogWrite(pinL_PWM, 1000);
      analogWrite(pinR_PWM, 1000);
    }
  } else {
    if(!bumperSensor){
      //hit wall at the end of track
      digitalWrite(pinL_DIR, LOW);
      digitalWrite(pinR_DIR, LOW);
      analogWrite(pinL_PWM, 150);
      analogWrite(pinR_PWM, 150);
      delay(750);
      digitalWrite(pinL_DIR, HIGH);
      digitalWrite(pinR_DIR, HIGH);
      analogWrite(pinL_PWM, 100);
      analogWrite(pinR_PWM, 100);
      delay(50);
      analogWrite(pinL_PWM, 0);
      analogWrite(pinR_PWM, 0);
      exit(0);
    }

    if ( !leftSensor && !rightSensor ) {
      //both on white
      //turn left at first two yJunctions, afterwards go right
      if(junctionsPassed < 2){
        turnLeftAtY();
        junctionsPassed++;
        if(junctionsPassed == 2){
          enteredSlightBends = true;
        }
      } else {
        if(!enteredBend){
          //at the third junction turn right
          turnRightAtY();
          enteredBend = true;
        }
      }
    }

    if ( !leftSensor && rightSensor ) {
      //left on white, turn left
      if(enteredBend){
        digitalWrite(pinL_DIR, LOW);
        digitalWrite(pinR_DIR, HIGH);
        analogWrite(pinL_PWM, 140);
        analogWrite(pinR_PWM, 143);
        delay(40);
      } else {
        digitalWrite(pinL_DIR, LOW);
        digitalWrite(pinR_DIR, HIGH);
        analogWrite(pinL_PWM, 140);
        analogWrite(pinR_PWM, 143);    
      }
    }

    if ( leftSensor && !rightSensor ) {
      //right on white, turn right
      if(enteredBend){
        digitalWrite(pinL_DIR, HIGH);
        digitalWrite(pinR_DIR, LOW);
        analogWrite(pinL_PWM, 143);
        analogWrite(pinR_PWM, 140);
        delay(40);
      } else {
      digitalWrite(pinL_DIR, HIGH);
      digitalWrite(pinR_DIR, LOW);
      analogWrite(pinL_PWM, 143);
      analogWrite(pinR_PWM, 140);
      }
    }

    if ( leftSensor && rightSensor ) {
      //both on black, go forwards
      digitalWrite(pinL_DIR, HIGH);
      digitalWrite(pinR_DIR, HIGH);
      if(enteredBend){
        //go slow at bend stage to avoid nyooming 
        analogWrite(pinL_PWM, 140);
        analogWrite(pinR_PWM, 140);
      } else {
        if(enteredSlightBends){
          analogWrite(pinL_PWM, 200);
          analogWrite(pinR_PWM, 200);
        } else {
          analogWrite(pinL_PWM, 185);
          analogWrite(pinR_PWM, 185);
        }
      }
    }
  }
}
