#include <Servo.h>

#define MAX_SERVOS 8
const int servo_pins[MAX_SERVOS] = {2, 3, 4, 5, 6, 7, 8, 9};
Servo servos[MAX_SERVOS];
bool servo_attached[MAX_SERVOS] = {false, false, false, false, false, false, false, false};

int get_servo_index(int pin) {
  for (int i = 0; i < MAX_SERVOS; i++) {
    if (servo_pins[i] == pin) return i;
  }
  return -1;
}

void setup() {
  Serial.begin(115200);
}

void loop() {
  if (Serial.available() > 0) {
    char data = Serial.read();

    // --- SERVO COMMANDS ---
    if (data == 'A') { // Attach Servo
      while (!Serial.available());
      int pin = Serial.read() - '0';
      int idx = get_servo_index(pin);
      if (idx != -1 && !servo_attached[idx]) {
        servos[idx].attach(pin);
        servo_attached[idx] = true;
      }
    }
    else if (data == 'B') { // Servo auf Winkel stellen
      while (Serial.available() < 2); // Warten auf Pin und mindestens 1 Ziffer
      int pin = Serial.read() - '0';
      int idx = get_servo_index(pin);
      delay(2);
      char winkel_str[4] = {0};

      int i = 0;
      // Bis zu 3 Ziffern für Winkel einlesen (z.B. 180)
      while (i < 3 && Serial.available()) {
        char c = Serial.peek();
        if (c >= '0' && c <= '9') {
          winkel_str[i++] = Serial.read();
        } else {
          break;
        }
      }
      int winkel = atoi(winkel_str);

      if (idx != -1 && servo_attached[idx]) {
        servos[idx].write(winkel);
      }
    }
    else if (data == 'C') { // Detach Servo
      while (!Serial.available());
      int pin = Serial.read() - '0';
      int idx = get_servo_index(pin);
      if (idx != -1 && servo_attached[idx]) {
        servos[idx].detach();
        servo_attached[idx] = false;
      }
    }
    // --- END SERVO COMMANDS ---

    else if (data == 'a') {
      pinMode(2, INPUT);
    } else if (data == 'b') {
      pinMode(3, INPUT);
    } else if (data == 'c') {
      pinMode(4, INPUT);
    } else if (data == 'd') {
      pinMode(5, INPUT);
    } else if (data == 'e') {
      pinMode(6, INPUT);
    } else if (data == 'f') {
      pinMode(7, INPUT);
    } else if (data == 'g') {
      pinMode(8, INPUT);
    } else if (data == 'h') {
      pinMode(9, INPUT);
    } else if (data == 'i') {
      pinMode(10, INPUT);
    } else if (data == 'j') {
      pinMode(11, INPUT);
    } else if (data == 'N') {
      pinMode(12, INPUT);
    } else if (data == 'I') {
      pinMode(13, INPUT);
    }

    else if (data == 'k') {
      pinMode(2, OUTPUT);
    } else if (data == 'l') {
      pinMode(3, OUTPUT);
    } else if (data == 'm') {
      pinMode(4, OUTPUT);
    } else if (data == 'n') {
      pinMode(5, OUTPUT);
    } else if (data == 'o') {
      pinMode(6, OUTPUT);
    } else if (data == 'p') {
      pinMode(7, OUTPUT);
    } else if (data == 'q') {
      pinMode(8, OUTPUT);
    } else if (data == 'r') {
      pinMode(9, OUTPUT);
    } else if (data == 's') {
      pinMode(10, OUTPUT);
    } else if (data == 't') {
      pinMode(11, OUTPUT);
    } else if (data == 'O') {
      pinMode(12, OUTPUT);
    } else if (data == 'L') {
      pinMode(13, OUTPUT);
    }

    else if (data == 'u') {
      digitalWrite(2, HIGH);
    } else if (data == 'v') {
      digitalWrite(3, HIGH);
    } else if (data == 'w') {
      digitalWrite(4, HIGH);
    } else if (data == 'x') {
      digitalWrite(5, HIGH);
    } else if (data == 'y') {
      digitalWrite(6, HIGH);
    } else if (data == 'z') {
      digitalWrite(7, HIGH);
    } else if (data == '0') {
      digitalWrite(8, HIGH);
    } else if (data == '1') {
      digitalWrite(9, HIGH);
    } else if (data == '2') {
      digitalWrite(10, HIGH);
    } else if (data == '3') {
      digitalWrite(11, HIGH);
    } else if (data == 'P') {
      digitalWrite(12, HIGH);
    } else if (data == 'H') {
      digitalWrite(13, HIGH);
    }

    else if (data == '4') {
      digitalWrite(2, LOW);
    } else if (data == '5') {
      digitalWrite(3, LOW);
    } else if (data == '6') {
      digitalWrite(4, LOW);
    } else if (data == '7') {
      digitalWrite(5, LOW);
    } else if (data == '8') {
      digitalWrite(6, LOW);
    } else if (data == '9') {
      digitalWrite(7, LOW);
    } else if (data == '!') {
      digitalWrite(8, LOW);
    } else if (data == '@') {
      digitalWrite(9, LOW);
    } else if (data == '#') {
      digitalWrite(10, LOW);
    } else if (data == '$') {
      digitalWrite(11, LOW);
    } else if (data == 'Q') {
      digitalWrite(12, LOW);
    } else if (data == 'M') {
      digitalWrite(13, LOW);
    }

    else if (data == '%') {
      Serial.write(digitalRead(2));
    } else if (data == '^') {
      Serial.write(digitalRead(3));
    } else if (data == '&') {
      Serial.write(digitalRead(4));
    } else if (data == '*') {
      Serial.write(digitalRead(5));
    } else if (data == '(') {
      Serial.write(digitalRead(6));
    } else if (data == ')') {
      Serial.write(digitalRead(7));
    } else if (data == '-') {
      Serial.write(digitalRead(8));
    } else if (data == '=') {
      Serial.write(digitalRead(9));
    } else if (data == ',') {
      Serial.write(digitalRead(10));
    } else if (data == '.') {
      Serial.write(digitalRead(11));
    } else if (data == '.') {
      Serial.write(digitalRead(12));
    } else if (data == 'R') {
      Serial.write(digitalRead(13));
    }
  }
}
