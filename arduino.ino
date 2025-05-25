#include <Servo.h>

// Servo motorlar için tanımlamalar
Servo servo1;  // 9. pin (donanımsal PWM destekli)
Servo servo2;  // 11. pin (donanımsal PWM destekli)
Servo servo3;  // 6. pin (donanımsal PWM destekli)

void setup() {
  // Seri iletişim başlat
  Serial.begin(9600);

  // Donanımsal PWM pinleri ayarla
  servo1.attach(9);   // Servo Motor 1 -> Pin 9
  servo2.attach(11);  // Servo Motor 2 -> Pin 11
  servo3.attach(6);   // Servo Motor 3 -> Pin 6

  // Servo motorları başlangıç pozisyonuna getir
  servo1.write(0);  // Servo Motor 1 başlangıç pozisyonu
  servo2.write(0);  // Servo Motor 2 başlangıç pozisyonu
  servo3.write(0);  // Servo Motor 3 başlangıç pozisyonu

  Serial.println("Servo motor sistemi hazır. Komut bekleniyor...");
}

void loop() {
  // Seri porttan gelen komutları kontrol et
  if (Serial.available() > 0) {
    char command = Serial.read(); // Gelen komutu oku
    processCommand(command);      // Komutu işleme fonksiyonuna gönder
  }
}

// Gelen komutları işleme
void processCommand(char command) {
  switch (command) {
    case '1':  // Grup 1 için motor hareketi
      Serial.println("Grup 1 tanındı. Servo Motor 1 çalışıyor...");
      servo1.write(90);  // Servo Motor 1, 90 derece hareket eder
      delay(1000);       // 1 saniye bekle
      servo1.write(0);   // Başlangıç pozisyonuna döner
      break;

    case '2':  // Grup 2 için motor hareketi
      Serial.println("Grup 2 tanındı. Servo Motor 2 çalışıyor...");
      servo2.write(90);  // Servo Motor 2, 90 derece hareket eder
      delay(1000);       // 1 saniye bekle
      servo2.write(0);   // Başlangıç pozisyonuna döner
      break;

    case '3':  // Grup 3 için motor hareketi
      Serial.println("Grup 3 tanındı. Servo Motor 3 çalışıyor...");
      servo3.write(90);  // Servo Motor 3, 90 derece hareket eder
      delay(1000);       // 1 saniye bekle
      servo3.write(0);   // Başlangıç pozisyonuna döner
      break;

    default:  // Geçersiz komut
      Serial.println("Geçersiz komut alındı. Motorlar çalışmıyor.");
      break;
  }
}