int led = 9; //設定led pin, PWM pin有~3,~5,~6,~9,~10,~11
int brightness = 0; //LED亮度變數
int fadeAmount = 5; //亮度變化變數

void setup() {
  //設定led pin為OUTPUT
  pinMode(led, OUTPUT);  
}

void loop() {
  //PWM輸出
  analogWrite(led, brightness);
 


  //在每次回圈brightness都會累加fadeAmount
  brightness = brightness + fadeAmount;

  //到最亮或最暗時反轉
  if (brightness <= 0 || brightness >= 255) {
    fadeAmount = -fadeAmount;
  }

  //延遲30ms,使呼吸燈效果更好
  delay(30);
}